export class TourRequest {

    src: string;
    toVisit: string[];
    vacationDays: number;
    startDate: Date;
    filters: {
        global: GlobalFilter[],
        ontrip: OnTripFilter[],
        oncity: OnCityFilter[]
    };

    constructor() {
        this.src = '';
        this.toVisit = [];
        this.startDate = new Date();
        this.filters = {global: [], ontrip: [], oncity: []};
    }
}

export class GlobalFilter {
    name: string;
    cityName: string;
    daysToStay: number;
    used: boolean;
}

export class OnTripFilter {
    name: string;
    cityName: string;
    daysToStay: number;
    used: boolean;
}

export class OnCityFilter {
    name: string;
    cityName: string;
    daysToStay: number;
    used: boolean;
}
