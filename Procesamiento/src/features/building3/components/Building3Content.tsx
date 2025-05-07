import React from 'react';
import { equipmentItems } from '../data/equipment';

interface Building3ContentProps {
  pointId: string;
}

const Building3Content: React.FC<Building3ContentProps> = ({ pointId }) => {
  // Determinar qué equipamiento mostrar según el punto seleccionado
  let equipmentToShow;
  
  switch (pointId) {
    case 'b3-lab1':
      equipmentToShow = equipmentItems[0];
      break;
    case 'b3-niv1':
      equipmentToShow = equipmentItems[1];
      break;
    case 'b3-ca1':
      equipmentToShow = equipmentItems[2];
      break;
    default:
      equipmentToShow = null;
  }

  if (!equipmentToShow) {
    return <p>No hay información detallada disponible para este punto.</p>;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center space-x-2">
        {equipmentToShow.icono}
        <h3 className="text-lg font-semibold">{equipmentToShow.nombre}</h3>
      </div>
      
      <div className="rounded-lg overflow-hidden">
        <img 
          src={equipmentToShow.imagen} 
          alt={equipmentToShow.nombre}
          className="w-full h-48 object-cover"
        />
      </div>
      
      <p className="text-gray-700">{equipmentToShow.descripcion}</p>
      
      <div className="mt-4 pt-4 border-t border-gray-200">
        <h4 className="font-medium mb-2">Horarios:</h4>
        <ul className="list-disc pl-5 text-sm">
          <li>Lunes a Viernes: 8:00 - 20:00</li>
          <li>Sábados: 9:00 - 14:00</li>
        </ul>
      </div>
      
      <button className="mt-4 w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition-colors">
        Ver más detalles
      </button>
    </div>
  );
};

export default Building3Content;