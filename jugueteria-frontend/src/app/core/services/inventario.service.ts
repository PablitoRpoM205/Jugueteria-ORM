export class InventarioService {
    private apiUrl = 'http://localhost:8000/inventario'; // Cambiar según la URL de la API

    constructor(private http: HttpClient) {}

    getInventario(): Observable<Inventario[]> {
        return this.http.get<Inventario[]>(this.apiUrl);
    }

    actualizarInventario(inventario: Inventario): Observable<Inventario> {
        return this.http.put<Inventario>(`${this.apiUrl}/${inventario.id}`, inventario);
    }
}