export interface MapPoint {
    id: string;
    buildingId: string;  // Identificador del edificio
    name: string;
    coordinates: {
      lat: number;
      lng: number;
    };
    type: 'classroom' | 'lab' | 'office' | 'common' | 'sports';
  }
  
  export interface Building {
    id: string;
    name: string;
    description: string;
    groupId: number; // Grupo responsable
    points: MapPoint[];
  }