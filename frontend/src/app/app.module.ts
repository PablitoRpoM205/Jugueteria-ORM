import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AuthInterceptor } from './core/interceptors/auth.interceptor';
import { LoginComponent } from './features/auth/login/login/login.component';
import { RegisterComponent } from './features/auth/login/register/register.component';
import { UsuariosComponent } from './features/usuarios/usuarios.component';
import { JuguetesComponent } from './features/juguetes/juguetes.component';
import { VentasComponent } from './features/ventas/ventas.component';
import { InventarioComponent } from './features/inventario/inventario.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { SidebarComponent } from './shared/sidebar/sidebar.component';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    SidebarComponent,
    AppComponent,
    LoginComponent,
    UsuariosComponent,
    JuguetesComponent,
    VentasComponent,
    InventarioComponent,
    DashboardComponent,
    RegisterComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
