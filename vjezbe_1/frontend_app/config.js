const API_URL = "http://127.0.0.1:8000";

// Zaštita od ubacivanja HTML-a u tekst koji stiže s API-ja
function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}