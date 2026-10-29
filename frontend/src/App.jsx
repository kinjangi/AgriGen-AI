import { useState, useEffect, useRef } from 'react';
import './App.css';
import LocationPickerModal from './components/LocationPickerModal';
import FieldSelectorBar from './components/FieldSelectorBar';

// Custom Agricultural SVG Icon Set
const SproutIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M7 20h10" />
    <path d="M12 20v-8" />
    <path d="M12 12c-3.3 0-6-2.7-6-6 0 0 3.3.5 6 3" />
    <path d="M12 12c3.3 0 6-2.7 6-6 0 0-3.3.5-6 3" />
  </svg>
);

const WaterDropletIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z" />
  </svg>
);

const WeatherSunIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="12" cy="12" r="4" />
    <path d="M12 2v2" strokeLinecap="round" />
    <path d="M12 20v2" strokeLinecap="round" />
    <path d="m4.93 4.93 1.41 1.41" />
    <path d="m17.66 17.66 1.41 1.41" />
    <path d="M2 12h2" strokeLinecap="round" />
    <path d="M20 12h2" strokeLinecap="round" />
    <path d="m6.34 17.66-1.41 1.41" />
    <path d="m19.07 4.93-1.41 1.41" />
  </svg>
);

const MandiChartIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M3 3v18h18" />
    <path d="m19 9-5 5-4-4-3 3" />
  </svg>
);

const ShieldCheckIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    <path d="m9 12 2 2 4-4" />
  </svg>
);

const DroneSensorIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="12" cy="12" r="3" />
    <path d="M4 8l4 4m8 0l4-4" />
    <path d="M4 16l4-4m8 0l4 4" />
    <circle cx="4" cy="8" r="2" />
    <circle cx="20" cy="8" r="2" />
    <circle cx="4" cy="16" r="2" />
    <circle cx="20" cy="16" r="2" />
  </svg>
);

const WheatGrainIcon = ({ size = 20, color = 'currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M2 22 12 12" />
    <path d="M12 12c-2-3-1-7 2-10 3 3 7 4 10 2-3 3-7 4-10 2z" />
    <path d="M9 15c-2-2-1-5 1-7 2 2 5 3 7 1" />
  </svg>
);

// Animated Count-Up Hook
function useAnimatedNumber(targetNumber, duration = 1200) {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    const end = parseFloat(targetNumber) || 0;
    if (end === 0) return;

    let start = 0;
    const startTime = performance.now();

    const update = (now) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const val = start + (end - start) * easeProgress;

      setCurrent(Number.isInteger(end) ? Math.round(val) : parseFloat(val.toFixed(1)));

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    };

    requestAnimationFrame(update);
  }, [targetNumber, duration]);

  return current;
}

