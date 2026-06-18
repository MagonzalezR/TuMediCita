import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { PacienteService } from '../../../core/services/paciente.service';

@Component({
  selector: 'app-paciente-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  templateUrl: './paciente-form.component.html',
  styleUrl: './paciente-form.component.scss'
})
export class PacienteFormComponent implements OnInit {
  pacienteId: number | null = null;
  guardando = false;

  form = this.fb.group({
    nombres: ['', Validators.required],
    apellidos: ['', Validators.required],
    documento: ['', Validators.required],
    fechaNacimiento: ['', Validators.required],
    telefono: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    direccion: ['', Validators.required]
  });

  constructor(
    private fb: FormBuilder,
    private pacienteService: PacienteService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.pacienteId = Number(id);
      this.pacienteService.obtener(this.pacienteId).subscribe((paciente) => {
        this.form.patchValue(paciente);
      });
    }
  }

  guardar(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    const valor = this.form.getRawValue();
    this.guardando = true;

    const peticion = this.pacienteId
      ? this.pacienteService.actualizar(this.pacienteId, valor as any)
      : this.pacienteService.crear(valor as any);

    peticion.subscribe({
      next: () => this.router.navigate(['/pacientes']),
      error: () => (this.guardando = false)
    });
  }
}
