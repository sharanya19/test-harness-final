// axios.ts
import axios from 'axios';
import { Order, Specimen, Submitter, Patient } from '../types/api'; // Adjust imports as needed
import { BASE_URL, API_PATH } from './appRoutes';
import { getRefreshToken, getToken, setToken } from './auth';

// Create an instance of axios with base URL
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor to add token to headers if available
api.interceptors.request.use(config => {
  const token = getToken();
  if (token) {
    console.log("Token found:", token);  // Debugging log
    config.headers['Authorization'] = `Bearer ${token}`;
  } else {
    console.warn("No token found, request might be unauthorized.");
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// Interceptor to handle responses and errors
api.interceptors.response.use(response => {
  return response;
}, async error => {
  const originalRequest = error.config;

  // Check if the error is due to an expired token
  if (error.response && error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;

    try {
      const refreshToken = getRefreshToken();

      // Attempt to refresh the token using the refresh token endpoint
      const response = await axios.post(API_PATH.REFRESH_TOKEN, {
        refresh: refreshToken,
      });

      if (response.status === 200) {
        const newAccessToken = response.data.access;
        const newRefreshToken = response.data.refresh;

        // Update tokens
        setToken(newAccessToken, newRefreshToken);

        // Update the Authorization header with the new access token
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;

        // Retry the original request with the new token
        return api(originalRequest);
      }
    } catch (refreshError) {
      console.error("Error refreshing token:", refreshError);
      // Redirect to login page if refresh token is invalid or expired
      window.location.href = '/login';
    }
  }

  return Promise.reject(error);
});
// Fetch Orders
export const fetchOrders = async (): Promise<Order[]> => {
  try {
    const response = await api.get(API_PATH.ORDERS);
    return response.data;
  } catch (error) {
    console.error("Error fetching orders:", error);
    throw error; // Rethrow error to handle it in the component
  }
};


// Fetch Specimens by Order Code
export const fetchSpecimensByOrderCode = async (orderCode: string): Promise<Specimen[]> => {
  try {
    const response = await api.get(`${API_PATH.SPECIMENS}?orderCode=${orderCode}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching specimens for order code ${orderCode}:`, error);
    throw error;
  }
};

// Post Order
export const postOrder = async (order: Order) => {
  try {
    const response = await api.post(API_PATH.ORDERS, order);
    return response.data;
  } catch (error) {
    console.error("Error posting order:", error);
    throw error;
  }
};

// Post Specimen
export const postSpecimen = async (specimen: Specimen) => {
  try {
    const response = await api.post(API_PATH.SPECIMENS, specimen);
    return response.data;
  } catch (error) {
    console.error("Error posting specimen:", error);
    throw error;
  }
};

// Post Submission
export const postSubmission = async (submitter: Submitter) => {
  try {
    const response = await api.post(API_PATH.SUBMISSIONS, submitter);
    return response.data;
  } catch (error) {
    console.error("Error posting submission:", error);
    throw error;
  }
};

// Post Patient
export const postPatient = async (patient: Patient) => {
  try {
    const response = await api.post(API_PATH.PATIENTS, patient);
    return response.data;
  } catch (error) {
    console.error("Error posting patient:", error);
    throw error;
  }
};

// Fetch Dropdown Data
export const fetchDropdownData = async (type: keyof typeof API_PATH): Promise<any[]> => {
  try {
    const response = await api.get(API_PATH[type]);
    console.log('fetchDropdownData', {data: response.data, type})
    return response.data;
  } catch (error) {
    console.error(`Error fetching dropdown data for type ${type}:`, error);
    throw error;  // Re-throwing the error to be handled by the caller
  }
};

export default api;