function App() {
  // Theme State (default to light Earthy theme)
  const [theme, setTheme] = useState('light');

// Language State ('en' for English, 'te' for Telugu)
  const [language, setLanguage] = useState('en');

  // Helpers for dynamic crop labels
  const getCropDisplayName = (cropKey) => {
    if (!cropKey) return 'Crop';
    const k = cropKey.toLowerCase();
    switch(k) {
      case 'paddy': return 'Paddy';
      case 'cotton': return 'Cotton';
      case 'maize': return 'Maize';
      case 'chilli': return 'Chilli';
      case 'wheat': return 'Wheat';
      case 'groundnut': return 'Groundnut';
      case 'soybean': return 'Soybean';
      default: return cropKey.charAt(0).toUpperCase() + cropKey.slice(1);
    }
  };

  const getCropTeluguName = (cropKey) => {
    if (!cropKey) return 'పంట';
    const k = cropKey.toLowerCase();
    switch(k) {
      case 'paddy': return 'వరి';
      case 'cotton': return 'పత్తి';
      case 'maize': return 'మొక్కజొన్న';
      case 'chilli': return 'మిర్చి';
      case 'wheat': return 'గోధుమ';
      case 'groundnut': return 'వేరుశనగ';
      case 'soybean': return 'సోయాబీన్';
      default: return 'పంట';
    }
  };
  
  // Navigation & Active Scroll-Spy Section State
  const [activeSection, setActiveSection] = useState('hero');
  const [health, setHealth] = useState(null);

  // Floating Persistent Chat Widget State
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [unreadBadgeCount, setUnreadBadgeCount] = useState(0);
  
  // Live Location-Based Telemetry & Multi-Field Location State
  const defaultFields = [
    {
      id: 'field_1',
      name: 'Field #1 (North Plot)',
      crop: 'paddy',
      locationName: 'Warangal, Telangana',
      district: 'Warangal',
      state: 'Telangana',
      lat: 18.0000,
      lon: 79.5833,
      sensorId: ''
    },
    {
      id: 'field_2',
      name: 'Field #2 (East Plot)',
      crop: 'chilli',
      locationName: 'Kothagudem, Telangana',
      district: 'Bhadradri Kothagudem',
      state: 'Telangana',
      lat: 17.5511,
      lon: 80.6178,
      sensorId: 'IOT-SENS-402'
    },
    {
      id: 'field_3',
      name: 'Field #3 (Coastal Plot)',
      crop: 'paddy',
      locationName: 'Razam, Andhra Pradesh',
      district: 'Srikakulam',
      state: 'Andhra Pradesh',
      lat: 18.4491,
      lon: 83.6596,
      sensorId: ''
    }
  ];

  const [savedFields, setSavedFields] = useState(() => {
    try {
      const saved = localStorage.getItem('agrigen_saved_fields');
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn("Failed to load fields from localStorage", e);
    }
    return defaultFields;
  });

  const [activeFieldId, setActiveFieldId] = useState(() => {
    try {
      const savedId = localStorage.getItem('agrigen_active_field_id');
      if (savedId) return savedId;
    } catch (e) {
      // ignore
    }
    return 'field_1';
  });

  const [isLocationModalOpen, setIsLocationModalOpen] = useState(false);
  const [editingField, setEditingField] = useState(null);
  const [isDetectingLocation, setIsDetectingLocation] = useState(false);

  const activeField = savedFields.find(f => f.id === activeFieldId) || savedFields[0] || defaultFields[0];

  const handleGetLiveLocation = () => {
    if (!navigator.geolocation) {
      alert(language === 'te' 
        ? 'మీ బ్రౌజర్ స్థాన (GPS) సేవకు మద్దతు ఇవ్వదు. దయచేసి మాన్యువల్‌గా స్థానాన్ని ఎంచుకోండి.' 
        : 'Geolocation is not supported by your browser. Please select location manually.');
      return;
    }

    setIsDetectingLocation(true);
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const lat = parseFloat(position.coords.latitude.toFixed(4));
        const lon = parseFloat(position.coords.longitude.toFixed(4));

        try {
          const res = await fetch(`http://agrigen-ai.onrender.com/api/v1/telemetry/overview?lat=${lat}&lon=${lon}&crop=${activeField.crop}&field_name=${encodeURIComponent('Live GPS Location')}`);
          if (res.ok) {
            const data = await res.json();
            const locationName = data.location?.name || `GPS (${lat}, ${lon})`;

            const gpsField = {
              id: 'field_gps',
              name: `🎯 My Live GPS Plot`,
              crop: activeField.crop || 'paddy',
              locationName: locationName,
              district: data.location?.district || 'Detected Region',
              state: data.location?.state || 'India',
              lat: lat,
              lon: lon,
              sensorId: 'GPS-LIVE'
            };

            setSavedFields(prev => [gpsField, ...prev.filter(f => f.id !== 'field_gps')]);
            setActiveFieldId('field_gps');
            setIsDetectingLocation(false);
            fetchTelemetry(false);
            alert(language === 'te' ? `స్థానం విజయవంతంగా లభ్యమైంది: ${locationName}` : `GPS Location captured: ${locationName}`);
            return;
          }
        } catch (e) {
          console.warn("Reverse geocode failed for GPS coords, using direct lat/lon", e);
        }

        const gpsField = {
          id: 'field_gps',
          name: `🎯 My Live GPS Plot`,
          crop: activeField.crop || 'paddy',
          locationName: `GPS (${lat}, ${lon})`,
          district: 'Detected Location',
          state: 'India',
          lat: lat,
          lon: lon,
          sensorId: 'GPS-LIVE'
        };

        setSavedFields(prev => [gpsField, ...prev.filter(f => f.id !== 'field_gps')]);
        setActiveFieldId('field_gps');
        setIsDetectingLocation(false);
        fetchTelemetry(false);
      },
      (error) => {
        console.warn("Geolocation permission error or timeout:", error);
        setIsDetectingLocation(false);
        alert(language === 'te' 
          ? 'స్థాన అనుమతి తిరస్కరించబడింది. దయచేసి ఎంచుకున్న పొలం స్థానాన్ని ఉపయోగించండి.' 
          : 'GPS location permission denied or timed out. Falling back to selected saved field location.');
      },
      { timeout: 10000, enableHighAccuracy: true }
    );
  };

  useEffect(() => {
    try {
      localStorage.setItem('agrigen_saved_fields', JSON.stringify(savedFields));
    } catch (e) {
      console.warn("Failed to save fields to localStorage", e);
    }
  }, [savedFields]);

  useEffect(() => {
    try {
      localStorage.setItem('agrigen_active_field_id', activeFieldId);
    } catch (e) {
      // ignore
    }
  }, [activeFieldId]);

  const [telemetry, setTelemetry] = useState(null);
  const [hasScannedCrop, setHasScannedCrop] = useState(false);

  // Voice Assistant State (STT & TTS)
  const [isListening, setIsListening] = useState(false);
  const [autoPlayVoice, setAutoPlayVoice] = useState(true);
  const [currentlyPlayingIdx, setCurrentlyPlayingIdx] = useState(null);
  const recognitionRef = useRef(null);
  const audioPlayerRef = useRef(new Audio());

  // Initial Welcome Messages per language
  const initialMessages = {
    en: [
      {
        sender: 'ai',
        text: '🌾 **Welcome to AgriGen AI**\nI am your autonomous agricultural advisor. How can I assist with your crops, soil management, or market predictions today? Feel free to speak or attach photos/PDFs/videos!',
        time: 'Just now'
      }
    ],
    te: [
      {
        sender: 'ai',
        text: '🌾 **అగ్రిజెన్ AI సలహా కేంద్రానికి స్వాగతం**\nనేను మీ డిజిటల్ వ్యవసాయ సలహాదారుడిని. మీ పంటలు, ఎరువుల యాజమాన్యం, లేదా మార్కెట్ ధరల గురించి ఏమైనా అడగండి. మీరు మాట్లాడవచ్చు లేదా పంట ఫోటోలు, PDF పత్రాలు, లేదా వీడియోలను అప్‌లోడ్ చేయవచ్చు.',
        time: 'ఇప్పుడే'
      }
    ]
  };

  // Persistent Chat History in LocalStorage
  const [messages, setMessages] = useState(() => {
    try {
      const saved = localStorage.getItem('agrigen_chat_history');
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn("Failed to load chat history from localStorage", e);
    }
    return initialMessages.en;
  });

  useEffect(() => {
    try {
      localStorage.setItem('agrigen_chat_history', JSON.stringify(messages));
    } catch (e) {
      console.warn("Failed to save chat history to localStorage", e);
    }
  }, [messages]);

  // Persistent Behavioral Profile (Interests, Crop focus, Preferences across chat resets)
  const [userInterests, setUserInterests] = useState(() => {
    try {
      const saved = localStorage.getItem('agrigen_user_interests');
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn("Failed to load user interests from localStorage", e);
    }
    return ['paddy', 'fertilizer', 'weather', 'mandi rates'];
  });

  useEffect(() => {
    try {
      localStorage.setItem('agrigen_user_interests', JSON.stringify(userInterests));
    } catch (e) {
      console.warn("Failed to save user interests to localStorage", e);
    }
  }, [userInterests]);

  const updateInterestsFromQuery = (queryText) => {
    if (!queryText) return;
    const lower = queryText.toLowerCase();
    const keywords = ['fertilizer', 'disease', 'pest', 'weather', 'rain', 'mandi', 'price', 'market', 'irrigation', 'soil', 'paddy', 'cotton', 'maize', 'chilli', 'wheat'];
    const found = keywords.filter(k => lower.includes(k));
    if (found.length > 0) {
      setUserInterests(prev => Array.from(new Set([...prev, ...found])));
    }
  };

  const resetChat = () => {
    if (audioPlayerRef.current) {
      audioPlayerRef.current.pause();
    }
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    setCurrentlyPlayingIdx(null);
    setAttachments([]);
    setInputQuery('');
    const freshMessages = initialMessages[language] || initialMessages.en;
    setMessages(freshMessages);
    try {
      localStorage.removeItem('agrigen_chat_history');
    } catch (e) {
      console.warn("Failed to clear chat history from localStorage", e);
    }
  };

  const [inputQuery, setInputQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  // File Upload State
  const [attachments, setAttachments] = useState([]);
  const fileInputRef = useRef(null);
  const [activePreviewImage, setActivePreviewImage] = useState(null);

  // Toggle Theme
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  // Handle Language Change
  const handleLanguageChange = (newLang) => {
    setLanguage(newLang);
    setMessages(initialMessages[newLang] || initialMessages.en);
    if (isListening && recognitionRef.current) {
      recognitionRef.current.stop();
      setIsListening(false);
    }
  };

  // Field Management Handlers
  const handleSaveField = (fieldObj) => {
    setSavedFields((prev) => {
      const exists = prev.some(f => f.id === fieldObj.id);
      if (exists) {
        return prev.map(f => f.id === fieldObj.id ? fieldObj : f);
      }
      return [...prev, fieldObj];
    });
    setActiveFieldId(fieldObj.id);
  };

  const handleOpenAddLocation = () => {
    setEditingField(null);
    setIsLocationModalOpen(true);
  };

  const handleEditField = (fieldToEdit) => {
    setEditingField(fieldToEdit);
    setIsLocationModalOpen(true);
  };

  // Fetch Live Telemetry Data tied to active field's coordinates & crop
  const fetchTelemetry = (scanned = hasScannedCrop, targetField = activeField) => {
    if (!targetField) return;
    console.log(`[Open-Meteo Weather Fetch] Requesting live weather for '${targetField.name}' at Lat: ${targetField.lat}, Lon: ${targetField.lon}`);
    const url = `http://https://agrigen-ai.onrender.com/api/v1/telemetry/overview?lat=${targetField.lat}&lon=${targetField.lon}&crop=${encodeURIComponent(targetField.crop)}&field_name=${encodeURIComponent(targetField.name)}&sensor_id=${encodeURIComponent(targetField.sensorId || '')}&scanned=${scanned}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        console.log(`[Open-Meteo Weather Success] Received live temp: ${data?.soil_temp_humidity?.air_temp}°C for ${data?.location?.name}`);
        setTelemetry(data);
      })
      .catch((err) => console.error("Telemetry fetch error: ", err));
  };

  // Backend Health Check & Telemetry Polling
  useEffect(() => {
    fetch('http://agrigen-ai.onrender.com/api/v1/health')
      .then((res) => res.json())
      .then((data) => setHealth(data))
      .catch((err) => console.error("Health check error: ", err));

    fetchTelemetry(hasScannedCrop, activeField);

    const interval = setInterval(() => {
      fetchTelemetry(hasScannedCrop, activeField);
    }, 15 * 60 * 1000);

    return () => clearInterval(interval);
  }, [hasScannedCrop, activeFieldId, savedFields]);

  // Scroll-Spy Setup for Smooth Navigation
  useEffect(() => {
    const handleScroll = () => {
      const sections = ['hero', 'overview', 'market', 'assistant', 'tools'];
      const scrollPosition = window.scrollY + 200;

      for (const sectionId of sections) {
        const el = document.getElementById(sectionId);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPosition >= top && scrollPosition < top + height) {
            setActiveSection(sectionId);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
      setActiveSection(id);
    }
  };

  // Open Chat Overlay with Optional Context Query
  const openChatWithQuery = (queryText) => {
    setIsChatOpen(true);
    setUnreadBadgeCount(0);
    if (queryText) {
      handleSend(queryText);
    }
  };

  const toggleChatOverlay = () => {
    if (!isChatOpen) {
      setUnreadBadgeCount(0);
    }
    setIsChatOpen(!isChatOpen);
  };

  // Auto Scroll Chat
  useEffect(() => {
    if (isChatOpen) {
      chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, loading, isChatOpen]);

  // Initialize Speech Recognition (STT)
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = true;

      recognition.onstart = () => {
        setIsListening(true);
      };

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        setInputQuery(transcript);
      };

      recognition.onerror = (event) => {
        console.warn('Speech recognition notice/error:', event.error);
        setIsListening(false);
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognitionRef.current = recognition;
    }
  }, []);

  // Toggle Microphone (STT)
  const toggleListening = () => {
    if (!recognitionRef.current) {
      alert(language === 'te' ? 'మీ బ్రౌజర్ స్పీచ్ రికగ్నిషన్‌కు మద్దతు ఇవ్వదు.' : 'Speech recognition is not supported in this browser.');
      return;
    }

    if (isListening) {
      try {
        recognitionRef.current.stop();
      } catch (e) {
        console.warn("Stop error:", e);
      }
      setIsListening(false);
    } else {
      recognitionRef.current.lang = language === 'te' ? 'te-IN' : 'en-US';
      try {
        recognitionRef.current.stop();
      } catch (e) {
        // ignore
      }
      setTimeout(() => {
        try {
          recognitionRef.current.start();
          setIsListening(true);
        } catch (err) {
          console.error("Start recognition error:", err);
          setIsListening(false);
        }
      }, 50);
    }
  };

  // Speech Output (TTS)
  const speakMessage = async (text, msgIdx) => {
    if (currentlyPlayingIdx === msgIdx) {
      audioPlayerRef.current.pause();
      window.speechSynthesis?.cancel();
      setCurrentlyPlayingIdx(null);
      return;
    }

    audioPlayerRef.current.pause();
    window.speechSynthesis?.cancel();

    const cleanText = text.replace(/[*#🌾•]/g, '').trim();
    if (!cleanText) return;

    setCurrentlyPlayingIdx(msgIdx);

    try {
      const res = await fetch('http://agrigen-ai.onrender.com/api/v1/orchestrator/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: cleanText, language: language })
      });

      if (res.ok) {
        const data = await res.json();
        audioPlayerRef.current.src = data.audio_url;
        audioPlayerRef.current.play();
        audioPlayerRef.current.onended = () => setCurrentlyPlayingIdx(null);
        return;
      }
    } catch (e) {
      console.warn("Backend TTS failed, falling back to Web Speech Synthesis", e);
    }

    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.lang = language === 'te' ? 'te-IN' : 'en-US';
      utterance.onend = () => setCurrentlyPlayingIdx(null);
      utterance.onerror = () => setCurrentlyPlayingIdx(null);
      window.speechSynthesis.speak(utterance);
    } else {
      setCurrentlyPlayingIdx(null);
    }
  };

  // File Selection Handler with Size & Type Validation
  const handleFileSelect = (e) => {
    const files = Array.from(e.target.files);
    if (!files.length) return;

    const newAttachments = [];
    for (const file of files) {
      const type = file.type || '';
      const sizeMB = file.size / (1024 * 1024);
      let category = 'file';

      if (type.startsWith('image/') || file.name.match(/\.(jpg|jpeg|png|heic|webp)$/i)) {
        category = 'image';
        if (sizeMB > 10) {
          alert(`Image "${file.name}" exceeds max limit of 10MB.`);
          continue;
        }
        setHasScannedCrop(true);
        fetchTelemetry(true);
      } else if (type === 'application/pdf' || file.name.endsWith('.pdf')) {
        category = 'pdf';
        if (sizeMB > 20) {
          alert(`PDF "${file.name}" exceeds max limit of 20MB.`);
          continue;
        }
      } else if (type.startsWith('video/') || file.name.match(/\.(mp4|mov|webm|avi)$/i)) {
        category = 'video';
        if (sizeMB > 50) {
          alert(`Video "${file.name}" exceeds max limit of 50MB.`);
          continue;
        }
      } else {
        alert(`Unsupported file type: ${file.name}. Allowed: Images, PDFs, Videos.`);
        continue;
      }

      const previewUrl = category === 'image' || category === 'video' ? URL.createObjectURL(file) : null;
      newAttachments.push({
        file,
        name: file.name,
        size: (file.size / 1024).toFixed(1) + ' KB',
        category,
        previewUrl
      });
    }

    setAttachments((prev) => [...prev, ...newAttachments]);
    if (fileInputRef.current) fileInputRef.current.value = '';
    
    // Ensure floating widget is open when user selects files
    setIsChatOpen(true);
  };

  const removeAttachment = (index) => {
    setAttachments((prev) => prev.filter((_, i) => i !== index));
  };

  // Handle Chat Message Sending
  const handleSend = async (queryText) => {
    const textToSend = queryText || inputQuery.trim();
    if ((!textToSend && !attachments.length) || loading) return;

    if (isListening && recognitionRef.current) {
      recognitionRef.current.stop();
      setIsListening(false);
    }

    const timeString = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const currentAttachments = [...attachments];

    setMessages((prev) => [
      ...prev,
      {
        sender: 'user',
        text: textToSend,
        attachments: currentAttachments,
        time: timeString
      }
    ]);

    if (!queryText) setInputQuery('');
    setAttachments([]);
    setLoading(true);

    updateInterestsFromQuery(textToSend);

    // Build rich persistent behavioral profile context
    const userProfileContext = {
      active_field: {
        id: activeField.id,
        name: activeField.name,
        crop: activeField.crop,
        location_name: activeField.locationName || activeField.name,
        district: activeField.district || '',
        state: activeField.state || '',
        lat: activeField.lat,
        lon: activeField.lon
      },
      saved_fields: savedFields.map(f => ({ name: f.name, crop: f.crop, location: f.locationName })),
      interests: userInterests,
      preferred_language: language
    };

    try {
      let response;
      if (currentAttachments.length > 0) {
        const formData = new FormData();
        formData.append('query', textToSend || (language === 'te' ? 'అటాచ్ చేసిన ఫైల్‌ను విశ్లేషించండి' : 'Analyze attached file'));
        formData.append('language', language);
        formData.append('lat', activeField.lat);
        formData.append('lon', activeField.lon);
        formData.append('crop', activeField.crop);
        formData.append('location_name', activeField.locationName || activeField.name);
        formData.append('user_profile', JSON.stringify(userProfileContext));
        currentAttachments.forEach((item) => {
          formData.append('files', item.file);
        });

        response = await fetch('http://agrigen-ai.onrender.com/api/v1/orchestrator/chat_with_files', {
          method: 'POST',
          body: formData,
        });
      } else {
        response = await fetch('http://agrigen-ai.onrender.com/api/v1/orchestrator/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: textToSend,
            language: language,
            lat: activeField.lat,
            lon: activeField.lon,
            crop: activeField.crop,
            location_name: activeField.locationName || activeField.name,
            user_profile: userProfileContext
          }),
        });
      }

      if (!response.ok) throw new Error(`Server returned status ${response.status}`);

      const aiMsgIndex = messages.length + 1;
      setMessages((prev) => [
        ...prev,
        { sender: 'ai', text: '', time: timeString }
      ]);

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let aiResponseText = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split('\n');
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.replace('data: ', '').trim();
            if (data === '[DONE]') break;
            if (data) {
              aiResponseText += (aiResponseText ? ' ' : '') + data;
              setMessages((prev) => {
                const updated = [...prev];
                updated[updated.length - 1] = {
                  sender: 'ai',
                  text: aiResponseText,
                  time: timeString
                };
                return updated;
              });
            }
          }
        }
      }

      // If widget is closed when AI responds, increment unread badge
      if (!isChatOpen) {
        setUnreadBadgeCount((prev) => prev + 1);
      }

      if (autoPlayVoice && aiResponseText) {
        speakMessage(aiResponseText, aiMsgIndex);
      }

    } catch (err) {
      console.error('Chat error:', err);
      const isNetworkErr = !navigator.onLine || (err.message && (err.message.includes('fetch') || err.message.includes('Network') || err.message.includes('status')));
      const errorMsg = language === 'te' 
        ? (isNetworkErr 
            ? '⚠️ బ్యాకెండ్ సర్వర్ (పోర్ట్ 8000) అందుబాటులో లేదు. దయచేసి "npm run dev" లేదా సర్వర్‌ను ప్రారంభించండి.'
            : '⚠️ సేవ తాత్కాలికంగా అందుబాటులో లేదు. దయచేసి మళ్లీ ప్రయత్నించండి.')
        : (isNetworkErr
            ? '⚠️ Cannot reach backend server at http://agrigen-ai.onrender.com. Please ensure the backend server is running (e.g. run "npm run dev").'
            : '⚠️ Service temporarily unavailable. Please verify your server connection.');

      setMessages((prev) => [
        ...prev,
        {
          sender: 'ai',
          text: errorMsg,
          time: timeString
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSend();
  };

  return (
    <div className="app-container">
      {/* Sticky Navigation Top Header Bar */}
      <header className="header-bar sticky-nav">
        <div className="brand-section" onClick={() => scrollToSection('hero')}>
          <div className="brand-icon">🌱</div>
          <div className="brand-title">
            AgriGen AI
            <span className="brand-tag">v1.0 Live</span>
          </div>
        </div>

        {/* Scroll-Spy Section Anchor Navigation */}
        <nav className="header-nav-links">
          <button 
            className={`nav-link-btn ${activeSection === 'hero' ? 'active' : ''}`}
            onClick={() => scrollToSection('hero')}
          >
            🏠 {language === 'te' ? 'హోమ్' : 'Home'}
          </button>
          <button 
            className={`nav-link-btn ${activeSection === 'overview' ? 'active' : ''}`}
            onClick={() => scrollToSection('overview')}
          >
            📊 {language === 'te' ? 'ఓవర్‌వ్యూ' : 'Farm Overview'}
          </button>
          <button 
            className={`nav-link-btn ${activeSection === 'market' ? 'active' : ''}`}
            onClick={() => scrollToSection('market')}
          >
            📈 {language === 'te' ? 'మార్కెట్' : 'Market Forecast'}
          </button>
          <button 
            className={`nav-link-btn ${activeSection === 'assistant' ? 'active' : ''}`}
            onClick={() => scrollToSection('assistant')}
          >
            🤖 {language === 'te' ? 'AI అసిస్టెంట్' : 'AI Assistant'}
          </button>
          <button 
            className={`nav-link-btn ${activeSection === 'tools' ? 'active' : ''}`}
            onClick={() => scrollToSection('tools')}
          >
            🛠️ {language === 'te' ? 'పరికరాలు' : 'Tools & Reports'}
          </button>
        </nav>

        <div className="header-actions">
          {/* Weather Widget Snapshot Pill */}
          <div className="header-weather-pill">
            <span>{telemetry?.soil_temp_humidity?.icon || '🌤️'}</span> 
            {telemetry?.soil_temp_humidity?.air_temp || 24}°C • Soil {telemetry?.soil_moisture?.value || 81}%
          </div>

          {/* Language Switcher */}
          <div className="lang-switcher">
            <button 
              className={`lang-btn ${language === 'en' ? 'active' : ''}`}
              onClick={() => handleLanguageChange('en')}
            >
              🇬🇧 EN
            </button>
            <button 
              className={`lang-btn ${language === 'te' ? 'active' : ''}`}
              onClick={() => handleLanguageChange('te')}
            >
              🇮🇳 తెలుగు
            </button>
          </div>

          <div className={`status-pill ${health?.status === 'active' ? 'online' : 'offline'}`}>
            <span className="status-dot"></span>
            {health?.status === 'active' 
              ? (language === 'te' ? 'లైవ్' : 'Operational') 
              : (language === 'te' ? 'ఆఫ్‌లైన్' : 'Offline')}
          </div>

          <button 
            className="theme-toggle-btn"
            onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
            title="Toggle Light/Dark Theme"
          >
            {theme === 'light' ? '🌙' : '☀️'}
          </button>
        </div>
      </header>

      {/* Main Multi-Section Scrollable Body */}
      <main className="website-body">

        {/* SECTION 1: HERO / LANDING */}
        <section id="hero" className="site-section hero-section">
          <div className="hero-content">
            <span className="hero-badge animate-fade-in">
              <SproutIcon size={16} color="#72d588" /> 
              {language === 'te' ? 'AI ఆధారిత స్వయంప్రతిపత్తి వ్యవసాయ వేదిక' : 'AI-Powered Smart Farming for Every Field'}
            </span>

            <h1 className="hero-title animate-fade-in">
              {language === 'te' ? (
                <>
                  <span className="highlight-green">ఖచ్చితమైన వ్యవసాయం</span> & <span className="highlight-terracotta">AI స్వయంప్రతిపత్తి</span> సలహా కేంద్రం
                </>
              ) : (
                <>
                  <span className="highlight-green">Precision</span> Telemetry & <span className="highlight-terracotta">Autonomous</span> Agronomist Guidance
                </>
              )}
            </h1>

            <p className="hero-description animate-fade-in">
              {language === 'te'
                ? 'ఓపెన్-మీటియో లైవ్ వాతావరణం, అగ్‌మార్క్‌నెట్ మార్కెట్ ధరల అంచనాలు, ఆకు తెగుళ్ల నివారణ, మరియు వాయిస్ కమాండ్లతో మీ పంట దిగుబడిని పెంచుకోండి.'
                : 'Empower your farm with real-time Open-Meteo telemetry, Agmarknet mandi forecasts, YOLOv11 leaf disease diagnostics, and voice-assisted advisors in English & Telugu.'}
            </p>

            <div className="hero-cta-group animate-fade-in">
              <button className="cta-btn primary" onClick={() => scrollToSection('overview')}>
                <DroneSensorIcon size={20} color="#ffffff" />
                {language === 'te' ? 'ఫార్మ్ ఓవర్‌వ్యూ చూడండి' : 'Explore Farm Telemetry'}
              </button>
              <button className="cta-btn secondary" onClick={() => openChatWithQuery('')}>
                <SproutIcon size={20} color="#ffffff" />
                {language === 'te' ? 'AI నిపుణుడితో మాట్లాడండి' : 'Talk to AI Agronomist'}
              </button>
            </div>

            {/* Trust & Credibility Strip */}
            <div className="hero-trust-strip animate-fade-in">
              <div className="trust-badge-item">
                <WeatherSunIcon size={16} color="#81c784" />
                <span>Open-Meteo Telemetry</span>
              </div>
              <div className="trust-badge-divider"></div>
              <div className="trust-badge-item">
                <MandiChartIcon size={16} color="#f7a862" />
                <span>Agmarknet Mandi Feeds</span>
              </div>
              <div className="trust-badge-divider"></div>
              <div className="trust-badge-item">
                <ShieldCheckIcon size={16} color="#81c784" />
                <span>YOLOv11 Deep Learning</span>
              </div>
              <div className="trust-badge-divider"></div>
              <div className="trust-badge-item">
                <WheatGrainIcon size={16} color="#f7a862" />
                <span>12,400+ Acres Monitored</span>
              </div>
            </div>

            {/* Live Location Telemetry Snapshot Widget */}
            <div className="hero-snapshot-card animate-fade-in">
              <div className="snapshot-header">
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <DroneSensorIcon size={18} color="var(--primary)" />
                  {telemetry?.location?.name || `${activeField?.locationName} — ${activeField?.name}`}
                </span>
                <span className="live-pulse-badge">
                  <span className="live-pulse-ring"></span>
                  Live Telemetry
                </span>
              </div>
              <div className="snapshot-stats-row">
                <div className="snapshot-stat">
                  <span className="snapshot-stat-lbl">
                    <WeatherSunIcon size={14} color="var(--accent)" />
                    {language === 'te' ? 'వాతావరణం' : 'Weather'}
                  </span>
                  <span className="snapshot-stat-val">
                    {telemetry?.soil_temp_humidity?.air_temp || 27.5}°C
                  </span>
                </div>
                <div className="snapshot-stat">
                  <span className="snapshot-stat-lbl">
                    <WaterDropletIcon size={14} color="#0284c7" />
                    {language === 'te' ? 'నేల తేమ' : 'Soil Moisture'}
                  </span>
                  <span className="snapshot-stat-val">
                    {telemetry?.soil_moisture?.value || 81}%
                  </span>
                </div>
                <div className="snapshot-stat">
                  <span className="snapshot-stat-lbl">
                    <MandiChartIcon size={14} color="var(--primary)" />
                    {telemetry?.market_rate?.label || (language === 'te' ? `${getCropTeluguName(activeField?.crop)} మార్కెట్ ధర` : `${getCropDisplayName(activeField?.crop)} Market Rate`)}
                  </span>
                  <span className="snapshot-stat-val">
                    ₹{telemetry?.market_rate?.price || 2450} / Qtl
                  </span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION 2: FARM OVERVIEW (LIVE STATS) */}
        <section id="overview" className="site-section overview-section">
          <div className="section-header">
            <h2 className="section-title" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '12px' }}>
              <MandiChartIcon size={28} color="var(--primary)" />
              {language === 'te' ? 'ఫార్మ్ ఓవర్‌వ్యూ & లైవ్ సమాచారం' : 'Farm Overview & Live Telemetry Metrics'}
            </h2>
            <p className="section-subtitle">
              {language === 'te' 
                ? 'లైవ్ సెన్సార్ సమాచారం, ఓపెన్-మీటియో వాతావరణం, మరియు అగ్‌మార్క్‌నెట్ మార్కెట్ ధరలు' 
                : 'Real-time environmental telemetry, soil moisture estimates, and government mandi price feeds updated every 15 minutes.'}
            </p>
          </div>

          {/* Interactive Field Selector Bar */}
          <FieldSelectorBar 
            savedFields={savedFields}
            activeFieldId={activeFieldId}
            onSelectField={(id) => setActiveFieldId(id)}
            onOpenAddLocation={handleOpenAddLocation}
            onEditField={handleEditField}
            onUseLiveLocation={handleGetLiveLocation}
            isDetectingLocation={isDetectingLocation}
            language={language}
          />

          {/* Localized Agronomic Microclimate & Pest Risk Alerts */}
          {telemetry?.risk_alerts && telemetry.risk_alerts.length > 0 && (
            <div className="risk-alerts-container">
              {telemetry.risk_alerts.map((alert, idx) => (
                <div key={idx} className={`risk-alert-card ${alert.type}`}>
                  <span className="risk-alert-icon">
                    {alert.type === 'warning' ? '⚠️' : alert.type === 'caution' ? '☀️' : '🌱'}
                  </span>
                  <div className="risk-alert-content">
                    <h4>{alert.title}</h4>
                    <p>{alert.desc}</p>
                    <span className="risk-rec-tag">💡 Advisory: {alert.recommendation}</span>
                  </div>
                </div>
              ))}
            </div>
          )}

          <div className="metrics-cards-grid">
            {/* Card 1: Soil Moisture */}
            <div className="metric-card-expanded">
              <div className="metric-card-watermark">
                <WaterDropletIcon size={90} color="var(--primary)" />
              </div>
              <div className="metric-header">
                <div className="metric-title-group">
                  <div className="metric-icon-wrap">
                    <WaterDropletIcon size={20} color="#0284c7" />
                  </div>
                  <span className="metric-label">{language === 'te' ? 'నేల తేమ శాతం' : 'Soil Moisture'}</span>
                </div>
                <span className="trend-badge positive">
                  {telemetry?.soil_moisture?.status || (language === 'te' ? 'ఉత్తమం' : 'Optimal')}
                </span>
              </div>
              <div className="metric-value-row">
                <span className="metric-number">
                  {telemetry?.soil_moisture?.value || 81}<span className="metric-unit">%</span>
                </span>
              </div>
              <div className="metric-subtext">
                {telemetry?.soil_moisture?.method || (language === 'te' ? 'అంచనా (నేల నమూనా + వర్షపాతం)' : 'Estimated (Soil Model + Rainfall)')}
              </div>
              <div className="progress-bar-bg">
                <div className="progress-bar-fill" style={{ width: `${telemetry?.soil_moisture?.value || 81}%` }}></div>
              </div>
              <div className="source-attribution-tag">
                {telemetry?.soil_moisture?.source || 'Source: Open-Meteo Telemetry'} • {telemetry?.soil_moisture?.updated || 'Updated 2 mins ago'}
              </div>
            </div>

            {/* Card 2: Weather & Soil Temp/Humidity */}
            <div className="metric-card-expanded">
              <div className="metric-card-watermark">
                <WeatherSunIcon size={90} color="var(--accent)" />
              </div>
              <div className="metric-header">
                <div className="metric-title-group">
                  <div className="metric-icon-wrap">
                    <WeatherSunIcon size={20} color="var(--accent)" />
                  </div>
                  <span className="metric-label">{language === 'te' ? 'నేల ఉష్ణోగ్రత & తేమ' : 'Weather & Soil Temp'}</span>
                </div>
                <span className="trend-badge positive">Live</span>
              </div>
              <div className="metric-value-row">
                <span className="metric-number">
                  {telemetry?.soil_temp_humidity?.air_temp || 27.5}<span className="metric-unit">°C / {telemetry?.soil_temp_humidity?.humidity || 77}%</span>
                </span>
              </div>
              <div className="metric-subtext">
                🌤️ {telemetry?.soil_temp_humidity?.condition || 'Overcast'} (Soil: {telemetry?.soil_temp_humidity?.soil_temp || 26}°C)
              </div>
              <div className="progress-bar-bg">
                <div className="progress-bar-fill" style={{ width: `${telemetry?.soil_temp_humidity?.humidity || 77}%`, backgroundColor: 'var(--accent)' }}></div>
              </div>
              <div className="source-attribution-tag">
                {telemetry?.soil_temp_humidity?.source || 'Source: Open-Meteo Live API'} • {telemetry?.soil_temp_humidity?.updated || 'Updated 2 mins ago'}
              </div>
            </div>

            {/* Card 3: Mandi Market Rate */}
            <div className="metric-card-expanded">
              <div className="metric-card-watermark">
                <MandiChartIcon size={90} color="var(--primary)" />
              </div>
              <div className="metric-header">
                <div className="metric-title-group">
                  <div className="metric-icon-wrap">
                    <MandiChartIcon size={20} color="var(--primary)" />
                  </div>
                  <span className="metric-label">
                    {telemetry?.market_rate?.label || (language === 'te' ? `${getCropTeluguName(activeField?.crop)} మార్కెట్ ధర` : `${getCropDisplayName(activeField?.crop)} Mandi Rate`)}
                  </span>
                </div>
                <span className="trend-badge positive">+4.2% wk</span>
              </div>
              <div className="metric-value-row">
                <span className="metric-number">
                  ₹{telemetry?.market_rate?.price || 2450}<span className="metric-unit">{language === 'te' ? '/ క్వింటాల్' : '/ Qtl'}</span>
                </span>
              </div>
              <div className="metric-subtext">
                🏢 {telemetry?.market_rate?.mandi_name || (language === 'te' ? 'సమీప మండీ' : 'Nearest Mandi')}
              </div>
              <div className="progress-bar-bg">
                <div className="progress-bar-fill" style={{ width: '78%', backgroundColor: 'var(--primary)' }}></div>
              </div>
              <div className="source-attribution-tag">
                {telemetry?.market_rate?.source || 'Source: Agmarknet (Govt of India)'} • {telemetry?.market_rate?.updated || 'Updated Today'}
              </div>
            </div>

            {/* Card 4: Crop Health Score */}
            <div className="metric-card-expanded">
              <div className="metric-card-watermark">
                <ShieldCheckIcon size={90} color="#16a34a" />
              </div>
              <div className="metric-header">
                <div className="metric-title-group">
                  <div className="metric-icon-wrap">
                    <ShieldCheckIcon size={20} color="#16a34a" />
                  </div>
                  <span className="metric-label">{language === 'te' ? 'పంట ఆరోగ్య సూచిక' : 'Crop Health Score'}</span>
                </div>
                <span className={`trend-badge ${telemetry?.crop_health?.has_scanned ? 'positive' : 'neutral'}`}>
                  {telemetry?.crop_health?.has_scanned ? '94 / 100' : 'Pending Scan'}
                </span>
              </div>
              <div className="metric-value-row">
                {telemetry?.crop_health?.has_scanned ? (
                  <span className="metric-number">94<span className="metric-unit">/ 100</span></span>
                ) : (
                  <span className="metric-number" style={{ fontSize: '18px', color: 'var(--text-muted)' }}>
                    {language === 'te' ? 'స్కాన్ పెంజండి' : 'No Scan Yet'}
                  </span>
                )}
              </div>
              <div className="metric-subtext">
                {telemetry?.crop_health?.subtext || 'Upload a crop photo to get your health score'}
              </div>
              <div className="progress-bar-bg">
                <div 
                  className="progress-bar-fill" 
                  style={{ 
                    width: telemetry?.crop_health?.has_scanned ? '94%' : '0%', 
                    backgroundColor: 'var(--status-green-dot)' 
                  }}
                ></div>
              </div>
              
              {telemetry?.crop_health?.has_scanned ? (
                <div className="source-attribution-tag">
                  {telemetry?.crop_health?.source} • {telemetry?.crop_health?.updated}
                </div>
              ) : (
                <button className="scan-now-card-btn" onClick={() => scrollToSection('tools')}>
                  📷 {language === 'te' ? 'పంట ఫోటోను స్కాన్ చేయండి' : 'Scan Leaf Photo Now'}
                </button>
              )}
            </div>
          </div>
        </section>

        {/* SECTION 3: MARKET INSIGHTS & 30-DAY FORECAST */}
        <section id="market" className="site-section market-section">
          <div className="section-header">
            <h2 className="section-title">
              📈 {language === 'te' 
                ? `${getCropTeluguName(activeField?.crop)} మార్కెట్ ధరలు & 30-రోజుల అంచనా` 
                : `${getCropDisplayName(activeField?.crop)} Market Insights & 30-Day Forecast`}
            </h2>
            <p className="section-subtitle">
              {language === 'te'
                ? `${telemetry?.market_rate?.mandi_town || 'మండీ'} లైవ్ మార్కెట్ ధరలు మరియు PyTorch LSTM AI మోడల్ ధరల అంచనా ప్రొజెక్షన్`
                : `Real-time Agmarknet mandi feeds for ${telemetry?.market_rate?.mandi_town ? `${telemetry.market_rate.mandi_town} Mandi` : 'Nearest Mandi'} combined with PyTorch LSTM deep-learning trajectory projections.`}
            </p>
          </div>

          <div className="market-container-card">
            <div className="market-chart-header">
              <div className="market-chart-title">
                <span>📊</span> 30-Day {getCropDisplayName(activeField?.crop)} Price Trajectory (Agmarknet LSTM Projection)
              </div>
              <div className="market-header-actions">
                <button 
                  className="ask-ai-context-btn" 
                  onClick={() => openChatWithQuery(language === 'te' ? `ప్రస్తుత ${getCropTeluguName(activeField?.crop)} ధరలు మరియు అమ్మకానికి అనుకూల సమయం గురించి చెప్పండి?` : `Tell me more about current ${getCropDisplayName(activeField?.crop).toLowerCase()} prices and the best selling window?`)}
                >
                  💬 {language === 'te' ? 'ధరల గురించి AI ని అడగండి' : 'Ask AI About Prices'}
                </button>
                <span className="trend-badge positive">AI Projection Mode</span>
              </div>
            </div>

            <div className="market-svg-wrapper">
              <svg className="svg-chart-large" viewBox="0 0 700 180">
                <defs>
                  <linearGradient id="marketGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="var(--primary)" stopOpacity="0.35"/>
                    <stop offset="100%" stopColor="var(--primary)" stopOpacity="0.01"/>
                  </linearGradient>
                </defs>
                <line x1="0" y1="30" x2="700" y2="30" className="chart-axis" />
                <line x1="0" y1="90" x2="700" y2="90" className="chart-axis" />
                <line x1="0" y1="150" x2="700" y2="150" className="chart-axis" />

                <polygon points="0,150 0,120 120,110 240,100 360,75 480,35 600,50 700,30 700,150" fill="url(#marketGradient)" />
                <path d="M0,120 Q120,110 240,100 T480,35 T700,30" className="chart-line" strokeWidth="3.5" />

                <circle cx="0" cy="120" r="5" className="chart-point" />
                <circle cx="240" cy="100" r="5" className="chart-point" />
                <circle cx="480" cy="35" r="6.5" className="chart-point" />
                <circle cx="700" cy="30" r="5" className="chart-point" />

                <text x="380" y="24" fill="var(--primary)" fontSize="13" fontWeight="800">
                  {language === 'te' ? 'అంచనా గరిష్టం: ₹2,620 (18వ రోజు)' : 'Projected Peak: ₹2,620 (Day 18)'}
                </text>
              </svg>
            </div>

            <div className="market-stats-banner">
              <div className="m-stat-box">
                <span className="m-stat-lbl">{language === 'te' ? `${telemetry?.market_rate?.mandi_town || 'మండీ'} లైవ్ ధర` : `${telemetry?.market_rate?.mandi_town || 'Current Mandi'} Live Price`}</span>
                <span className="m-stat-val">₹{telemetry?.market_rate?.price || 2450} / Qtl</span>
              </div>
              <div className="m-stat-box">
                <span className="m-stat-lbl">{language === 'te' ? 'అంచనా గరిష్ట ధర' : 'Projected Peak'}</span>
                <span className="m-stat-val" style={{ color: 'var(--accent)' }}>₹2,620 / Qtl (+6.9%)</span>
              </div>
              <div className="m-stat-box">
                <span className="m-stat-lbl">{language === 'te' ? 'అమ్మకానికి అనుకూల సమయం' : 'Selling Window'}</span>
                <span className="m-stat-val">Aug 12 – Aug 18</span>
              </div>
              <div className="m-stat-box">
                <span className="m-stat-lbl">{language === 'te' ? 'డేటా ఆధారము' : 'Data Attribution'}</span>
                <span className="m-stat-val">Agmarknet Govt Data</span>
              </div>
            </div>
          </div>
        </section>

        {/* SECTION 4: AI FARM ASSISTANT SHOWCASE */}
        <section id="assistant" className="site-section assistant-section">
          <div className="section-header">
            <h2 className="section-title">
              🤖 {language === 'te' ? 'AI వ్యవసాయ నిపుణుడు & స్వయంప్రతిపత్తి చాట్‌బాట్' : 'Autonomous AI Agronomist Intelligence Center'}
            </h2>
            <p className="section-subtitle">
              {language === 'te'
                ? 'మీరు స్క్రీన్ పైభాగంలో ఎక్కడ ఉన్నా మాట్లాడండి లేదా ఫైళ్లను అప్‌లోడ్ చేసి క్షణాల్లో పరిష్కారాలు పొందండి'
                : 'Experience persistent voice and text agricultural guidance accessible anywhere on your screen.'}
            </p>
          </div>

          <div className="assistant-showcase-grid">
            <div className="assistant-feature-card">
              <div className="assistant-feature-icon">🎙️</div>
              <h3>{language === 'te' ? 'వాయిస్ & తెలుగు మద్దతు' : 'Multilingual Spoken Agronomist'}</h3>
              <p>
                {language === 'te' 
                  ? 'తెలుగు మరియు ఇంగ్లీషులో మాట్లాడండి. AI నేరుగా శబ్దరూపంలో సమాధానాలు ఇస్తుంది.' 
                  : 'Talk naturally in Telugu or English. Uses gTTS neural speech synthesis for spoken audio advisories.'}
              </p>
            </div>

            <div className="assistant-feature-card">
              <div className="assistant-feature-icon">📁</div>
              <h3>{language === 'te' ? 'మల్టీ-ఫైల్ తెగుళ్ల స్కాన్' : 'Multi-File Document & Media Analysis'}</h3>
              <p>
                {language === 'te'
                  ? 'ఆకు ఫోటోలు (JPG), మట్టి పరీక్ష నివేదికలు (PDF), మరియు పంట వీడియోలను (MP4) అప్‌లోడ్ చేయండి.'
                  : 'Upload crop leaf photos (JPG/PNG), soil lab reports (PDF), or field video clips for instant diagnosis.'}
              </p>
            </div>

            <div className="assistant-feature-card">
              <div className="assistant-feature-icon">⚡</div>
              <h3>{language === 'te' ? 'నిరంతర ఫ్లోటింగ్ చాట్' : 'Persistent Floating Chat Widget'}</h3>
              <p>
                {language === 'te'
                  ? 'స్క్రీన్ కుడి క్రింద భాగాన ఉండే ఫ్లోటింగ్ ఐకాన్ నొక్కి ఎప్పుడైనా చాట్ ప్రారంభించండి.'
                  : 'Click the bottom-right floating widget anytime while browsing the website to open your chat overlay.'}
              </p>
            </div>
          </div>

          <div className="assistant-launch-cta-box">
            <button className="launch-floating-chat-btn" onClick={() => openChatWithQuery('')}>
              💬 {language === 'te' ? 'AI అసిస్టెంట్ చాట్ ప్రారంభించండి' : 'Open Persistent AI Floating Chat Widget'}
            </button>
          </div>
        </section>

        {/* SECTION 5: TOOLS, DIAGNOSTIC SCAN & ADVISORY REPORTS */}
        <section id="tools" className="site-section tools-section">
          <div className="section-header">
            <h2 className="section-title">
              🛠️ {language === 'te' ? 'వ్యవసాయ పరికరాలు & నివేదికలు' : 'Smart Tools & Executive Advisory Reports'}
            </h2>
            <p className="section-subtitle">
              {language === 'te'
                ? 'వాతావరణ ప్రణాళిక, ఆకు తెగుళ్ల స్కాన్, మరియు వారపు PDF నివేదికలు'
                : '7-Day weather planner, YOLOv11 leaf disease scanning, and weekly executive advisory downloads.'}
            </p>
          </div>

          <div className="tools-grid-three">
            {/* Tool Card 1: 7-Day Weather Grid */}
            <div className="tool-card">
              <div className="tool-card-header">
                <span>🌦️</span> {language === 'te' ? '7-రోజుల వాతావరణం (Open-Meteo API)' : '7-Day Local Weather (Open-Meteo API)'}
              </div>
              <div className="weather-forecast-grid-compact">
                {(telemetry?.forecast_7day || []).map((item, idx) => (
                  <div key={idx} className="day-forecast-card">
                    <span className="day-name">{item.day}</span>
                    <span className="weather-icon">{item.icon}</span>
                    <span className="temp-range">{item.temp}</span>
                    <span className="rain-prob">💧 {item.rain}</span>
                  </div>
                ))}
              </div>
              <div className="tool-sub-note">
                💡 {language === 'te' ? 'రాబోయే 48 గంటలు మందుల పిచికారీ నిలిపివేయండి.' : 'Hold off on chemical spraying for 48h to prevent rain wash-off.'}
              </div>
            </div>

            {/* Tool Card 2: Leaf Disease Scan */}
            <div className="tool-card">
              <div className="tool-card-header">
                <span>🔬</span> {language === 'te' ? 'ఆకు తెగుళ్ల స్కాన్ (YOLOv11)' : 'Leaf Disease Scan (YOLOv11)'}
              </div>
              <div className="tool-dropzone" onClick={() => fileInputRef.current?.click()}>
                <div className="tool-upload-icon">📷</div>
                <div className="tool-upload-title">{language === 'te' ? 'ఆకు ఫోటో అప్‌లోడ్ చేయండి' : 'Click to Upload Leaf Photo'}</div>
                <div className="tool-upload-sub">Images, PDFs, Videos (10MB-50MB)</div>
              </div>
              <div className="tool-sub-note">
                🛡️ {language === 'te' ? 'తక్షణమే పురుగుల బెడద మరియు చికిత్స పొందండి.' : 'Get instant disease detection and remedy recommendations.'}
              </div>
            </div>

            {/* Tool Card 3: Advisory PDF Reports */}
            <div className="tool-card">
              <div className="tool-card-header">
                <span>📑</span> {language === 'te' ? 'వారపు నివేదికలు (PDF)' : 'Weekly Advisory Report (PDF)'}
              </div>
              <p className="tool-card-desc">
                {language === 'te'
                  ? 'మీ పొలం నేల వివరాలు, మార్కెట్ ధరలు, మరియు వాతావరణ సలహాలతో కూడిన నివేదికను డౌన్‌లోడ్ చేసుకోండి.'
                  : 'Download an executive PDF summary aggregating your soil telemetry, market price curves, weather alerts, and AI recommendations.'}
              </p>
              <button 
                className="tool-download-btn"
                onClick={() => alert(language === 'te' ? 'వ్యవసాయ నివేదిక PDF డౌన్‌లోడ్ అవుతోంది...' : 'Downloading Weekly Advisory Report PDF...')}
              >
                📥 {language === 'te' ? 'PDF నివేదికను డౌన్‌లోడ్ చేయండి' : 'Download Weekly PDF Summary'}
              </button>
            </div>
          </div>
        </section>

      </main>

      {/* Site Footer */}
      <footer className="site-footer">
        <div className="footer-content-wrap">
          <div className="footer-brand-col">
            <div className="brand-section">
              <div className="brand-icon">🌱</div>
              <div className="brand-title">AgriGen AI</div>
            </div>
            <p className="footer-tagline">
              {language === 'te' 
                ? 'రైతుల కోసం రూపొందించిన డిజిటల్ AI సలహా వేదిక.' 
                : 'Next-generation AI-powered agricultural intelligence for precision farming and sustainable crop yields.'}
            </p>
          </div>

          <div className="footer-links-col">
            <h4>{language === 'te' ? 'త్వరిత లింకులు' : 'Quick Navigation'}</h4>
            <a onClick={() => scrollToSection('hero')}>🏠 {language === 'te' ? 'హోమ్' : 'Home'}</a>
            <a onClick={() => scrollToSection('overview')}>📊 {language === 'te' ? 'ఫార్మ్ ఓవర్‌వ్యూ' : 'Farm Overview'}</a>
            <a onClick={() => scrollToSection('market')}>📈 {language === 'te' ? 'మార్కెట్ అంచనా' : 'Market Forecast'}</a>
            <a onClick={() => scrollToSection('assistant')}>🤖 {language === 'te' ? 'AI అసిస్టెంట్' : 'AI Assistant'}</a>
            <a onClick={() => scrollToSection('tools')}>🛠️ {language === 'te' ? 'పరికరాలు & నివేదికలు' : 'Tools & Reports'}</a>
          </div>

          <div className="footer-info-col">
            <h4>{language === 'te' ? 'సహాయం & చిరునామా' : 'Support & Contact'}</h4>
            <p>📧 tarunkinjangi@gmail.com</p>
            <p>📞 +91 9398733693</p>
            <p>📍 Makkuva - 535547, Parvathipuram Manyam Dist., Andhra Pradesh, India</p>
            <p>⚡ FastAPI • LangGraph • PyTorch • Open-Meteo</p>
          </div>
        </div>

        <div className="footer-bottom-bar">
          <span>© 2026 AgriGen AI Platform. All rights reserved.</span>
          <span>v1.0 Live Multi-Section Edition</span>
        </div>
      </footer>

      {/* ==========================================================================
         FLOATING PERSISTENT CHAT WIDGET (INTERCOM / WHATSAPP STYLE)
         ========================================================================== */}
      
      {/* 1. Floating Action Button (FAB) in Bottom-Right Corner */}
      <button 
        className={`floating-chat-fab ${isChatOpen ? 'expanded' : ''}`} 
        onClick={toggleChatOverlay}
        title={isChatOpen ? "Close AI Agronomist Chat" : "Open AI Agronomist Chat Widget"}
      >
        <div className="fab-icon-wrap">
          {isChatOpen ? '✕' : '🤖'}
        </div>
        <span className="fab-ai-badge">AI</span>
        {unreadBadgeCount > 0 && !isChatOpen && (
          <span className="fab-unread-badge">{unreadBadgeCount}</span>
        )}
      </button>

      {/* 2. Floating Expanded Overlay Panel */}
      <div className={`floating-chat-overlay ${isChatOpen ? 'open' : ''}`}>
        <div className="chat-panel-header">
          <div className="agronomist-profile">
            <div className="avatar-badge">🤖</div>
            <div className="agronomist-info">
              <span className="agronomist-name">
                {language === 'te' ? 'అగ్రిజెన్ AI వాయిస్ నిపుణుడు' : 'AgriGen Voice Agronomist'}
              </span>
              <span className="agronomist-role">
                {language === 'te' ? 'వాయిస్ కమాండ్లు అందుబాటులో ఉన్నాయి 🎙️' : 'Speech-to-Text & Spoken TTS Active 🎙️'}
              </span>
            </div>
          </div>
          
          <div className="chat-header-actions">
            <button 
              className="new-chat-btn"
              onClick={resetChat}
              title={language === 'te' ? 'కొత్త సంభాషణ ప్రారంభించు (చాట్ రీసెట్)' : 'Start New Conversation (Reset Chat)'}
            >
              ➕ {language === 'te' ? 'కొత్త చాట్' : 'New Chat'}
            </button>
            <button 
              className={`voice-autoplay-toggle ${autoPlayVoice ? 'active' : ''}`}
              onClick={() => setAutoPlayVoice(!autoPlayVoice)}
              title="Toggle Auto Spoken Voice Response"
            >
              🔊 {autoPlayVoice ? (language === 'te' ? 'వాయిస్ ఆన్' : 'Voice ON') : (language === 'te' ? 'వాయిస్ ఆఫ్‌' : 'Voice OFF')}
            </button>
            <button 
              className="minimize-chat-btn" 
              onClick={() => setIsChatOpen(false)}
              title="Minimize Chat Widget"
            >
              —
            </button>
          </div>
        </div>

        {/* Prompt Suggestions Chips */}
        <div className="prompt-suggestions-row">
          {language === 'te' ? (
            <>
              <button className="prompt-chip" onClick={() => handleSend('వరి పంటకు వేయాల్సిన ఎరువుల పట్టిక తెలపండి?')}>
                🌾 వరి ఎరువుల పట్టిక
              </button>
              <button className="prompt-chip" onClick={() => handleSend('ప్రస్తుతం వరి మార్కెట్ ధరలు ఎంత ఉన్నాయి?')}>
                📈 మార్కెట్ ధరలు
              </button>
              <button className="prompt-chip" onClick={() => handleSend('ఆకులు పసుపు రంగులోకి మారితే నివారణ ఏంటి?')}>
                🔬 ఆకు మచ్చలు
              </button>
            </>
          ) : (
            <>
              <button className="prompt-chip" onClick={() => handleSend('What is the best fertilizer schedule for Paddy crop?')}>
                🌾 Paddy Fertilizer
              </button>
              <button className="prompt-chip" onClick={() => handleSend('What is the current market price forecast for Paddy?')}>
                📈 Market Rates
              </button>
              <button className="prompt-chip" onClick={() => handleSend('How do I manage yellowing leaf spots?')}>
                🔬 Leaf Spots
              </button>
            </>
          )}
        </div>

        {/* Chat Messages Scroll List */}
        <div className="chat-messages-area-floating">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message-wrapper ${msg.sender} animate-fade-in`}>
              <div className="message-meta">
                {msg.sender === 'user' 
                  ? (language === 'te' ? 'మీరు' : 'You') 
                  : (language === 'te' ? 'అగ్రిజెన్ AI నిపుణుడు' : 'AgriGen Agronomist')} • {msg.time}
              </div>

              <div className="message-bubble">
                {/* Render User Uploaded Attachments Inline */}
                {msg.attachments && msg.attachments.length > 0 && (
                  <div className="message-attachments-grid">
                    {msg.attachments.map((att, aIdx) => (
                      <div key={aIdx} className="inline-attachment-card">
                        {att.category === 'image' && (
                          <img 
                            src={att.previewUrl} 
                            alt={att.name} 
                            className="inline-attachment-img" 
                            onClick={() => setActivePreviewImage(att.previewUrl)}
                          />
                        )}
                        {att.category === 'video' && (
                          <video 
                            src={att.previewUrl} 
                            controls 
                            className="inline-attachment-video" 
                          />
                        )}
                        {att.category === 'pdf' && (
                          <div className="inline-pdf-chip">
                            <span className="pdf-icon">📄</span>
                            <div className="pdf-meta">
                              <span className="pdf-name">{att.name}</span>
                              <span className="pdf-size">{att.size}</span>
                            </div>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}

                <div className="message-bubble-content">
                  <span>
                    {msg.text || (loading && idx === messages.length - 1 ? (
                      <div className="typing-indicator">
                        <span className="typing-dot"></span>
                        <span className="typing-dot"></span>
                        <span className="typing-dot"></span>
                      </div>
                    ) : '')}
                  </span>

                  {/* Speaker Play/Stop Button on AI Messages */}
                  {msg.sender === 'ai' && msg.text && (
                    <button 
                      className={`audio-speak-btn ${currentlyPlayingIdx === idx ? 'playing' : ''}`}
                      onClick={() => speakMessage(msg.text, idx)}
                      title={currentlyPlayingIdx === idx ? "Stop Audio" : "Listen to Voice Response"}
                    >
                      {currentlyPlayingIdx === idx ? '⏹️' : '🔊'}
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
          <div ref={chatEndRef} />
        </div>

        {/* Listening Waveform Indicator Banner */}
        {isListening && (
          <div className="listening-waveform-banner animate-pulse">
            <div className="pulse-wave-dot"></div>
            <div className="pulse-wave-dot"></div>
            <div className="pulse-wave-dot"></div>
            <span className="listening-text">
              🎙️ {language === 'te' ? 'వింటున్నాను... మాట్లాడండి' : 'Listening... Speak naturally'}
            </span>
          </div>
        )}

        {/* Pre-Send Attachment Chips Preview Bar */}
        {attachments.length > 0 && (
          <div className="attachments-preview-bar">
            {attachments.map((att, idx) => (
              <div key={idx} className="attachment-chip-preview">
                {att.category === 'image' && <img src={att.previewUrl} alt={att.name} className="chip-img-thumb" />}
                {att.category === 'pdf' && <span className="chip-icon">📄</span>}
                {att.category === 'video' && <span className="chip-icon">🎥</span>}
                <span className="chip-filename">{att.name}</span>
                <button className="chip-remove-btn" onClick={() => removeAttachment(idx)}>✕</button>
              </div>
            ))}
          </div>
        )}

        {/* Chat Input Bar */}
        <div className="chat-input-container">
          {/* Onboarding Voice Tooltip */}
          <div className="voice-tooltip-banner">
            💡 {language === 'te' ? 'నోటితో అడగడానికి 🎙️ మైక్ బటన్ నొక్కండి' : 'Tap the 🎙️ mic button to ask by voice'}
          </div>

          {/* Hidden Multi-file input */}
          <input 
            type="file" 
            ref={fileInputRef} 
            multiple 
            accept="image/*,video/*,application/pdf"
            capture="environment"
            onChange={handleFileSelect}
            style={{ display: 'none' }}
          />

          <div className="chat-input-wrapper">
            <button 
              className="input-icon-btn attachment-btn" 
              title={language === 'te' ? 'ఫైల్ లేదా ఫోటో అప్‌లోడ్ చేయండి' : 'Attach Photo, PDF, or Video'} 
              onClick={() => fileInputRef.current?.click()}
            >
              📎
            </button>

            {/* Microphone Button (Speech-to-Text) */}
            <button 
              className={`input-icon-btn mic-btn ${isListening ? 'recording' : ''}`}
              onClick={toggleListening}
              title={isListening 
                ? (language === 'te' ? 'రికార్డింగ్ ఆపు' : 'Stop Recording') 
                : (language === 'te' ? 'వాయిస్‌తో అడగండి' : 'Speak Question')}
            >
              🎙️
            </button>

            <input 
              type="text"
              className="chat-input-field"
              placeholder={isListening 
                ? (language === 'te' ? 'వింటున్నాను...' : 'Listening...') 
                : (language === 'te' ? 'వరి సాగు, ఎరువులు, లేదా మాట్లాడండి...' : 'Ask about crops, soil, pests, or speak...')}
              value={inputQuery}
              onChange={(e) => setInputQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={loading}
            />
            <button 
              className="send-submit-btn"
              onClick={() => handleSend()}
              disabled={loading || (!inputQuery.trim() && !attachments.length)}
            >
              {loading ? '...' : (language === 'te' ? 'పంపు' : 'Send')}
            </button>
          </div>
        </div>
      </div>

      {/* Location & Field Picker Modal */}
      <LocationPickerModal 
        isOpen={isLocationModalOpen}
        onClose={() => setIsLocationModalOpen(false)}
        onSaveField={handleSaveField}
        editingField={editingField}
        language={language}
      />
    </div>
  );
}

export default App;
