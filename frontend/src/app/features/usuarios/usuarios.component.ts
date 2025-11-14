import { Component, OnInit } from '@angular/core';
import { UsuariosService } from '../../core/services/usuarios.service';
import { Usuario } from 'src/app/models/usuario.model';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.scss']
})
export class UsuariosComponent implements OnInit {
  usuarios: Usuario[] = [];
  nuevo: Usuario = {
    id: 1,
    nombre: '',
    correo: '',
    contrasena: '',
    es_admin: false
  };
  editando: Usuario | null = null;
  buscarId: number | null = null;
  resultadoBusqueda: any = null;
  currentPage: number = 1;
  itemsPerPage: number = 5;
  mostrarMensaje = false;
  mensaje = '';
  mensajeExito = true;

  constructor(private usuariosService: UsuariosService) { }

  ngOnInit(): void {
    console.log('Iniciando componente de usuarios');
    this.cargarUsuarios();
  }

  get totalPages(): number {
    return Math.ceil(this.usuarios.length / this.itemsPerPage);
  }

  get paginatedData() {
    const sortedData = [...this.usuarios].sort((a, b) => a.id - b.id);
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

  cargarUsuarios(): void {
    console.log('Cargando usuarios...');
    this.usuariosService.ObtenerUsuarios().subscribe({
      next: (data) => {
        console.log('Usuarios recibidos:', data);
        this.usuarios = data;
        console.log('Total usuarios:', this.usuarios.length);
        console.log('Total páginas:', this.totalPages);
      },
      error: (error) => {
        console.error('Error al cargar los usuarios:', error);
        this.mostrarNotificacion('❌ Error al cargar los usuarios', false);
      }
    });
  }

  crear() {
    if (!this.nuevo.nombre || !this.nuevo.correo || !this.nuevo.contrasena) {
      this.mostrarNotificacion('⚠️ Por favor completa todos los campos', false);
      return;
    }

    console.log('Datos a enviar:', this.nuevo);

    this.usuariosService.crearUsuario(this.nuevo).subscribe({
      next: () => {
        this.cargarUsuarios();
        this.nuevo = {
          id: 0,
          nombre: '',
          correo: '',
          contrasena: '',
          es_admin: false
        };
        this.mostrarNotificacion('✅ Usuario creado correctamente', true);
      },
      error: (err) => {
        console.error('Error al crear usuario:', err);
        const mensajeError = err.error?.detail || 'No se pudo crear el usuario';
        this.mostrarNotificacion(`❌ ${mensajeError}`, false);
      }
    });
  }

  buscarPorId() {
    if (!this.buscarId) return;
    this.resultadoBusqueda = null;

    const activeElement = document.activeElement as HTMLElement;
    if (activeElement) activeElement.blur();

    this.usuariosService.ObtenerUsuarioPorId(this.buscarId).subscribe({
      next: (data) => {
        this.resultadoBusqueda = data;
      },
      error: (err) => {
        console.error(err);
        this.mostrarNotificacion('❌ No se encontró un usuario con ese ID', false);
      }
    });
  }

  editar(usuario: Usuario) {
    this.editando = { ...usuario, contrasena: '' };
  }

  eliminar(id: number) {
    if (confirm('¿Eliminar este usuario?')) {
      this.usuariosService.eliminarUsuario(id).subscribe({
        next: () => {
          this.cargarUsuarios();
          this.mostrarNotificacion('✅ Usuario eliminado correctamente', true);
        },
        error: (err) => {
          console.error('Error al eliminar:', err);
          this.mostrarNotificacion('❌ No se pudo eliminar el usuario', false);
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

    const datosActualizar: any = {
      nombre: this.editando.nombre,
      correo: this.editando.correo,
      es_admin: this.editando.es_admin
    };

    if (this.editando.contrasena && this.editando.contrasena.trim() !== '') {
      datosActualizar.contrasena = this.editando.contrasena;
    }
    this.usuariosService.actualizarUsuario(this.editando.id, this.editando).subscribe({
      next: () => {
        this.cargarUsuarios();
        this.cerrarModal();
        this.mostrarNotificacion('✅ Usuario actualizado correctamente', true);
      },
      error: (err) => {
        console.error('Error al actualizar usuario:', err);
        this.mostrarNotificacion('❌ No se pudo actualizar el usuario', false);
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