import { Component, OnInit, Input } from '@angular/core';
import { Tour } from '../tour-result/TourResult';

@Component({
  selector: 'app-tour-trips-list',
  templateUrl: './tour-trips-list.component.html',
  styleUrls: ['./tour-trips-list.component.css']
})

export class TourTripsListComponent implements OnInit {

  @Input() cardTitle: string;
  @Input() tour: Tour;
  constructor() { }

  ngOnInit() {
  }

}
