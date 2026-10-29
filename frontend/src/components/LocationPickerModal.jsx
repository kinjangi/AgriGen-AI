import { useState, useEffect, useRef } from 'react';

export default function LocationPickerModal({ isOpen, onClose, onSaveField, editingField = null, language = 'en' }) {
  const [activeTab, setActiveTab] = useState('search'); // 'gps', 'search', 'map'
  const [fieldName, setFieldName] = useState('Field #1');
  const [crop, setCrop] = useState('paddy');
  const [sensorId, setSensorId] = useState('');

  const [locationName, setLocationName] = useState('Warangal, Telangana');
  const [district, setDistrict] = useState('Warangal');
  const [state, setState] = useState('Telangana');
  const [lat, setLat] = useState(17.9784);
  const [lon, setLon] = useState(79.5941);

  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [gpsLoading, setGpsLoading] = useState(false);
  const [gpsError, setGpsError] = useState(null);

  const mapRef = useRef(null);
  const leafletMap = useRef(null);
  const markerRef = useRef(null);

  // Initialize or populate form on modal open
  useEffect(() => {
    if (editingField) {
      setFieldName(editingField.name || 'Field #1');
      setCrop(editingField.crop || 'paddy');
      setSensorId(editingField.sensorId || '');
      setLocationName(editingField.locationName || 'Warangal, Telangana');
      setDistrict(editingField.district || 'Warangal');
      setState(editingField.state || 'Telangana');
      setLat(editingField.lat || 17.9784);
      setLon(editingField.lon || 79.5941);
    } else {
      setFieldName(`Field #${Math.floor(Math.random() * 89) + 10}`);
      setCrop('paddy');
      setSensorId('');
    }
  }, [editingField, isOpen]);

  // Initial load of district search suggestions
  useEffect(() => {
    if (isOpen && activeTab === 'search') {
      handleSearch('Telangana');
    }
  }, [isOpen, activeTab]);

  // Leaflet Map Initialization for Pin-Drop Tab
  useEffect(() => {
    if (isOpen && activeTab === 'map' && mapRef.current) {
      if (window.L && !leafletMap.current) {
        const L = window.L;
        const initialMap = L.map(mapRef.current).setView([lat, lon], 12);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; OpenStreetMap contributors'
        }).addTo(initialMap);

        const initialMarker = L.marker([lat, lon], { draggable: true }).addTo(initialMap);

        const updateCoords = (newLat, newLon) => {
          const roundedLat = parseFloat(newLat.toFixed(4));
          const roundedLon = parseFloat(newLon.toFixed(4));
          setLat(roundedLat);
          setLon(roundedLon);

          // Reverse geocode new pin location
          fetch(`https://agrigen-ai.onrender.com/api/v1/telemetry/reverse_geocode?lat=${roundedLat}&lon=${roundedLon}`)
            .then(res => res.json())
            .then(data => {
              if (data) {
                setLocationName(data.name || `${roundedLat}, ${roundedLon}`);
                setDistrict(data.district || 'Agricultural Field');
                setState(data.state || 'India');
              }
            })
            .catch(err => console.warn('Map reverse geocode error:', err));
        };

        initialMarker.on('dragend', (e) => {
          const pos = e.target.getLatLng();
          updateCoords(pos.lat, pos.lng);
        });

        initialMap.on('click', (e) => {
          initialMarker.setLatLng(e.latlng);
          updateCoords(e.latlng.lat, e.latlng.lng);
        });

        leafletMap.current = initialMap;
        markerRef.current = initialMarker;
      } else if (leafletMap.current) {
        leafletMap.current.setView([lat, lon], 12);
        if (markerRef.current) markerRef.current.setLatLng([lat, lon]);
      }
    }

    return () => {
      if (!isOpen && leafletMap.current) {
        leafletMap.current.remove();
        leafletMap.current = null;
      }
    };
  }, [isOpen, activeTab, lat, lon]);

  // Handle Location Search
  const handleSearch = (query) => {
    setSearchQuery(query);
    setIsSearching(true);
    fetch(`https://agrigen-ai.onrender.com/api/v1/telemetry/search_location?query=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => {
        setSearchResults(Array.isArray(data) ? data : []);
      })
      .catch(err => console.error('Search error:', err))
      .finally(() => setIsSearching(false));
  };

  // Select Search Item
  const handleSelectLocation = (item) => {
    setLocationName(`${item.name}, ${item.state}`);
    setDistrict(item.district || item.name);
    setState(item.state || 'India');
    setLat(item.lat);
    setLon(item.lon);

    if (leafletMap.current && markerRef.current) {
      leafletMap.current.setView([item.lat, item.lon], 12);
      markerRef.current.setLatLng([item.lat, item.lon]);
    }
  };

  // GPS Detect My Location
  const handleDetectGPS = () => {
    if (!navigator.geolocation) {
      setGpsError(language === 'te' ? 'మీ బ్రౌజర్‌లో GPS మద్దతు లేదు.' : 'Geolocation is not supported by your browser.');
      return;
    }

    setGpsLoading(true);
    setGpsError(null);

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const userLat = parseFloat(position.coords.latitude.toFixed(4));
        const userLon = parseFloat(position.coords.longitude.toFixed(4));
        setLat(userLat);
        setLon(userLon);

        fetch(`https://agrigen-ai.onrender.com/api/v1/telemetry/reverse_geocode?lat=${userLat}&lon=${userLon}`)
          .then(res => res.json())
          .then(data => {
            if (data) {
              setLocationName(data.name || `${userLat}, ${userLon}`);
              setDistrict(data.district || 'My Location');
              setState(data.state || 'India');
            }
          })
          .catch(err => console.error('Reverse geocode error:', err))
          .finally(() => setGpsLoading(false));
      },
      (error) => {
        console.warn('GPS position error:', error);
        setGpsLoading(false);
        setGpsError(
          language === 'te'
            ? 'GPS అనుమతి నిరాకరించబడింది. దయచేసి క్రింద ఉన్న శోధన నుండి మీ జిల్లాను ఎంచుకోండి.'
            : 'GPS permission denied or unavailable. Please select your district/mandal manually below.'
        );
      },
      { timeout: 10000, enableHighAccuracy: true }
    );
  };

  // Save Field
  const handleSubmit = (e) => {
    e.preventDefault();
    const newField = {
      id: editingField?.id || `field_${Date.now()}`,
      name: fieldName || 'Field #1',
      crop: crop || 'paddy',
      locationName: locationName || `${lat}, ${lon}`,
      district: district || 'Agricultural Region',
      state: state || 'India',
      lat: lat,
      lon: lon,
      sensorId: sensorId.trim()
    };
    onSaveField(newField);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="location-modal-overlay">
      <div className="location-modal-card">
        <div className="modal-header">
          <h3>
            📍 {language === 'te' ? 'వ్యవసాయ స్థానం & పంట వివరాలు' : 'Set Farm Location & Crop Profile'}
          </h3>
          <button className="close-modal-btn" onClick={onClose}>✕</button>
        </div>

        {/* Tab Selection */}
        <div className="modal-tabs">
          <button
            className={`modal-tab-btn ${activeTab === 'search' ? 'active' : ''}`}
            onClick={() => setActiveTab('search')}
          >
            🔍 {language === 'te' ? 'జిల్లా / మండలం శోధించండి' : 'Search District/Mandal'}
          </button>
          <button
            className={`modal-tab-btn ${activeTab === 'gps' ? 'active' : ''}`}
            onClick={() => setActiveTab('gps')}
          >
            🎯 {language === 'te' ? 'GPS ద్వారా కనుగొనండి' : 'Detect GPS Location'}
          </button>
          <button
            className={`modal-tab-btn ${activeTab === 'map' ? 'active' : ''}`}
            onClick={() => setActiveTab('map')}
          >
            🗺️ {language === 'te' ? 'మ్యాప్‌లో పాయింట్ గుర్తించండి' : 'Pin Drop on Map'}
          </button>
        </div>

        <div className="modal-tab-content">
          {/* TAB 1: SEARCH DISTRICT */}
          {activeTab === 'search' && (
            <div className="tab-pane">
              <div className="search-box-wrap">
                <input
                  type="text"
                  className="modal-input"
                  placeholder={language === 'te' ? "ఉదా: కొత్తగూడెం, వరంగల్, గుంటూరు..." : "e.g., Kothagudem, Warangal, Guntur, Ludhiana..."}
                  value={searchQuery}
                  onChange={(e) => handleSearch(e.target.value)}
                />
              </div>

              <div className="search-results-list">
                {isSearching ? (
                  <div className="loading-spinner-row">⏳ Searching location database...</div>
                ) : searchResults.length > 0 ? (
                  searchResults.map((item, idx) => (
                    <div
                      key={idx}
                      className={`search-result-item ${item.lat === lat && item.lon === lon ? 'selected' : ''}`}
                      onClick={() => handleSelectLocation(item)}
                    >
                      <span className="location-item-icon">📍</span>
                      <div className="location-item-info">
                        <strong>{item.name}</strong>
                        <small>{item.mandal} • {item.district}, {item.state} ({item.lat}, {item.lon})</small>
                      </div>
                      {item.lat === lat && item.lon === lon && <span className="selected-check">✓ Active</span>}
                    </div>
                  ))
                ) : (
                  <div className="empty-search-msg">No location found matching "{searchQuery}". Try another town or district name.</div>
                )}
              </div>
            </div>
          )}

          {/* TAB 2: GPS DETECT */}
          {activeTab === 'gps' && (
            <div className="tab-pane gps-tab-pane">
              <p className="tab-desc">
                {language === 'te'
                  ? 'మీ పరికరం రన్ అవుతున్న ఖచ్చితమైన GPS అక్షాంశం మరియు రేఖాంశాలను స్వయంచాలకంగా పొందండి.'
                  : 'Automatically fetch real-time latitude & longitude from your mobile device or browser GPS sensor.'}
              </p>

              <button className="gps-detect-btn" onClick={handleDetectGPS} disabled={gpsLoading}>
                {gpsLoading ? '⏳ Fetching Satellite Coordinates...' : '🛰️ Detect My Exact Location'}
              </button>

              {gpsError && <div className="gps-error-box">⚠️ {gpsError}</div>}

              {lat && lon && (
                <div className="detected-coords-card">
                  <div className="coord-row">
                    <span>Selected Location:</span>
                    <strong>{locationName}</strong>
                  </div>
                  <div className="coord-row">
                    <span>Coordinates:</span>
                    <code>Lat: {lat}, Lon: {lon}</code>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* TAB 3: MAP PIN DROP */}
          {activeTab === 'map' && (
            <div className="tab-pane map-tab-pane">
              <p className="tab-desc">
                {language === 'te'
                  ? 'మీ పంట పొలం సరిహద్దు లేదా ఖచ్చితమైన స్థానాన్ని ఎంచుకోవడానికి మ్యాప్‌పై క్లిక్ చేయండి లేదా మార్కర్‌ను జారండి.'
                  : 'Click anywhere on the satellite map or drag the green marker to set your field boundaries.'}
              </p>
              <div id="map-container" ref={mapRef} style={{ width: '100%', height: '220px', borderRadius: '12px' }}></div>
              <div className="map-coords-badge">
                📍 Point Selected: <strong>{locationName}</strong> (Lat: {lat}, Lon: {lon})
              </div>
            </div>
          )}
        </div>

        {/* FIELD CONFIGURATION FORM */}
        <form onSubmit={handleSubmit} className="field-config-form">
          <hr className="modal-divider" />
          <div className="form-grid">
            <div className="form-group">
              <label>{language === 'te' ? 'పొలం పేరు / లేబుల్' : 'Field Label / Name'}</label>
              <input
                type="text"
                className="modal-input"
                value={fieldName}
                onChange={(e) => setFieldName(e.target.value)}
                placeholder="e.g. Field #1 (North Plot)"
                required
              />
            </div>

            <div className="form-group">
              <label>{language === 'te' ? 'ముఖ్యమైన పంట రకం' : 'Primary Crop Cultivated'}</label>
              <select
                className="modal-select"
                value={crop}
                onChange={(e) => setCrop(e.target.value)}
              >
                <option value="paddy">🌾 Paddy / Rice (వరి)</option>
                <option value="cotton">☁️ Cotton (పత్తి)</option>
                <option value="maize">🌽 Maize / Corn (మొక్కజొన్న)</option>
                <option value="chilli">🌶️ Red Chilli (మిర్చి)</option>
                <option value="wheat">🌾 Wheat (గోధుమ)</option>
                <option value="groundnut">🥜 Groundnut (వేరుశనగ)</option>
                <option value="soybean">🌱 Soybean (సోయాబీన్)</option>
              </select>
            </div>
          </div>

          <div className="form-group margin-top-sm">
            <label>
              📡 {language === 'te' ? 'IoT హార్డ్‌వేర్ సెన్సార్ ఐడీ (ఐచ్ఛికం)' : 'Link IoT Physical Sensor Hardware ID (Optional)'}
            </label>
            <input
              type="text"
              className="modal-input"
              value={sensorId}
              onChange={(e) => setSensorId(e.target.value)}
              placeholder="e.g. IOT-SENS-884 (Leave blank for automated Soil Model)"
            />
            <small className="input-hint font-size-xs">
              {sensorId.trim() ? "✓ Physical sensor linked! Dashboard will display real-time IoT hardware telemetry." : "ℹ️ No sensor entered. Dashboard will use location-based SoilGrids model + rainfall calculations."}
            </small>
          </div>

          <div className="modal-footer-actions">
            <button type="button" className="modal-cancel-btn" onClick={onClose}>
              {language === 'te' ? 'రద్దు చేయి' : 'Cancel'}
            </button>
            <button type="submit" className="modal-save-btn">
              💾 {language === 'te' ? 'పొలం స్థానాన్ని సేవ్ చేయి' : 'Save Field Profile'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
