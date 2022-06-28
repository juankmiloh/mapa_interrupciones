import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap} from 'rxjs/operators';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root',
})
export class SuiService {

  constructor(public http: HttpClient) { }

  serverUrl = environment.serverUrl;


  verifyConnectionSUI() {
    return new Promise((resolve, reject) => {
      this.http.get<any[]>(`${this.serverUrl}/i_anios`).toPromise().then(res => {
        resolve(res);
      }, (error) => {
        resolve(error);
      });
    });
  }

  getVisitas(): Observable<any[]> {
    return this.http.get<any[]>(`${this.serverUrl}/visitas`).pipe(
      tap((data) => {
        // console.log(data);
      }), catchError(this.handleError),
      );
  }

  setVisita(model: any): Observable<any[]> {
    return this.http.post<any[]>(`${this.serverUrl}/visitas`, model).pipe(
      tap((data) => {
        // console.log('DATA desde service -> ', JSON.stringify(data))
      }),
      catchError(this.handleError)
    );
  }

  getAnios(): Observable<any[]> {
    return this.http.get<any[]>(`${this.serverUrl}/i_anios`).pipe(
      tap((data) => {
        // console.log(data);
      }), catchError(this.handleError),
      );
  }

  getCausas(): Observable<any[]> {
    return this.http.get<any[]>(`${this.serverUrl}/i_causas`).pipe(
      tap((data) => {
        // console.log('Carga causas exitosa!');
      }), catchError(this.handleError),
    );
  }

  getCausaId(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.serverUrl}/i_causas/${id}`).pipe(
      tap((data) => {
        // console.log(JSON.stringify(data));
      }), catchError(this.handleError),
    );
  }

  getEmpresas(): Observable<any[]> {
    return this.http.get<any[]>(`${this.serverUrl}/i_empresas`).pipe(
      tap((data) => {
        // console.log('Carga empresas exitosa!');
      }), catchError(this.handleError),
    );
  }

  getEmpresasId(id: number) {
    return new Promise((resolve, reject) => {
      this.http.get<any[]>(`${this.serverUrl}/i_empresas/${id}`).toPromise().then(res => {
        resolve(res);
      }, (error) => {
        catchError(this.handleError);
      });
    });
  }

  // Capturamos el estado del error y el mensaje
  private handleError(err: HttpErrorResponse) {
    const error = {
      status: err.status,
      message: err.message,
    };
    return throwError(error);
  }

}
