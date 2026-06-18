import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { CitaService } from '../../../core/services/cita.service';
import { PacienteService } from '../../../core/services/paciente.service';
import { DoctorService } from '../../../core/services/doctor.service';
import { Paciente } from '../../../core/models/paciente.model';
import { Doctor } from '../../../core/models/doctor.model';

@Component({
  selector: 'app-cita-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  templateUrl: './cita-form.component.html',
  styleUrl: './cita-form.component.scss'
})
export class CitaFormComponent implements OnInit {
  pacientes: Paciente[] = [];
  doctores: Doctor[] = [];
  doctorSeleccionado?: Doctor;
  guardando = false;

  form = this.fb.group({
    pacienteId: [null as number | null, Validators.required],
    doctorId: [null as number | null, Validators.required],
    fecha: ['', Validators.required],
    motivo: ['', Validators.required]
  });

  constructor(
    private fb: FormBuilder,
    private citaService: CitaService,
    private pacienteService: PacienteService,
    private doctorService: DoctorService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.pacienteService.listar().subscribe((data) => (this.pacientes = data));
    this.doctorService.listar().subscribe((data) => (this.doctores = data));
  }

  onDoctorChange(): void {
    const doctorId = this.form.value.doctorId;
    this.doctorSeleccionado = this.doctores.find((doctor) => doctor.id === Number(doctorId));
  }

  guardar(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    const valor = this.form.getRawValue();
    this.guardando = true;

    this.citaService
      .crear({
        pacienteId: Number(valor.pacienteId),
        doctorId: Number(valor.doctorId),
        fecha: valor.fecha as string,
        motivo: valor.motivo as string,
        estado: 'PROGRAMADA'
      })
      .subscribe({
        next: () => this.router.navigate(['/citas']),
        error: () => (this.guardando = false)
      });
  }
}
