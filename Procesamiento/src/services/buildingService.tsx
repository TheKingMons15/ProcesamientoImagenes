const buildings: Building[] = [
    {
      id: 'building3',
      name: 'Edificio 3',
      description: 'Edificio dedicado a nivelación académica y centros de estudio especializados.',
      groupId: 1,
      points: building3Points
    },
    // Aquí irían los demás edificios
  ];
  
  export const getBuildingData = (buildingId: string): Building | undefined => {
    return buildings.find(building => building.id === buildingId);
  };
  
  export const getAllPoints = () => {
    return buildings.flatMap(building => building.points);
  };