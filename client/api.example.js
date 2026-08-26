// Copy this into your frontend project. Replace NGROK_URL with the current ngrok URL.
const NGROK_URL = 'https://hurling-catalog-pretense.ngrok-free.dev';

// --- Axios ---
import axios from 'axios';

export const api = axios.create({
  baseURL: `${NGROK_URL}/api`,
  withCredentials: true,
  headers: {
    'ngrok-skip-browser-warning': 'true',
  },
});

// --- Fetch ---
export async function fetchApi(path, options = {}) {
  const response = await fetch(`${NGROK_URL}/api${path}`, {
    credentials: 'include',
    ...options,
    headers: {
      'ngrok-skip-browser-warning': 'true',
      ...options.headers,
    },
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
