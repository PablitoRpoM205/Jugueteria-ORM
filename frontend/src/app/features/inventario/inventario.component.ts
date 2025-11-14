import { Component, OnInit } from '@angular/core';
import { InventarioService } from '../../core/services/inventario.service';
import { Inventario } from 'src/app/models/inventario.model';

@Component({
  selector: 'app-inventario',
  templateUrl: './inventario.component.html',
  styleUrls: ['./inventario.component.scss']
})
export class InventarioComponent implements OnInit {
  inventario: Inventario[] = [];
  nuevo: Inventario = {
    id: 0,
    usuario_id: null as any,
    juguete_id: null as any,
    cantidad: null as any
  };
  editando: Inventario | null = null;
  currentPage: number = 1;
  itemsPerPage: number = 5;
  mostrarMensaje = false;
  mensaje = '';
  mensajeExito = true;

  constructor(private inventarioService: InventarioService) { }

  ngOnInit(): void {
    console.log('Iniciando componente de inventario');
    this.cargarInventario();
  }

  get totalPages(): number {
    return Math.ceil(this.inventario.length / this.itemsPerPage);
  }

  get paginatedData() {
    const sortedData = [...this.inventario].sort((a, b) => a.id - b.id);
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

  cargarInventario(): void {
    console.log('Cargando inventario...');
    this.inventarioService.obtenerInventario().subscribe({
      next: (data) => {
        console.log('Inventario recibido:', data);
        this.inventario = data;
        console.log('Total inventario:', this.inventario.length);
        console.log('Total páginas:', this.totalPages);
      },
      error: (error) => {
        console.error('❌ Error al cargar el inventario:', error);
        this.mostrarNotificacion('❌ Error al cargar el inventario', false);
      }
    });
  }

  crear() {
    if (!this.nuevo.usuario_id || !this.nuevo.juguete_id || !this.nuevo.cantidad) {
      this.mostrarNotificacion('⚠️ Por favor completa todos los campos', false);
      return;
    }

    console.log('Datos a enviar:', this.nuevo);

    this.inventarioService.crearInventario(this.nuevo).subscribe({
      next: () => {
        this.cargarInventario();
        this.nuevo = {
          id: 0,
          usuario_id: null as any,
          juguete_id: null as any,
          cantidad: null as any
        };
        this.mostrarNotificacion('✅ Inventario creado correctamente', true);
      },
      error: (err) => {
        console.error('Error al crear inventario:', err);
        const mensajeError = err.error?.detail || 'No se pudo crear el inventario';
        this.mostrarNotificacion(`❌ ${mensajeError}`, false);
      }
    });
  }

  editar(item: Inventario) {
    this.editando = { ...item };
  }

  cerrarModal() {
    this.editando = null;
  }

  actualizar() {
    if (!this.editando || !this.editando.id) return;

    this.inventarioService.actualizarInventario(this.editando.id, this.editando).subscribe({
      next: () => {
        this.cargarInventario();
        this.cerrarModal();
        this.mostrarNotificacion('✅ Inventario actualizado correctamente', true);
      },
      error: (err) => {
        console.error('Error al actualizar inventario:', err);
        this.mostrarNotificacion('❌ No se pudo actualizar el inventario', false);
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