import { Doctor } from './doctor.model';
import { Paciente } from './paciente.model';

export type EstadoCita = 'PROGRAMADA' | 'ATENDIDA' | 'CANCELADA';

export interface Cita {
  id?: number;
  pacienteId: number;
  doctorId: number;
  fecha: string;
  motivo: string;
  estado: EstadoCita;
  paciente?: Paciente;
  doctor?: Doctor;
}
