import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'app';
  constructor(private http: HttpClient){

  }
  onBtnClick(event) {

    this.http.get('/get_data').subscribe((res: Response) => alert(JSON.stringify(res)));
  }
}
