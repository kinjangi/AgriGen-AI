import { useState } from 'react';

export default function FieldSelectorBar({
  savedFields,
  activeFieldId,
  onSelectField,
  onOpenAddLocation,
  onEditField,
  onUseLiveLocation,
  isDetectingLocation = false,
  language = 'en'
}) {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const activeField = savedFields.find((f) => f.id === activeFieldId) || savedFields[0];

  const getCropIcon = (cropKey) => {
    switch ((cropKey || '').toLowerCase()) {
      case 'paddy': return '🌾';
      case 'cotton': return '☁️';
      case 'maize': return '🌽';
      case 'chilli': return '🌶️';
      case 'wheat': return '🌾';
      case 'groundnut': return '🥜';
      case 'soybean': return '🌱';
      default: return '🌱';
    }
  };

  return (
    <div className="field-selector-container">
      <div className="field-selector-main">
        {/* Active Field Display Pill */}
        <div className="active-field-pill" onClick={() => setDropdownOpen(!dropdownOpen)}>
          <span className="field-location-icon">📍</span>
          <div className="field-pill-info">
            <span className="field-pill-name">
              {activeField?.name || 'Field #1'} • {getCropIcon(activeField?.crop)} {(activeField?.crop || 'paddy').toUpperCase()}
            </span>
            <span className="field-pill-loc">
              {activeField?.locationName || 'Warangal, Telangana'} {activeField?.sensorId ? '• 📡 IoT Active' : ''}
            </span>
          </div>
          <span className="dropdown-caret">{dropdownOpen ? '▲' : '▼'}</span>
        </div>

        {/* Action Buttons */}
        <div className="field-selector-actions">
          <button 
            className="field-action-btn live-gps" 
            onClick={onUseLiveLocation}
            disabled={isDetectingLocation}
            title="Detect live browser GPS location"
            style={{ backgroundColor: '#15803d', color: '#ffffff', fontWeight: '600' }}
          >
            🎯 {isDetectingLocation 
                  ? (language === 'te' ? 'గుర్తిస్తోంది...' : 'Detecting GPS...') 
                  : (language === 'te' ? 'నా లైవ్ స్థానం' : 'Use My Live GPS')}
          </button>
          <button 
            className="field-action-btn edit" 
            onClick={() => onEditField(activeField)}
            title="Edit Active Field Profile"
          >
            ✏️ {language === 'te' ? 'సవరించు' : 'Edit Field'}
          </button>
          <button 
            className="field-action-btn add" 
            onClick={onOpenAddLocation}
            title="Add New Farm Field Location"
          >
            ➕ {language === 'te' ? 'కొత్త పొలం' : 'Add Field'}
          </button>
        </div>
      </div>

      {/* Dropdown Menu for Switching Fields */}
      {dropdownOpen && (
        <div className="fields-dropdown-menu">
          <div className="dropdown-header-lbl">
            {language === 'te' ? 'మీ రక్షించబడిన పొలాలు:' : 'Select Saved Field Location:'}
          </div>
          <div className="saved-fields-list">
            {savedFields.map((field) => (
              <div 
                key={field.id} 
                className={`field-item-row ${field.id === activeFieldId ? 'active-selected' : ''}`}
                onClick={() => {
                  onSelectField(field.id);
                  setDropdownOpen(false);
                }}
              >
                <div className="field-item-left">
                  <span className="field-item-bullet">{field.id === activeFieldId ? '🟢' : '⚪'}</span>
                  <div>
                    <strong className="field-item-title">{field.name} ({getCropIcon(field.crop)} {field.crop.toUpperCase()})</strong>
                    <div className="field-item-sub">{field.locationName}</div>
                  </div>
                </div>
                {field.sensorId && <span className="sensor-tag">📡 IoT Linked</span>}
              </div>
            ))}
          </div>

          <button 
            className="add-field-menu-btn"
            onClick={() => {
              setDropdownOpen(false);
              onOpenAddLocation();
            }}
          >
            ➕ {language === 'te' ? 'మరో పొలాన్ని జోడించండి' : 'Add Another Farm Location'}
          </button>
        </div>
      )}
    </div>
  );
}
