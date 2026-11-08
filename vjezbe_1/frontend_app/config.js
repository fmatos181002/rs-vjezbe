const API_URL = "https://rs-vjezbe-1-backend-lz08.onrender.com";

// Zaštita od ubacivanja HTML-a u tekst koji stiže s API-ja
function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}