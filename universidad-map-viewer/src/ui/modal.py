import customtkinter as ctk

class InfoModal:
    """Clase para crear ventanas modales informativas"""
    
    def __init__(self, parent, title, color_principal):
        self.parent = parent
        self.color_principal = color_principal
        
        # Crear ventana modal
        self.modal = ctk.CTkToplevel(parent)
        self.modal.title(title)
        self.modal.geometry("500x400")
        self.modal.attributes("-topmost", True)
        
        # Contenido del modal
        self.frame = ctk.CTkFrame(self.modal, corner_radius=10)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    def add_title(self, text):
        """Añade un título al modal"""
        title = ctk.CTkLabel(
            self.frame, 
            text=text, 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=10)
        
    def add_info(self, text):
        """Añade información al modal"""
        info = ctk.CTkLabel(
            self.frame, 
            text=text, 
            font=ctk.CTkFont(size=14),
            justify="left"
        )
        info.pack(pady=20)
    
    def add_close_button(self):
        """Añade un botón para cerrar el modal"""
        close_btn = ctk.CTkButton(
            self.frame, 
            text="Cerrar", 
            fg_color=self.color_principal, 
            hover_color=self.darken_color(self.color_principal),
            corner_radius=10,
            command=self.modal.destroy
        )
        close_btn.pack(pady=10)
    
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