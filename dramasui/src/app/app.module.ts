import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {HeaderMenuComponent} from './header-menu/header-menu.component';
import {SectionMenuComponent} from './section-menu/section-menu.component';
import {SliderComponent} from './slider/slider.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderMenuComponent,
    SectionMenuComponent,
    SliderComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
