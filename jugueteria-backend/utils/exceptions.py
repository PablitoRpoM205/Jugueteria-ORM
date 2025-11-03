from fastapi import HTTPException, status


class UsuarioNoEncontrado(HTTPException):
    def __init__(self, usuario_id: int = None):
        detail = (
            f"Usuario {usuario_id} no encontrado"
            if usuario_id
            else "Usuario no encontrado"
        )
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class JugueteNoEncontrado(HTTPException):
    def __init__(self, juguete_id: int = None):
        detail = (
            f"Juguete {juguete_id} no encontrado"
            if juguete_id
            else "Juguete no encontrado"
        )
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class VentaNoEncontrada(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada"
        )


class InventarioNoEncontrado(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="Inventario no encontrado"
        )


class UsuarioYaExiste(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT, detail="El correo ya está registrado"
        )


class CredencialesInvalidas(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas"
        )


class UsuarioTieneRelaciones(HTTPException):
    def __init__(self, relacion: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede eliminar el usuario porque tiene {relacion} asociados",
        )


class JugueteTieneRelaciones(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar el juguete porque está en el inventario",
        )


class StockInsuficiente(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Stock insuficiente para realizar la venta",
        )
