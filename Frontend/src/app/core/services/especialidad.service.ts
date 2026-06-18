import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Especialidad } from '../models/especialidad.model';

@Injectable({ providedIn: 'root' })
export class EspecialidadService {
  private readonly baseUrl = `${environment.apiUrl}/especialidades`;

  constructor(private http: HttpClient) {}

  listar(): Observable<Especialidad[]> {
    return this.http.get<Especialidad[]>(this.baseUrl);
  }

  crear(especialidad: Especialidad): Observable<Especialidad> {
    return this.http.post<Especialidad>(this.baseUrl, especialidad);
  }
}
