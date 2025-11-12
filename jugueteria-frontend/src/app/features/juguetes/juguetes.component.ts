import { Component } from '@angular/core';
import { JuguetesService } from '../../core/services/juguetes.service';
import { Juguete } from 'src/app/models/juguete.model';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-juguetes',
  templateUrl: './juguetes.component.html',
  styleUrls: ['./juguetes.component.scss']
})

export class JuguetesComponent {
  juguetes: Juguete[] = [];
  nuevo: Juguete = { id: 0, nombre: '', precio: null, stock: null, tipo: '', usuario_id: 1 };
  editando: Juguete | null = null;
  buscarId: number | null = null;
  resultadoBusqueda: any = null;
  currentPage: number = 1;
  itemsPerPage: number = 5;
  mostrarMensaje = false;
  mensaje = '';
  mensajeExito = true;
  constructor(private juguetesService: JuguetesService) { }

  ngOnInit(): void {
    console.log('Data:', this.juguetes);
    console.log('Total items:', this.juguetes.length);
    console.log('Paginated data:', this.paginatedData);

    this.cargarJuguetes();
  }
  cargarJuguetes(): void {
    this.juguetesService.obtenerJuguetes().subscribe(
      (data) => {
        this.juguetes = data;
      },
      (error) => {
        console.error('Error al cargar los juguetes', error);
      }

    );
  }

  crear() {
    if (!this.nuevo.nombre || !this.nuevo.precio || !this.nuevo.stock || !this.nuevo.tipo) {
      alert('⚠️ Por favor completa todos los campos');
      return;
    }

    console.log('Datos enviados:', this.nuevo);

    this.juguetesService.crearJuguete(this.nuevo).subscribe({
      next: () => {
        this.cargarJuguetes();
        this.nuevo = { id: 0, nombre: '', precio: null, stock: null, tipo: '', usuario_id: 1 };
        alert('✅ Juguete creado correctamente');
      },
      error: (err) => {
        console.error('Error al crear juguete:', err);
        alert('❌ No se pudo crear el juguete');
      }
    });
  }

  buscarPorId() {
    if (!this.buscarId) return;
    this.resultadoBusqueda = null;

    const activeElement = document.activeElement as HTMLElement;
    if (activeElement) activeElement.blur();

    this.juguetesService.obtenerJuguetePorId(this.buscarId).subscribe({
      next: (data) => {
        this.resultadoBusqueda = data;
      },
      error: (err) => {
        console.error(err);
        alert('No se encontró un juguete con ese ID');
      },
    });
  }
  get totalPages() {
    return Math.ceil(this.juguetes.length / this.itemsPerPage);
  }

  get paginatedData() {
    const sortedData = [...this.juguetes].sort((a, b) => a.id - b.id);
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

  onItemsPerPageChange() {
    this.currentPage = 1;
  }

  get pageNumbers(): number[] {
    return Array.from({ length: this.totalPages }, (_, i) => i + 1);
  }



  editar(juguete: Juguete) {
    this.editando = { ...juguete };
  }

  guardar() {
    if (!this.editando) return;
    this.juguetesService.actualizarJuguete(this.editando.id, this.editando).subscribe(() => {
      this.cargarJuguetes();
      this.editando = null;
    });
  }

  eliminar(id: number) {
    if (confirm('¿Eliminar este juguete?')) {
      this.juguetesService.eliminarJuguete(id).subscribe(() => this.cargarJuguetes());
    }
  }
  limpiarBusqueda() {
    this.buscarId = null;
    this.resultadoBusqueda = null;
    this.cargarJuguetes();
  }
  cerrarModal() {
    this.editando = null;
  }

  actualizar() {
    if (!this.editando || !this.editando.id) return;

    this.juguetesService.actualizarJuguete(this.editando.id, this.editando).subscribe({
      next: () => {
        alert('✅ Juguete actualizado correctamente');
        this.cargarJuguetes();
        this.cerrarModal();
      },
      error: (err) => {
        console.error('Error al actualizar juguete:', err);
        alert('❌ No se pudo actualizar el juguete');
      },
    });
  }

}