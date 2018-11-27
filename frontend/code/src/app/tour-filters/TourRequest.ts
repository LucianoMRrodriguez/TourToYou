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
    max: number;

    constructor(name?: string, max?: number) {
        this.name = name;
        this.max = max;
    }
}

export class OnTripFilter {
    name: string;
    fromPlace: string;
    toPort: string;
    toCity: string;
    used: boolean;

    constructor(name?: string, fromPlace?: string, toPort?:string, toCity?:string) {
        this.name = name;
        this.fromPlace = fromPlace;
        this.toPort = toPort;
        this.toCity = toCity;
        this.used = false;
    }
}

export class OnCityFilter {
    name: string;
    cityName: string;
    daysToStay: number;
    used: boolean;

    constructor(name?: string, cityName?: string, daysToStay?: number) {
        this.name = name;
        this.cityName = cityName;
        this.daysToStay = daysToStay;
        this.used = false;
    }
}
