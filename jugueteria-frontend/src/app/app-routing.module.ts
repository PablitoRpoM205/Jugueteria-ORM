import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/auth/login/login.component';
import { UsuariosComponent } from './components/usuarios/usuarios.component';
import { JuguetesComponent } from './components/juguetes/juguetes.component';
import { VentasComponent } from './components/ventas/ventas.component';
import { InventarioComponent } from './components/inventario/inventario.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { AuthGuard } from './core/guards/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'usuarios', component: UsuariosComponent, canActivate: [AuthGuard] },
  { path: 'juguetes', component: JuguetesComponent, canActivate: [AuthGuard] },
  { path: 'ventas', component: VentasComponent, canActivate: [AuthGuard] },
  { path: 'inventario', component: InventarioComponent, canActivate: [AuthGuard] },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }