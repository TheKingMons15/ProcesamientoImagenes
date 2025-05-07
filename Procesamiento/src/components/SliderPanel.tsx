import React from 'react';
import { useMap } from '../context/MapContext';
import { getBuildingData } from '../services/buildingService';b

const SliderPanel: React.FC = () => {
  const { selectedPoint, isSliderOpen, closeSlider } = useMap();
  
  if (!isSliderOpen || !selectedPoint) return null;

  const buildingData = getBuildingData(selectedPoint.buildingId);
  
  return (
    <div 
      className={`fixed top-0 right-0 h-full w-80 bg-white shadow-lg transform transition-transform duration-300 ${
        isSliderOpen ? 'translate-x-0' : 'translate-x-full'
      }`}
    >
      <div className="p-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold">{selectedPoint.name}</h2>
          <button onClick={closeSlider} className="text-gray-500 hover:text-gray-700">
            X
          </button>
        </div>
        
        <div className="mt-4">
          {buildingData ? (
            <div>
              <p className="mb-4">{buildingData.description}</p>
              
              {/* Aquí se renderizaría el componente específico para este edificio */}
              {buildingData.groupId === 1 && <Building3Content pointId={selectedPoint.id} />}
              {buildingData.groupId === 2 && <Building1Content pointId={selectedPoint.id} />}
              {/* ... y así sucesivamente para cada grupo */}
            </div>
          ) : (
            <p>No hay información disponible para este punto.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default SliderPanel;