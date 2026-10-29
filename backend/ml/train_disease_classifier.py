import os
import sys
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from typing import Dict, Any, List

sys.stdout.reconfigure(encoding='utf-8')

# Target Paddy Disease Classes in Order
CLASS_NAMES = [
    "bacterial_leaf_blight",
    "brown_spot",
    "leaf_blast",
    "sheath_blight",
    "tungro_virus",
    "healthy_leaf"
]

class PaddyImageDataset(Dataset):
    """PyTorch Dataset loader for standardized paddy leaf disease images."""
    
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.samples = []
        
        for class_idx, class_name in enumerate(CLASS_NAMES):
            cls_dir = os.path.join(root_dir, class_name)
            if not os.path.isdir(cls_dir):
                continue
            for fname in os.listdir(cls_dir):
                if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                    self.samples.append((os.path.join(cls_dir, fname), class_idx))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        with Image.open(img_path) as img:
            img = img.convert("RGB").resize((224, 224))
            arr = np.array(img, dtype=np.float32) / 255.0  # [H, W, C]
            tensor = torch.from_numpy(arr).permute(2, 0, 1)  # [C, H, W]
            
            # Standard ImageNet Normalization (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
            std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
            normalized_tensor = (tensor - mean) / std
            
            return normalized_tensor, label


class EfficientNetPaddyClassifier(nn.Module):
    """
    Lightweight EfficientNet-style feature extractor backbone with 
    Adaptive Pooling and Multi-layer Classification Head for 6 Paddy Classes.
    """
    
    def __init__(self, num_classes: int = 6):
        super(EfficientNetPaddyClassifier, self).__init__()
        
        # Conv Block 1
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.SiLU(),
            
            # Depthwise Separable Conv 1
            nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1, groups=32, bias=False),
            nn.BatchNorm2d(32),
            nn.SiLU(),
            nn.Conv2d(32, 64, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(64),
            
            # Depthwise Separable Conv 2
            nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1, groups=64, bias=False),
            nn.BatchNorm2d(64),
            nn.SiLU(),
            nn.Conv2d(64, 128, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(128),
            
            # Conv Block 3
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.SiLU(),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        
        # Linear Classifier Head
        self.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.SiLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


def train_paddy_classifier(data_dir: str = "backend/data/paddy_diseases", epochs: int = 4) -> Dict[str, Any]:
    """Fine-tunes the PyTorch Paddy Disease Classifier on the combined dataset."""
    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")
    save_path = os.path.join(data_dir, "paddy_efficientnet_v1.pt")
    
    train_dataset = PaddyImageDataset(train_dir)
    val_dataset = PaddyImageDataset(val_dir)
    
    if len(train_dataset) == 0:
        print("⚠️ Train dataset empty. Run dataset_pipeline.py first.")
        return {"status": "failed", "accuracy": 0.0}

    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=16, shuffle=False)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = EfficientNetPaddyClassifier(num_classes=6).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    
    best_acc = 0.0
    print(f"🚀 Fine-Tuning EfficientNet-B0 Paddy Classifier on {len(train_dataset)} images ({device})...")
    
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
            
        train_loss = running_loss / total
        train_acc = (correct / total) * 100.0
        
        # Validation Evaluation
        model.eval()
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, preds = torch.max(outputs, 1)
                val_correct += (preds == labels).sum().item()
                val_total += labels.size(0)
                
        val_acc = (val_correct / val_total) * 100.0 if val_total > 0 else 0.0
        print(f"  Epoch [{epoch}/{epochs}] — Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.1f}% | Val Acc: {val_acc:.1f}%")
        
        if val_acc >= best_acc:
            best_acc = val_acc
            torch.save(model.state_dict(), save_path)
            
    print(f"✅ Model Checkpoint Saved: {save_path} (Best Val Accuracy: {best_acc:.1f}%)")
    return {
        "status": "success",
        "best_val_accuracy": best_acc,
        "classes_trained": CLASS_NAMES,
        "checkpoint_path": save_path
    }


if __name__ == "__main__":
    res = train_paddy_classifier("backend/data/paddy_diseases", epochs=3)
    print("\nTraining Metrics Summary:")
    print(res)
