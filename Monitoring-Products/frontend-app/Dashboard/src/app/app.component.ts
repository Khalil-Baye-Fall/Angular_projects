import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './Authentication/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Dashboard';


  constructor(
    public authService: AuthService,
    private route: Router,
  ){

  }

  user_signOut(){
    this.authService.SignOut();
  }
}
