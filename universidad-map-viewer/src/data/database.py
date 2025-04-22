import sqlite3
import os

class BuildingDatabase:
    """Clase para gestionar la base de datos de edificios"""
    
    def __init__(self, db_path):
        """Inicializa la conexión a la base de datos"""
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        """Establece la conexión a la base de datos"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Crea las tablas necesarias si no existen"""
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
    
    def add_building(self, name, careers, classrooms, floors, description, x1, y1, x2, y2):
        """Añade un nuevo edificio a la base de datos"""
        self.cursor.execute('''
            INSERT INTO buildings (name, careers, classrooms, floors, description, x1, y1, x2, y2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, careers, classrooms, floors, description, x1, y1, x2, y2))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_building_at_point(self, x, y):
        """Obtiene el edificio que contiene el punto (x, y)"""
        self.cursor.execute('''
            SELECT id, name, careers, classrooms, floors, description 
            FROM buildings 
            WHERE x1 <= ? AND x2 >= ? AND y1 <= ? AND y2 >= ?
        ''', (x, x, y, y))
        return self.cursor.fetchone()
    
    def get_all_buildings(self):
        """Obtiene todos los edificios de la base de datos"""
        self.cursor.execute('SELECT * FROM buildings')
        return self.cursor.fetchall()
    
    def update_building(self, building_id, name, careers, classrooms, floors, description, x1, y1, x2, y2):
        """Actualiza la información de un edificio"""
        self.cursor.execute('''
            UPDATE buildings
            SET name = ?, careers = ?, classrooms = ?, floors = ?, description = ?,
                x1 = ?, y1 = ?, x2 = ?, y2 = ?
            WHERE id = ?
        ''', (name, careers, classrooms, floors, description, x1, y1, x2, y2, building_id))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_building(self, building_id):
        """Elimina un edificio de la base de datos"""
        self.cursor.execute('DELETE FROM buildings WHERE id = ?', (building_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.conn:
            self.conn.close()