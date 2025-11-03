import { Component, OnInit } from '@angular/core';
import { VentasService } from 'src/app/core/services/ventas.service';
import { Venta } from 'src/app/models/venta.model';

@Component({
  selector: 'app-ventas',
  templateUrl: './ventas.component.html',
  styleUrls: ['./ventas.component.scss']
})
export class VentasComponent implements OnInit {
  ventas: Venta[] = [];

  constructor(private ventasService: VentasService) {}

  ngOnInit(): void {
    this.loadVentas();
  }

  loadVentas(): void {
    this.ventasService.getVentas().subscribe(
      (data: Venta[]) => {
        this.ventas = data;
      },
      (error) => {
        console.error('Error al cargar las ventas', error);
      }
    );
  }

  deleteVenta(id: number): void {
    this.ventasService.deleteVenta(id).subscribe(
      () => {
        this.ventas = this.ventas.filter(venta => venta.id !== id);
      },
      (error) => {
        console.error('Error al eliminar la venta', error);
      }
    );
  }
}