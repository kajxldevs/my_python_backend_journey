// CycleFit API connector
const API = "http://localhost:8000";

// SIGNUP
async function apiSignup(username, password) {
  const res = await fetch(`${API}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  return await res.json();
}

// LOGIN
async function apiLogin(username, password) {
  const res = await fetch(`${API}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  return await res.json();
}

// BMI
async function apiBMI(weight, height) {
  const res = await fetch(`${API}/bmi?weight=${weight}&height=${height}`);
  return await res.json();
}

// CYCLE PHASE — converts YYYY-MM-DD to DD/MM/YYYY for Python backend
async function apiCycle(period_date) {
  let formatted = period_date;
  if (period_date && period_date.includes('-')) {
    const parts = period_date.split('-');
    formatted = `${parts[2]}/${parts[1]}/${parts[0]}`;
  }
  const res = await fetch(`${API}/cycle?period_date=${formatted}`);
  return await res.json();
}

// WORKOUT
async function apiWorkout(phase, equipment, body_part) {
  const res = await fetch(`${API}/workout?phase=${phase}&equipment=${equipment}&body_part=${body_part}`);
  return await res.json();
}

// SAVE MOOD
async function apiSaveMood(mood, energy) {
  const res = await fetch(`${API}/mood`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mood, energy })
  });
  return await res.json();
}

// GET MOODS
async function apiGetMoods() {
  const res = await fetch(`${API}/moods`);
  return await res.json();
}
