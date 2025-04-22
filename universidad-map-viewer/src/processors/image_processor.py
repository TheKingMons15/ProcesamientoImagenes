import cv2
import numpy as np

class ImageProcessor:
    """Clase para procesar las imágenes de drones"""
    
    def __init__(self):
        self.image = None
        self.original_image = None
        self.segmented_areas = []
    
    def load_image(self, image_path):
        """Carga una imagen desde el disco"""
        self.original_image = cv2.imread(image_path)
        if self.original_image is None:
            raise ValueError(f"No se pudo cargar la imagen desde {image_path}")
        
        self.image = self.original_image.copy()
        return self.convert_to_rgb(self.image)
    
    def convert_to_rgb(self, image):
        """Convierte una imagen BGR a RGB"""
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    def segment_buildings(self, threshold_value=127):
        """Segmenta los edificios en la imagen"""
        if self.image is None:
            raise ValueError("No hay imagen cargada para segmentar")
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
        # Aplicar umbral para segmentar
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        
        # Encontrar contornos
        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        # Filtrar contornos por área
        min_area = 1000  # Ajustar según necesidad
        self.segmented_areas = []
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_area:
                x, y, w, h = cv2.boundingRect(contour)
                self.segmented_areas.append((x, y, x+w, y+h))
        
        return self.segmented_areas
    
    def draw_segmented_areas(self):
        """Dibuja las áreas segmentadas en la imagen"""
        result = self.original_image.copy()
        
        for x1, y1, x2, y2 in self.segmented_areas:
            cv2.rectangle(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        return self.convert_to_rgb(result)
    
    def resize_image(self, width=None, height=None):
        """Redimensiona la imagen manteniendo la proporción"""
        if self.image is None:
            raise ValueError("No hay imagen cargada para redimensionar")
        
        h, w = self.image.shape[:2]
        
        if width and height:
            new_size = (width, height)
        elif width:
            new_size = (width, int(h * width / w))
        elif height:
            new_size = (int(w * height / h), height)
        else:
            return self.image.copy()
        
        return cv2.resize(self.image, new_size)