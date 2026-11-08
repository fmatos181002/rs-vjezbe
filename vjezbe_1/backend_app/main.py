import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NBA top 10 service")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

DATA = Path(__file__).parent / "players.json"

def load_players():
    return json.loads(DATA.read_text(encoding="utf-8"))
@app.get("/")
def root():
    return {"service": "NBA top 10 service", "endpoints": ["/health", "/players", "/players/{id}", "/docs"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/players")
def list_players():
    return load_players()

@app.get("/players/{player_id}")
def get_player(player_id: int):
    for p in load_players():
        if p["id"] == player_id:
            return p
    raise HTTPException(status_code=404, detail="Igrac nije pronaden")