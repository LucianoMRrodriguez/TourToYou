import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TourResult } from './tour-result/TourResult';
import { TourRequest, OnCityFilter } from './tour-filters/TourRequest';

@Injectable({
  providedIn: 'root'
})
export class TourSolverService {

  private tourSolverUrl = 'http://localhost:8000/api/';

  constructor(
    private http: HttpClient) { }

  getTourResult (tourRequest: TourRequest): Observable<TourResult> {
    console.log(tourRequest);
    // const body = new TourRequest();
    // body.src = 'Buenos Aires';
    // body.toVisit = ['Orly', 'Londres', 'Barcelona'];
    // body.vacationDays = 7;
    // body.startDate = new Date(2019, 0, 1);
    // const filter = new OnCityFilter();
    // filter.name = 'Stay in city for at least';
    // filter.cityName = 'Paris';
    // filter.daysToStay = 3;
    // filter.used = false;
    // body.filters = {global: [], ontrip: [], oncity: [filter]};

    return this.http.post<TourResult>(this.tourSolverUrl, tourRequest);
    // return this.http.post<TourResult>(this.tourSolverUrl, body);
  }
}
