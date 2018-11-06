import { TestBed } from '@angular/core/testing';

import { TourSolverService } from './tour-solver.service';

describe('TourSolverService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TourSolverService = TestBed.get(TourSolverService);
    expect(service).toBeTruthy();
  });
});
