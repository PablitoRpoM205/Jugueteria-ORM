import { Component, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/core/services/usuarios.service';
import { Usuario } from 'src/app/models/usuario.model';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.scss']
})
export class UsuariosComponent implements OnInit {
  usuarios: Usuario[] = [];

  constructor(private usuariosService: UsuariosService) {}

  ngOnInit(): void {
    this.cargarUsuarios();
  }

  cargarUsuarios(): void {
    this.usuariosService.obtenerUsuarios().subscribe(
      (data: Usuario[]) => {
        this.usuarios = data;
      },
      (error) => {
        console.error('Error al cargar usuarios', error);
      }
    );
  }

  eliminarUsuario(id: number): void {
    this.usuariosService.eliminarUsuario(id).subscribe(
      () => {
        this.usuarios = this.usuarios.filter(usuario => usuario.id !== id);
      },
      (error) => {
        console.error('Error al eliminar usuario', error);
      }
    );
  }
}