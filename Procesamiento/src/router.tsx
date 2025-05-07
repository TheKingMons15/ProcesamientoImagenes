import React from 'react';
import { Routes, Route } from 'react-router-dom';
import MapPage from './pages/MapPage';
import Building3Page from './features/building3/pages/Building3Page';
// Importar las demás páginas específicas

const AppRoutes: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<MapPage />} />
      <Route path="/building3/*" element={<Building3Page />} />
      {/* Rutas para los demás edificios */}
    </Routes>
  );
};

export default AppRoutes;