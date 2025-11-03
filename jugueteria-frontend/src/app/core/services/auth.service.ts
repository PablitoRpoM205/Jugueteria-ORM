export class AuthService {
  private apiUrl = 'http://localhost:8000/auth'; // URL de la API de autenticación

  constructor(private http: HttpClient) {}

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
}