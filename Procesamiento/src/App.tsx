import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { MapProvider } from './context/MapContext';
import AppRoutes from './router';
import SliderPanel from './components/SliderPanel';

const App: React.FC = () => {
  return (
    <Router>
      <MapProvider>
        <div className="relative">
          <AppRoutes />
          <SliderPanel />
        </div>
      </MapProvider>
    </Router>
  );
};

export default App;