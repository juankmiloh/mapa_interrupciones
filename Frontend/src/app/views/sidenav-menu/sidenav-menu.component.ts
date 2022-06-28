import { Component, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { Router } from '@angular/router';
import { ISUIError } from 'src/app/models/IOptionsMapa.model';
import { AppObservableService } from 'src/app/services/app-observable.service';
import { SuiService } from 'src/app/services/sui.service';

@Component({
  selector: 'app-sidenav-menu',
  templateUrl: './sidenav-menu.component.html',
  styleUrls: ['./sidenav-menu.component.scss'],
})
export class SidenavMenuComponent {
  myWindow: Window;

  constructor(
    private router: Router,
    private suiService: SuiService,
    public observer: AppObservableService
  ) {}

  @ViewChild('sidenav') sidenav: MatSidenav;

  opcion = 'Mapa de Interrupciones para el Servicio de Energía';
  // opcion = 'Superintendencia Delegada para Energía y Gas - Portal Grupo SUI';

  x: MediaQueryList;
  countVisitas = 0

  async ngOnInit() {
    this.x = window.matchMedia('(max-width: 800px)'); // Si hace match con dispositivos móviles
    this.loadVisitors();
    this.createVisitors();
  }

  createVisitors() {
    this.suiService.setVisita({id_usuario: 1, observacion: "Sin observación"}).subscribe( visitas => {
      // console.log(visitas);
      this.loadVisitors();
    }, (error: ISUIError) => {
      // console.log(error);
      this.observer.setShowAlertErrorSUI(error.status);
    });
  }
  
  loadVisitors() {
    this.suiService.getVisitas().subscribe( visitas => {
      let result: any = visitas;
      // console.log(result);
      this.countVisitas = result.total;
    }, (error: ISUIError) => {
      // console.log(error);
      this.observer.setShowAlertErrorSUI(error.status);
    });
  }

  close(reason: string) {
    if (reason !== 'na') {
      if (reason === 'Mapa de PQR´s' || reason === 'Tarifarito | Grupo Tarifario') {
        this.sidenav.close();
        // this.router.navigateByUrl('/');
        window.close();
        this.opcion = 'Superintendencia Delegada para Energía y Gas - Portal Grupo SUI';
      } else {
        this.opcion = reason;
        this.sidenav.close();
      }
    } else {
      this.sidenav.close();
    }
  }

}
