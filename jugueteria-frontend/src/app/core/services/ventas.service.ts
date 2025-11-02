import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Venta } from '../../models/venta.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class VentasService {
  private apiUrl = `${environment.apiUrl}/ventas`;

  constructor(private http: HttpClient) { }

  crearVenta(venta: Venta): Observable<Venta> {
    return this.http.post<Venta>(this.apiUrl, venta);
  }

  obtenerVentas(): Observable<Venta[]> {
    return this.http.get<Venta[]>(this.apiUrl);
  }

  obtenerVentaPorId(id: number): Observable<Venta> {
    return this.http.get<Venta>(`${this.apiUrl}/${id}`);
  }

  actualizarVenta(id: number, venta: Venta): Observable<Venta> {
    return this.http.put<Venta>(`${this.apiUrl}/${id}`, venta);
  }

  eliminarVenta(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}