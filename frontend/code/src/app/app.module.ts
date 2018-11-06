import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms';
import { MatDatepickerModule } from '@angular/material/datepicker';

import { AppComponent } from './app.component';
import { TourResultComponent } from './tour-result/tour-result.component';
import { TourFiltersComponent } from './tour-filters/tour-filters.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TourTripsListComponent } from './tour-trips-list/tour-trips-list.component';

@NgModule({
  declarations: [
    AppComponent,
    TourResultComponent,
    TourFiltersComponent,
    TourTripsListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatCardModule,
    BrowserAnimationsModule,
    MatButtonModule,
    FormsModule,
    MatDatepickerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
