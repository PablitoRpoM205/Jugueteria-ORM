import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { Injectable } from '@angular/core';


export interface User {
  id: number;
  nombre: string;
  correo: string;
  contrasena: string;
  rol: string; // Puede ser 'admin' o 'usuario'
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/auth'; // URL de la API de autenticación
  private currentUserSubject: BehaviorSubject<User | null> = new BehaviorSubject<User | null>(null);

  constructor(private http: HttpClient) { }

  login(credentials: { correo: string; contrasena: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials);
  }

  logout(): void {
    // Lógica para cerrar sesión, como eliminar el token del almacenamiento local
    localStorage.removeItem('token');
  }

  isLoggedIn(): boolean {
    // Verifica si el usuario está autenticado
    return !!localStorage.getItem('token');
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  isAuthenticated(): boolean {
    // Lógica para verificar si el usuario está autenticado
    const token = this.getToken();
    return token !== null;
  }

  obtenerRolUsuario(): string | null {
    // Lógica para obtener el rol del usuario desde el token o almacenamiento
    const token = this.getToken();
    if (token) {
      // Decodificar el token y extraer el rol (esto depende de cómo esté estructurado el token)
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload.rol || null;
    }
    return null;
  }
  getCurrentUser(): User | null {
    return this.currentUserSubject.value;
  }
}