import { Component, OnInit } from '@angular/core';
import { VentasService } from '../../core/services/ventas.service';
import { Venta } from 'src/app/models/venta.model';

@Component({
  selector: 'app-ventas',
  templateUrl: './ventas.component.html',
  styleUrls: ['./ventas.component.scss']
})
export class VentasComponent implements OnInit {
  ventas: Venta[] = [];
  nueva: Venta = {
    id: 0,
    usuario_id: null as any,
    juguete_id: null as any,
    cantidad: null as any
  };
  editando: Venta | null = null;
  buscarId: number | null = null;
  resultadoBusqueda: any = null;
  currentPage: number = 1;
  itemsPerPage: number = 5;
  mostrarMensaje = false;
  mensaje = '';
  mensajeExito = true;

  constructor(private ventasService: VentasService) { }

  ngOnInit(): void {
    console.log('🔵 Iniciando componente de ventas');
    this.cargarVentas();
  }

  get totalPages(): number {
    return Math.ceil(this.ventas.length / this.itemsPerPage);
  }

  get paginatedData() {
    const sortedData = [...this.ventas].sort((a, b) => a.id - b.id);
    const start = (this.currentPage - 1) * this.itemsPerPage;
    const end = start + this.itemsPerPage;
    return sortedData.slice(start, end);
  }

  goToPage(page: number) {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
    }
  }

  nextPage() {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }

  get pageNumbers(): number[] {
    return Array.from({ length: this.totalPages }, (_, i) => i + 1);
  }

  cargarVentas(): void {
    console.log('🔵 Cargando ventas...');
    this.ventasService.obtenerVentas().subscribe({
      next: (data) => {
        console.log('✅ Ventas recibidas:', data);
        this.ventas = data;
        console.log('Total ventas:', this.ventas.length);
        console.log('Total páginas:', this.totalPages);
      },
      error: (error) => {
        console.error('❌ Error al cargar las ventas:', error);
        this.mostrarNotificacion('❌ Error al cargar las ventas', false);
      }
    });
  }

  crear() {
    if (!this.nueva.juguete_id || !this.nueva.cantidad) {
      this.mostrarNotificacion('⚠️ Por favor completa todos los campos', false);
      return;
    }

    console.log('Datos a enviar:', this.nueva);

    this.ventasService.crearVenta(this.nueva).subscribe({
      next: () => {
        this.cargarVentas();
        this.nueva = {
          id: 0,
          usuario_id: 1,
          juguete_id: null as any,
          cantidad: null as any
        };
        this.mostrarNotificacion('✅ Venta creada correctamente', true);
      },
      error: (err) => {
        console.error('Error al crear venta:', err);
        this.mostrarNotificacion('❌ No se pudo crear la venta', false);
      }
    });
  }

  buscarPorId() {
    if (!this.buscarId) return;
    this.resultadoBusqueda = null;

    const activeElement = document.activeElement as HTMLElement;
    if (activeElement) activeElement.blur();

    this.ventasService.obtenerVentaPorId(this.buscarId).subscribe({
      next: (data) => {
        this.resultadoBusqueda = data;
      },
      error: (err) => {
        console.error(err);
        this.mostrarNotificacion('❌ No se encontró una venta con ese ID', false);
      }
    });
  }

  editar(venta: Venta) {
    this.editando = { ...venta };
  }

  eliminar(id: number) {
    if (confirm('¿Eliminar esta venta?')) {
      this.ventasService.eliminarVenta(id).subscribe({
        next: () => {
          this.cargarVentas();
          this.mostrarNotificacion('✅ Venta eliminada correctamente', true);
        },
        error: (err) => {
          console.error('Error al eliminar:', err);
          this.mostrarNotificacion('❌ No se pudo eliminar la venta', false);
        }
      });
    }
  }

  limpiarBusqueda() {
    this.buscarId = null;
    this.resultadoBusqueda = null;
  }

  cerrarModal() {
    this.editando = null;
  }

  actualizar() {
    if (!this.editando || !this.editando.id) return;

    this.ventasService.actualizarVenta(this.editando.id, this.editando).subscribe({
      next: () => {
        this.cargarVentas();
        this.cerrarModal();
        this.mostrarNotificacion('✅ Venta actualizada correctamente', true);
      },
      error: (err) => {
        console.error('Error al actualizar venta:', err);
        this.mostrarNotificacion('❌ No se pudo actualizar la venta', false);
      }
    });
  }

  mostrarNotificacion(mensaje: string, exito: boolean) {
    this.mensaje = mensaje;
    this.mensajeExito = exito;
    this.mostrarMensaje = true;

    setTimeout(() => {
      this.mostrarMensaje = false;
    }, 3000);
  }
}