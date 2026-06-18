import { Especialidad } from './especialidad.model';

export interface Doctor {
  id?: number;
  nombres: string;
  apellidos: string;
  documento: string;
  telefono: string;
  email: string;
  especialidadId: number;
  especialidad?: Especialidad;
}
