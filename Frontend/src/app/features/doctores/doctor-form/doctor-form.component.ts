import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { DoctorService } from '../../../core/services/doctor.service';
import { EspecialidadService } from '../../../core/services/especialidad.service';
import { Especialidad } from '../../../core/models/especialidad.model';

@Component({
  selector: 'app-doctor-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  templateUrl: './doctor-form.component.html',
  styleUrl: './doctor-form.component.scss'
})
export class DoctorFormComponent implements OnInit {
  doctorId: number | null = null;
  especialidades: Especialidad[] = [];
  guardando = false;

  form = this.fb.group({
    nombres: ['', Validators.required],
    apellidos: ['', Validators.required],
    documento: ['', Validators.required],
    telefono: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    especialidad_id: [null as number | null, Validators.required]
  });

  constructor(
    private fb: FormBuilder,
    private doctorService: DoctorService,
    private especialidadService: EspecialidadService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.especialidadService.listar().subscribe((data) => (this.especialidades = data));

    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.doctorId = Number(id);
      this.doctorService.obtener(this.doctorId).subscribe((doctor) => {
        this.form.patchValue(doctor);
      });
    }
  }

  guardar(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    const valor = this.form.getRawValue();
    const payload = { ...valor, especialidad_id: Number(valor.especialidad_id) };
    this.guardando = true;

    const peticion = this.doctorId
      ? this.doctorService.actualizar(this.doctorId, payload as any)
      : this.doctorService.crear(payload as any);

    peticion.subscribe({
      next: () => this.router.navigate(['/doctores']),
      error: () => (this.guardando = false)
    });
  }
}
