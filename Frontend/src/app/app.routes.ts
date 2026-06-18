import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'pacientes', pathMatch: 'full' },
  {
    path: 'pacientes',
    loadComponent: () =>
      import('./features/pacientes/paciente-list/paciente-list.component').then(
        (m) => m.PacienteListComponent
      )
  },
  {
    path: 'pacientes/nuevo',
    loadComponent: () =>
      import('./features/pacientes/paciente-form/paciente-form.component').then(
        (m) => m.PacienteFormComponent
      )
  },
  {
    path: 'pacientes/:id/editar',
    loadComponent: () =>
      import('./features/pacientes/paciente-form/paciente-form.component').then(
        (m) => m.PacienteFormComponent
      )
  },
  {
    path: 'doctores',
    loadComponent: () =>
      import('./features/doctores/doctor-list/doctor-list.component').then(
        (m) => m.DoctorListComponent
      )
  },
  {
    path: 'doctores/nuevo',
    loadComponent: () =>
      import('./features/doctores/doctor-form/doctor-form.component').then(
        (m) => m.DoctorFormComponent
      )
  },
  {
    path: 'doctores/:id/editar',
    loadComponent: () =>
      import('./features/doctores/doctor-form/doctor-form.component').then(
        (m) => m.DoctorFormComponent
      )
  },
  {
    path: 'citas',
    loadComponent: () =>
      import('./features/citas/cita-list/cita-list.component').then(
        (m) => m.CitaListComponent
      )
  },
  {
    path: 'citas/nueva',
    loadComponent: () =>
      import('./features/citas/cita-form/cita-form.component').then(
        (m) => m.CitaFormComponent
      )
  },
  { path: '**', redirectTo: 'pacientes' }
];
