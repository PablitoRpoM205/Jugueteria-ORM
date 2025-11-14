import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Router, RouterModule, NavigationEnd } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';
import { filter } from 'rxjs/operators';


declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
    roles?: string[];
}

export const ROUTES: RouteInfo[] = [
    { path: '/dashboard', title: 'Dashboard', icon: 'fas fa-home', class: '' },
    { path: '/juguetes', title: 'Juguetes', icon: 'fas fa-gamepad', class: '' },
    { path: '/usuarios', title: 'Usuarios', icon: 'fa fa-users', class: '' },
    { path: '/inventario', title: 'Inventario', icon: 'fas fa-box', class: '' },
    { path: '/ventas', title: 'Ventas', icon: 'fas fa-shopping-cart', class: '' },
];

@Component({
    selector: 'app-sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
    @Input() collapsed = false;
    @Output() sidebarClosed = new EventEmitter<void>();
    sidebarCollapsed = false;
    menuItems: RouteInfo[] = [];
    currentUser: any = null;

    constructor(
        public authService: AuthService,
        private router: Router
    ) { }

    ngOnInit() {
        this.authService.currentUser$.subscribe(user => {
            this.currentUser = user;
        });

        this.menuItems = ROUTES;
        this.router.events.pipe(
            filter(event => event instanceof NavigationEnd)
        ).subscribe(() => {
            if (this.isMobileMenu()) {
                this.closeSidebar();
            }
        });

        console.log('Menu items cargados:', this.menuItems);

    }
    isMobileMenu() {
        return window.innerWidth <= 991;
    }
    toggleSidebar() {
        this.sidebarCollapsed = !this.sidebarCollapsed;
    }
    closeSidebar() {
        this.sidebarClosed.emit();
    }

    logout() {
        this.authService.logout();
        this.router.navigate(['/auth/login']);
    }

}
