import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TourTripsListComponent } from './tour-trips-list.component';

describe('TourTripsListComponent', () => {
  let component: TourTripsListComponent;
  let fixture: ComponentFixture<TourTripsListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TourTripsListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TourTripsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
