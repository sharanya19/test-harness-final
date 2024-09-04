// appRoutes.ts

// Fetch the base URL from environment variables
const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL;

// Log the base URL for debugging purposes
console.log('NEXT_PUBLIC_BASE_URL:', BASE_URL);

// Define API paths relative to the base URL
const API_PATH = {
    // Authentication routes
    LOGIN: `${BASE_URL}api/token/`,
    REFRESH_TOKEN: `${BASE_URL}api/token/refresh/`,

    // API routes based on Django router
    ORDERS: `${BASE_URL}api/orders/`,
    SPECIMENS: `${BASE_URL}api/specimens/`,
    SPECIMEN_TYPES: `${BASE_URL}api/specimen-types/`,
    SPECIMEN_TYPE_SNOMED_CODES: `${BASE_URL}api/specimen-type-snomed-codes/`,
    SOURCE_DESCRIPTIONS: `${BASE_URL}api/source-descriptions/`,
    SPECIMEN_SOURCES: `${BASE_URL}api/specimen-sources/`,
    SOURCE_SNOMED_CODES: `${BASE_URL}api/source-snomed-codes/`,
    SUBMISSIONS: `${BASE_URL}api/submissions/`,
    PATIENTS: `${BASE_URL}api/patients/`,
    CITIES: `${BASE_URL}api/cities/`,
    STATES: `${BASE_URL}api/states/`,
    RACES: `${BASE_URL}api/races/`,
    ETHNICITIES: `${BASE_URL}api/ethnicities/`,
    ENVIRONMENTS: `${BASE_URL}api/environments/`,
    GENDERS: `${BASE_URL}api/genders/`,
    DISTRICTS: `${BASE_URL}api/districts/`,
    TEST_LOCATIONS: `${BASE_URL}api/test-locations/`,
    ORDERING_PHYSICIANS: `${BASE_URL}api/ordering-physicians/`,
    COLLECTION_DATES: `${BASE_URL}api/collection-dates/`,
    COLLECTION_TIMES: `${BASE_URL}api/collection-times/`,

};

export {
    BASE_URL,
    API_PATH
};
