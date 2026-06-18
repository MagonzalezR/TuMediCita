import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { PacienteService } from '../../../core/services/paciente.service';
import { Paciente } from '../../../core/models/paciente.model';

@Component({
  selector: 'app-paciente-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './paciente-list.component.html',
  styleUrl: './paciente-list.component.scss'
})
export class PacienteListComponent implements OnInit {
  pacientes: Paciente[] = [];
  cargando = false;
  error = '';

  constructor(private pacienteService: PacienteService) {}

  ngOnInit(): void {
    this.cargarPacientes();
  }

  cargarPacientes(): void {
    this.cargando = true;
    this.error = '';
    this.pacienteService.listar().subscribe({
      next: (data) => {
        this.pacientes = data;
        this.cargando = false;
      },
      error: () => {
        this.error = 'No fue posible cargar los pacientes';
        this.cargando = false;
      }
    });
  }

  eliminar(id?: number): void {
    if (!id) return;
    if (!confirm('¿Eliminar este paciente?')) return;
    this.pacienteService.eliminar(id).subscribe(() => this.cargarPacientes());
  }
}
