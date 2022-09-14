import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {

  model:any = {};
  constructor(
    private authService: AuthService,
    private route: Router
  ) { }

  ngOnInit(): void {
  }

  user_register(){
    this.authService.register(this.model).subscribe(
      res =>{
        console.log(res);
        console.log('Successfully!')
      },
      err => {
        console.log("something is wrong!!");
      }
    )

  }

}
