export interface Venta {
    id: number;
    usuarioId: number;
    jugueteId: number;
    cantidad: number;
    fecha: Date;
    total: number;
}