import customtkinter as ctk
import cv2
import sqlite3
from PIL import Image, ImageTk
import os
import sys

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')

# Asegurar que existen los directorios
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Configuración de CustomTkinter
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue, green, dark-blue

class UniversidadMapApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Universidad Map Viewer")
        self.geometry("1200x800")
        
        # Paleta de colores
        self.color_principal = "#4CAF50"  # Verde
        self.color_secundario = "#FFFFFF"  # Blanco
        self.color_acento = "#FFD700"  # Amarillo
        
        # Inicializar base de datos
        self.init_database()
        
        # Crear interfaz
        self.create_ui()
        
        # Intentar cargar una imagen de demostración
        self.load_default_image()
        
    def init_database(self):
        """Inicializa la conexión a la base de datos SQLite"""
        db_path = os.path.join(DATA_DIR, "buildings.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # Crear tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS buildings (
                id INTEGER PRIMARY KEY,
                name TEXT,
                careers TEXT,
                classrooms INTEGER,
                floors INTEGER,
                description TEXT,
                x1 INTEGER, y1 INTEGER, x2 INTEGER, y2 INTEGER
            )
        ''')
        self.conn.commit()
        
        # Agregar algunos datos de ejemplo si la tabla está vacía
        self.cursor.execute("SELECT COUNT(*) FROM buildings")
        count = self.cursor.fetchone()[0]
        
        if count == 0:
            # Insertar datos de ejemplo
            self.cursor.execute('''
                INSERT INTO buildings (name, careers, classrooms, floors, description, x1, y1, x2, y2)
                VALUES 
                ("Edificio A", "Ingeniería en Sistemas, Informática", 20, 4, "Edificio principal de la facultad de ingeniería", 100, 100, 300, 250),
                ("Edificio B", "Arquitectura, Diseño", 15, 3, "Facultad de diseño y arquitectura", 350, 120, 500, 280),
                ("Biblioteca", "Todas las carreras", 5, 2, "Biblioteca central con salas de estudio", 150, 300, 280, 450)
            ''')
            self.conn.commit()
        
    def create_ui(self):
        """Crea la interfaz de usuario"""
        # Frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frame para la imagen
        self.image_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.image_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Label para la imagen
        self.image_label = ctk.CTkLabel(self.image_frame, text="")
        self.image_label.pack(fill="both", expand=True)
        self.image_label.bind("<Button-1>", self.on_image_click)
        
        # Frame para controles
        self.control_frame = ctk.CTkFrame(self.main_frame, width=200, corner_radius=10)
        self.control_frame.pack(side="right", fill="y", padx=10, pady=10)
        
        # Botones de control
        self.btn_load_image = ctk.CTkButton(
            self.control_frame, 
            text="Cargar Imagen", 
            fg_color=self.color_principal,
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=self.load_image_dialog
        )
        self.btn_load_image.pack(pady=10, padx=10, fill="x")
        
        self.btn_zoom_in = ctk.CTkButton(
            self.control_frame, 
            text="Zoom +", 
            fg_color=self.color_principal,
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=self.zoom_in
        )
        self.btn_zoom_in.pack(pady=10, padx=10, fill="x")
        
        self.btn_zoom_out = ctk.CTkButton(
            self.control_frame, 
            text="Zoom -", 
            fg_color=self.color_principal,
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=self.zoom_out
        )
        self.btn_zoom_out.pack(pady=10, padx=10, fill="x")
        
        self.btn_add_building = ctk.CTkButton(
            self.control_frame, 
            text="Añadir Edificio", 
            fg_color=self.color_principal,
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=self.add_building_dialog
        )
        self.btn_add_building.pack(pady=10, padx=10, fill="x")
        
        # Información
        self.info_label = ctk.CTkLabel(
            self.control_frame,
            text="Haz clic en un edificio\npara ver su información",
            font=ctk.CTkFont(size=12),
            justify="center"
        )
        self.info_label.pack(pady=20, padx=10)
        
        # Factor de zoom
        self.zoom_factor = 1.0
        
    def load_default_image(self):
        """Carga una imagen por defecto o crea una en blanco"""
        # Crear una imagen en blanco como demo
        width, height = 800, 600
        blank_image = Image.new('RGB', (width, height), color=(240, 240, 240))
        
        # Convertir a formato OpenCV para procesamiento
        self.original_image = cv2.cvtColor(
            cv2.resize(
                cv2.cvtColor(
                    numpy.array(blank_image), 
                    cv2.COLOR_RGB2BGR
                ), 
                (width, height)
            ), 
            cv2.COLOR_BGR2RGB
        )
        self.display_image = self.original_image.copy()
        self.update_image()
        
    def load_image_dialog(self):
        """Abre un diálogo para seleccionar una imagen"""
        file_path = ctk.filedialog.askopenfilename(
            title="Seleccionar imagen de dron",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png")]
        )
        
        if file_path:
            self.load_drone_image(file_path)
            
    def load_drone_image(self, image_path):
        """Carga la imagen del dron"""
        if os.path.exists(image_path):
            self.original_image = cv2.imread(image_path)
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            self.display_image = self.original_image.copy()
            self.update_image()
        else:
            print(f"Error: No se encuentra la imagen en {image_path}")
    
    def update_image(self):
        """Actualiza la imagen mostrada"""
        if hasattr(self, 'display_image'):
            image = Image.fromarray(self.display_image)
            self.tk_image = ImageTk.PhotoImage(image=image)
            self.image_label.configure(image=self.tk_image)
    
    def on_image_click(self, event):
        """Maneja los clics en la imagen"""
        x, y = event.x, event.y
        # Ajustar coordenadas según el zoom
        x_adjusted = int(x / self.zoom_factor)
        y_adjusted = int(y / self.zoom_factor)
        
        # Buscar si se hizo clic en un edificio
        self.cursor.execute('''
            SELECT id, name, careers, classrooms, floors, description 
            FROM buildings 
            WHERE x1 <= ? AND x2 >= ? AND y1 <= ? AND y2 >= ?
        ''', (x_adjusted, x_adjusted, y_adjusted, y_adjusted))
        
        building = self.cursor.fetchone()
        if building:
            self.show_building_info(building)
    
    def show_building_info(self, building):
        """Muestra un modal con la información del edificio"""
        # Crear ventana modal
        modal = ctk.CTkToplevel(self)
        modal.title(f"Edificio: {building[1]}")
        modal.geometry("500x400")
        modal.attributes("-topmost", True)
        
        # Contenido del modal
        frame = ctk.CTkFrame(modal, corner_radius=10)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title = ctk.CTkLabel(
            frame, 
            text=building[1], 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=10)
        
        # Información del edificio
        info_text = f"""
        🎓 Carreras: {building[2]}
        🚪 Aulas: {building[3]}
        🏢 Pisos: {building[4]}
        
        📝 Descripción:
        {building[5]}
        """
        
        info = ctk.CTkLabel(
            frame, 
            text=info_text, 
            font=ctk.CTkFont(size=14),
            justify="left"
        )
        info.pack(pady=20)
        
        # Botón para cerrar
        close_btn = ctk.CTkButton(
            frame, 
            text="Cerrar", 
            fg_color=self.color_principal, 
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=modal.destroy
        )
        close_btn.pack(pady=10)
    
    def add_building_dialog(self):
        """Abre un diálogo para añadir un nuevo edificio"""
        # Implementación pendiente
        pass
    
    def zoom_in(self):
        """Acerca la imagen"""
        if hasattr(self, 'original_image'):
            self.zoom_factor *= 1.2
            height, width = self.original_image.shape[:2]
            new_height, new_width = int(height * self.zoom_factor), int(width * self.zoom_factor)
            self.display_image = cv2.resize(self.original_image, (new_width, new_height))
            self.update_image()
    
    def zoom_out(self):
        """Aleja la imagen"""
        if hasattr(self, 'original_image'):
            self.zoom_factor /= 1.2
            height, width = self.original_image.shape[:2]
            new_height, new_width = int(height * self.zoom_factor), int(width * self.zoom_factor)
            self.display_image = cv2.resize(self.original_image, (new_width, new_height))
            self.update_image()
    
    def darken_color(self, hex_color, factor=0.8):
        """Oscurece un color hexadecimal por un factor"""
        # Convertir hex a RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Oscurecer
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        
        # Convertir de vuelta a hex
        return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    # Verificar si numpy está instalado
    try:
        import numpy
    except ImportError:
        print("Error: Numpy no está instalado. Instalando...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
        import numpy
    
    app = UniversidadMapApp()
    app.mainloop()