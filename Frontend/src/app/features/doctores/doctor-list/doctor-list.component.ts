import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { DoctorService } from '../../../core/services/doctor.service';
import { Doctor } from '../../../core/models/doctor.model';

@Component({
  selector: 'app-doctor-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './doctor-list.component.html',
  styleUrl: './doctor-list.component.scss'
})
export class DoctorListComponent implements OnInit {
  doctores: Doctor[] = [];
  cargando = false;
  error = '';

  constructor(private doctorService: DoctorService) {}

  ngOnInit(): void {
    this.cargarDoctores();
  }

  cargarDoctores(): void {
    this.cargando = true;
    this.error = '';
    this.doctorService.listar().subscribe({
      next: (data) => {
        this.doctores = data;
        this.cargando = false;
      },
      error: () => {
        this.error = 'No fue posible cargar los doctores';
        this.cargando = false;
      }
    });
  }

  eliminar(id?: number): void {
    if (!id) return;
    if (!confirm('¿Eliminar este doctor?')) return;
    this.doctorService.eliminar(id).subscribe(() => this.cargarDoctores());
  }
}
