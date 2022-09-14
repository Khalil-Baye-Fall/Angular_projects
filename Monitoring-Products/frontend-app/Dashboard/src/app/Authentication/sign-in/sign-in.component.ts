import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss']
})
export class SignInComponent implements OnInit {

  model:any = {};
  errorMessage = '';
  data =  {token:'', use_id:'', username:'', email:''};
  username = '';

  constructor(
    private authService: AuthService,
    private route: Router
  ) { }

  ngOnInit(): void {
  }

  user_login(){
    this.authService.login(this.model).subscribe( 
      
      res => {
        this.data  = res;
        this.username = this.data.username;
        this.route.navigate(['/home']);
        console.log(this.username);

        // this.messageService.sendMessage(this.data.username);       

    },
    err => {
      this.errorMessage = 'Oups! Something goes wrong! Please try it again.';
    }
    );
  }


}
