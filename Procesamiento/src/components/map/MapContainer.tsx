import { useMap } from '../../context/MapContext';
import { MapPoint } from '../../types/map';
import mapImage from '../../assets/campus-map.jpg';

interface MapContainerProps {
  points: MapPoint[];
}

const MapContainer: React.FC<MapContainerProps> = ({ points }) => {
  const { openSlider } = useMap();
  
  const handlePointClick = (point: MapPoint) => {
    openSlider(point);
  };

  return (
    <div className="relative w-full h-screen">
      <img src={mapImage} alt="Mapa del campus" className="w-full h-full object-cover" />
      
      {/* Puntos en el mapa */}
      {points.map((point) => (
        <button
          key={point.id}
          className="absolute w-6 h-6 bg-red-500 rounded-full transform -translate-x-1/2 -translate-y-1/2"
          style={{ 
            left: `${point.coordinates.lng}%`, 
            top: `${point.coordinates.lat}%` 
          }}
          onClick={() => handlePointClick(point)}
        />
      ))}
    </div>
  );
};

export default MapContainer;