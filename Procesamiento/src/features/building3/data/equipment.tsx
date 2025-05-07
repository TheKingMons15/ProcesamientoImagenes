import { FaDesktop, FaChalkboardTeacher, FaBookOpen } from 'react-icons/fa'
import { Equipment } from '../../../types/equipment'

export const equipmentItems: Equipment[] = [
  {
    nombre: "Laboratorio de Computación",
    icono: <FaDesktop className="text-2xl text-blue-500" />, // cambié FaComputer por FaDesktop
    imagen: "/img/lab-computacion.jpg",
    descripcion: "Laboratorio equipado con 30 computadoras de última generación con software especializado para el desarrollo de proyectos académicos y de investigación."
  },
  {
    nombre: "Aula de Nivelación",
    icono: <FaChalkboardTeacher className="text-2xl text-green-500" />,
    imagen: "/img/aula-nivelacion.jpg",
    descripcion: "Espacios diseñados para clases de nivelación académica, equipados con pizarras interactivas y sistema de sonido para una experiencia educativa completa."
  },
  {
    nombre: "Centro Académico",
    icono: <FaBookOpen className="text-2xl text-amber-500" />,
    imagen: "/img/centro-academico.jpg",
    descripcion: "Área dedicada a actividades académicas complementarias, con espacios para tutorías, asesorías y desarrollo de proyectos colaborativos."
  }
]
