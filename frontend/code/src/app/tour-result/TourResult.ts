export class TourResult {
    cheap: Tour;
    fast: Tour;
    balanced: Tour;
}

export class Tour {
    totalCost: string;
    totalDuration: string;
    path: Trip[];
    error: string;
}

export class Trip {
    id: number;
    fromPort: Port;
    toPort: Port;
    cost: number;
    currency: string;
    departure: Date;
    arrival: Date;
    duration: string;
    scales: number;
    sourceURL: string;
}

export class Port {
    id: number;
    country: string;
    city: string;
    name: string;
}
