import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignInComponent } from './Authentication/sign-in/sign-in.component';
import { RegistrationComponent } from './Authentication/registration/registration.component';
import { ProductsComponent } from './Dahsboard/products/products.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AuthService } from './Authentication/auth.service';


const routes: Routes = [
  {path:'', component:ProductsComponent},
  {path:'home', component:ProductsComponent},
  {path:'login', component:SignInComponent },
  {path: 'registration', component:RegistrationComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    RegistrationComponent,
    ProductsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
  ],
  providers: [
    AuthService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
