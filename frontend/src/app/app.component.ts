import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'jugueteria-frontend';
  sidebarCollapsed = true;
  currentRoute = '';
  constructor(private router: Router) { }

  ngOnInit() {
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe((event: any) => {
      this.currentRoute = event.url;
    });
  }
  toggleSidebar() {
    this.sidebarCollapsed = !this.sidebarCollapsed;
  }
  isMobile(): boolean {
    return window.innerWidth <= 991;
  }
  isAuthPage(): boolean {
    return this.currentRoute === '/login' ||
      this.currentRoute === '/register' ||
      this.currentRoute === '/';
  }
  adjustSidebarForDevice(): void {
    if (this.isMobile()) {
      this.sidebarCollapsed = true;
    } else {
      this.sidebarCollapsed = false;
    }
  }
}