import { Inventario } from '../../models/inventario.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class InventarioService {
    private apiUrl = 'http://localhost:8000/inventario';

    constructor(private http: HttpClient) { }
    obtenerInventario(): Observable<Inventario[]> {
        return this.http.get<Inventario[]>(this.apiUrl);
    }
    crearInventario(inventario: Inventario): Observable<Inventario> {
        return this.http.post<Inventario>(this.apiUrl, inventario);
    }

    actualizarInventario(id: number, inventario: Inventario): Observable<Inventario> {
        return this.http.put<Inventario>(`${this.apiUrl}/${id}`, inventario);
    }

}