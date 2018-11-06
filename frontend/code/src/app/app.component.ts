import { Component } from '@angular/core';
import { TourResult } from './tour-result/TourResult';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'TourToYou';
  tourResult: TourResult = undefined;

  onSearch(tourResult: TourResult) {
    this.tourResult = tourResult;
  }
}
