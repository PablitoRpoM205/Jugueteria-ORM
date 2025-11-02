export class JuguetesComponent {
  juguetes: any[] = [];
  
  constructor(private juguetesService: JuguetesService) {}

  ngOnInit(): void {
    this.loadJuguetes();
  }

  loadJuguetes(): void {
    this.juguetesService.getJuguetes().subscribe(
      (data) => {
        this.juguetes = data;
      },
      (error) => {
        console.error('Error al cargar los juguetes', error);
      }
    );
  }

  // Métodos adicionales para crear, actualizar y eliminar juguetes pueden ser añadidos aquí
}