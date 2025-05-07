import { MapPoint } from '../../../types/map';

export const building3Points: MapPoint[] = [
  {
    id: 'b3-lab1',
    buildingId: 'building3',
    name: 'Laboratorio de Computación 1',
    coordinates: {
      lat: 45.2, // Estos valores son aproximados y deberían ajustarse
      lng: 32.5  // según la imagen real del mapa
    },
    type: 'lab'
  },
  {
    id: 'b3-niv1',
    buildingId: 'building3',
    name: 'Aula de Nivelación A',
    coordinates: {
      lat: 46.1,
      lng: 33.8
    },
    type: 'classroom'
  },
  {
    id: 'b3-ca1',
    buildingId: 'building3',
    name: 'Centro Académico Principal',
    coordinates: {
      lat: 47.3,
      lng: 34.6
    },
    type: 'office'
  }
];