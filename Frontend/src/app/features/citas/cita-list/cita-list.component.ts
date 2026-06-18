import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CitaService } from '../../../core/services/cita.service';
import { Cita } from '../../../core/models/cita.model';

@Component({
  selector: 'app-cita-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './cita-list.component.html',
  styleUrl: './cita-list.component.scss'
})
export class CitaListComponent implements OnInit {
  citas: Cita[] = [];
  cargando = false;
  error = '';
  doctorId: number | null = null;

  constructor(
    private citaService: CitaService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.queryParamMap.subscribe((params) => {
      const doctorId = params.get('doctorId');
      this.doctorId = doctorId ? Number(doctorId) : null;
      this.cargarCitas();
    });
  }

  cargarCitas(): void {
    this.cargando = true;
    this.error = '';
    this.citaService.listar(this.doctorId ?? undefined).subscribe({
      next: (data) => {
        this.citas = data;
        this.cargando = false;
      },
      error: () => {
        this.error = 'No fue posible cargar las citas';
        this.cargando = false;
      }
    });
  }

  eliminar(id?: number): void {
    if (!id) return;
    if (!confirm('¿Eliminar esta cita?')) return;
    this.citaService.eliminar(id).subscribe(() => this.cargarCitas());
  }
}
