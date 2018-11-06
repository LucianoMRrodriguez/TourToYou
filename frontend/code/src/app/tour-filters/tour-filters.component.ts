import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { TourSolverService } from '../tour-solver.service';
import { TourResult } from '../tour-result/TourResult';
import { tap } from 'rxjs/operators';
import { TourRequest } from './TourRequest';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-tour-filters',
  templateUrl: './tour-filters.component.html',
  styleUrls: ['./tour-filters.component.css']
})
export class TourFiltersComponent implements OnInit {

  @Output() search: EventEmitter<TourResult> = new EventEmitter<TourResult>();
  tourRequest: TourRequest = new TourRequest();
  date: FormControl;

  constructor(
    private tourSolverService: TourSolverService
  ) { }

  ngOnInit() {
    this.date = new FormControl(new Date());
    this.addPlace();
  }

  buscar() {
    console.log(this.date);
    this.tourSolverService.getTourResult(this.tourRequest)
      .pipe(
        tap(tour => console.log(tour))
      )
      .subscribe(tour => this.search.emit(tour));
  }

  addPlace() {
    this.tourRequest.toVisit.push('');
  }
}
