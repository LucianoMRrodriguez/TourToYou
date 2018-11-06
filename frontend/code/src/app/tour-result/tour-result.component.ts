import { Component, OnInit, Input } from '@angular/core';
import { TourResult } from './TourResult';

@Component({
  selector: 'app-tour-result',
  templateUrl: './tour-result.component.html',
  styleUrls: ['./tour-result.component.css']
})
export class TourResultComponent implements OnInit {

  @Input() tourResult: TourResult;

  constructor() { }

  ngOnInit() {
  }

}
