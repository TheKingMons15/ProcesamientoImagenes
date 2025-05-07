import React from 'react';
import MapContainer from '../components/map/MapContainer';
import { getAllPoints } from '../services/buildingService';

const MapPage: React.FC = () => {
  const points = getAllPoints();
  
  return (
    <div className="h-screen">
      <MapContainer points={points} />
    </div>
  );
};

export default MapPage;