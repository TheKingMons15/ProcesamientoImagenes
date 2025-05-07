import React, { createContext, useContext, useState, useCallback, ReactNode } from 'react';
import { MapPoint } from '../types/map';

interface MapContextType {
  selectedPoint: MapPoint | null;
  isSliderOpen: boolean;
  openSlider: (point: MapPoint) => void;
  closeSlider: () => void;
}

const MapContext = createContext<MapContextType | null>(null);

export const MapProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [selectedPoint, setSelectedPoint] = useState<MapPoint | null>(null);
  const [isSliderOpen, setIsSliderOpen] = useState(false);

  const openSlider = useCallback((point: MapPoint) => {
    setSelectedPoint(point);
    setIsSliderOpen(true);
  }, []);

  const closeSlider = useCallback(() => {
    setIsSliderOpen(false);
  }, []);

  return (
    <MapContext.Provider value={{ selectedPoint, isSliderOpen, openSlider, closeSlider }}>
      {children}
    </MapContext.Provider>
  );
};

export const useMap = () => {
  const context = useContext(MapContext);
  if (!context) {
    throw new Error('useMap must be used within a MapProvider');
  }
  return context;
};