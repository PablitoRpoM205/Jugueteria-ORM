export interface Juguete {
    id: number;
    nombre: string;
    precio: number | null;
    stock: number | null;
    tipo: string;
    usuario_id?: number;
}