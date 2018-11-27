import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { TourSolverService } from '../tour-solver.service';
import { TourResult } from '../tour-result/TourResult';
import { tap } from 'rxjs/operators';
import { TourRequest, OnCityFilter, GlobalFilter, OnTripFilter } from './TourRequest';

@Component({
  selector: 'app-tour-filters',
  templateUrl: './tour-filters.component.html',
  styleUrls: ['./tour-filters.component.css']
})
export class TourFiltersComponent implements OnInit {

  @Output() search: EventEmitter<TourResult> = new EventEmitter<TourResult>();
  tourRequest: TourRequest = new TourRequest();
  citiesFilters = {};
  globalFilters = [];
  connections = [];
  maxDuration = '';
  constructor(
    private tourSolverService: TourSolverService
  ) { }

  ngOnInit() {
    this.addPlace();
    // this.tourRequest.src = 'Buenos Aires'
    // this.tourRequest.toVisit = ['Paris','Barcelona','Londres']
    // this.tourRequest.vacationDays = 7
    // this.tourRequest.startDate = new Date(2019,0,1)
    // this.citiesFilters = {0: [new OnCityFilter('Stay in city for at least', 'Paris', 3)], 
    //   1: [],
    //   2: []}
  }

  buscar() {
    this.tourRequest.filters['oncity'] = []
    for (let i = 0; i < this.tourRequest.toVisit.length; i++) {
      for (const cityFilter of this.citiesFilters[i]) {
        cityFilter.cityName = this.tourRequest.toVisit[i];
        this.tourRequest.filters['oncity'].push(cityFilter);
      }
    }

    this.tourRequest.filters['global'] = []
    for (const globalFilter of this.globalFilters) {
      if (globalFilter.name === 'Duration') {
        const time = this.maxDuration.split(':')
        globalFilter.max = parseInt(time[0])*60*60+parseInt(time[1])*60+parseInt(time[2])
      }
      this.tourRequest.filters['global'].push(globalFilter);
    }

    this.tourRequest.filters['ontrip'] = []
    for (const ontripFilter of this.connections) {
      this.tourRequest.filters['ontrip'].push(ontripFilter);
    }
    this.tourSolverService.getTourResult(this.tourRequest)
      .pipe(
        tap(tour => console.log(tour))
      )
      .subscribe(tour => this.search.emit(tour));
  }

  addPlace() {
    this.tourRequest.toVisit.push('');
    this.citiesFilters[this.tourRequest.toVisit.length - 1] = [];
  }

  addStayAtLeastFilter(index: number) {
    this.citiesFilters[index].push(new OnCityFilter('Stay in city for at least', null, null));
  }

  addGlobalFilter(name: string) {
    this.globalFilters.push(new GlobalFilter(name, null))
  }

  addConnection() {
    this.connections.push(new OnTripFilter('Connection', null, null, null))
  }
  trackByFn(index: any, item: any) {
    return index;
  }
}
