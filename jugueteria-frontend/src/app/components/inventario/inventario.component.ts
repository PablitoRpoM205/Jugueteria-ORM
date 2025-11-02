export class InventarioComponent {
  inventario: any[] = [];

  constructor(private inventarioService: InventarioService) {}

  ngOnInit(): void {
    this.cargarInventario();
  }

  cargarInventario(): void {
    this.inventarioService.obtenerInventario().subscribe(
      (data) => {
        this.inventario = data;
      },
      (error) => {
        console.error('Error al cargar el inventario', error);
      }
    );
  }

  actualizarInventario(item: any): void {
    this.inventarioService.actualizarInventario(item).subscribe(
      () => {
        this.cargarInventario();
      },
      (error) => {
        console.error('Error al actualizar el inventario', error);
      }
    );
  }

  eliminarInventario(itemId: number): void {
    this.inventarioService.eliminarInventario(itemId).subscribe(
      () => {
        this.cargarInventario();
      },
      (error) => {
        console.error('Error al eliminar el inventario', error);
      }
    );
  }
}