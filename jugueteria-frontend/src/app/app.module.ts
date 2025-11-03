import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthComponent } from './components/auth/login/login.component';
import { UsuariosComponent } from './components/usuarios/usuarios.component';
import { JuguetesComponent } from './components/juguetes/juguetes.component';
import { VentasComponent } from './components/ventas/ventas.component';
import { InventarioComponent } from './components/inventario/inventario.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    UsuariosComponent,
    JuguetesComponent,
    VentasComponent,
    InventarioComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }