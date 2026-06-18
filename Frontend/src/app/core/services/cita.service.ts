import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { Cita } from '../models/cita.model';

@Injectable({ providedIn: 'root' })
export class CitaService {
  private readonly baseUrl = `${environment.apiUrl}/citas`;

  constructor(private http: HttpClient) {}

  listar(doctorId?: number): Observable<Cita[]> {
    if (doctorId) {
      return this.http.get<Cita[]>(this.baseUrl, { params: { doctorId } });
    }
    return this.http.get<Cita[]>(this.baseUrl);
  }

  crear(cita: Cita): Observable<Cita> {
    return this.http.post<Cita>(this.baseUrl, cita);
  }

  eliminar(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
