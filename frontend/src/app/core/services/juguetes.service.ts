import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Juguete } from '../../models/juguete.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class JuguetesService {
  private apiUrl = `${environment.apiUrl}/juguetes`;

  constructor(private http: HttpClient) { }

  obtenerJuguetes(): Observable<Juguete[]> {
    return this.http.get<Juguete[]>(this.apiUrl);
  }

  obtenerJuguetePorId(id: number): Observable<Juguete> {
    return this.http.get<Juguete>(`${this.apiUrl}/${id}`);
  }

  crearJuguete(juguete: Juguete): Observable<Juguete> {
    return this.http.post<Juguete>(this.apiUrl, juguete);
  }

  actualizarJuguete(id: number, juguete: Juguete): Observable<Juguete> {
    return this.http.put<Juguete>(`${this.apiUrl}/${id}`, juguete);
  }

  eliminarJuguete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}