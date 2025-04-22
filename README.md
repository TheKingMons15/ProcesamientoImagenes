# Universidad Map Viewer

Aplicación Python de visualización interactiva para edificios universitarios usando imágenes de drones. Permite seleccionar edificios para mostrar información detallada sobre carreras, aulas y servicios.

🎯 Características

- **Visualización de imágenes aéreas** de drones de instalaciones universitarias
- **Segmentación inteligente** de edificios para interacción
- **Modales informativos** con datos detallados de cada edificio:
  - Carreras disponibles
  - Número de aulas
  - Cantidad de pisos
  - Servicios adicionales
- **Interfaz moderna** con colores institucionales y diseño atractivo

## 🛠️ Tecnologías

- Python 3.8+
- CustomTkinter (para UI moderna)
- OpenCV (procesamiento de imágenes)
- Pillow/PIL (manipulación de imágenes)
- SQLite (almacenamiento de datos)

## 🎨 Paleta de colores

- **Principal**: Verde `#4CAF50`
- **Secundarios**: Blanco, Amarillo
- **Acentos**: Derivados del color principal

## 🚀 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/universidad-map-viewer.git
cd universidad-map-viewer
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```bash
python src/main.py
```

## 📋 Gestión del proyecto

Este proyecto se está desarrollando utilizando la metodología **Scrum**:

- **Sprints**: Duración de 2 semanas
- **Daily Standups**: Actualizaciones diarias
- **Sprint Reviews**: Al final de cada ciclo
- **Product Backlog**: Disponible en la sección de Issues

## 📊 Estructura del proyecto

```
universidad-map-viewer/
├── src/
│   ├── main.py                 # Punto de entrada
│   ├── ui/                     # Componentes de interfaz
│   ├── processors/             # Procesamiento de imágenes
│   ├── data/                   # Gestión de datos
│   └── assets/                 # Recursos gráficos
├── data/
│   ├── buildings.db            # Base de datos SQLite
│   └── images/                 # Imágenes de drones
├── docs/                       # Documentación
├── tests/                      # Pruebas unitarias
├── requirements.txt            # Dependencias
└── README.md                   # Este archivo
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes.

## 📜 Licencia

