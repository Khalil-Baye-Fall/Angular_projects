import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { map } from 'rxjs/operators';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  base_url = "http://127.0.0.1:8000/dashapp/";
  private readonly CAH_USERNAME = 'username';

  constructor(
    private http: HttpClient,
    private route: Router,
    ) { }


  login(model:any){
    return this.http.post(this.base_url + 'login/auth/token/', model, httpOptions).pipe(
      map((response: any) => {
        const user = response;
        if (user && user.token) {   
          localStorage.setItem('token', user.token); 
          localStorage.setItem('username', user.username);         
        }
        return user;
        
      })
    );
  }

  register(model:any){
    // const requestOptions: Object = {
    //   responseType: 'application/json'
    // };
    return this.http.post(this.base_url + 'register/', model);
  }

  loggedIn(){
    return !!localStorage.getItem('token');
  }

  
  SignOut(){
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    this.route.navigate(['/home']);
    window.location.reload();
    return false;

  }


  getAuthHeaders(): HttpHeaders{
    let headers = new HttpHeaders();
    headers = headers.append('Authorization', `Token ${localStorage.getItem('token')}`);
    headers = headers.append('Content-Type', 'application/json');
    return headers;
  }
}
