import json
import requests

URL = "https://stats.nba.com/stats/leagueleaders"
PARAMS = {
    "LeagueID": "00",
    "PerMode": "PerGame",
    "Scope": "S",
    "Season": "2026-27",
    "SeasonType": "Regular Season",
    "StatCategory": "PTS",
}
# NBA odbija zahtjeve bez ovih zaglavlja
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
    "Accept": "application/json",
}

resp = requests.get(URL, params=PARAMS, headers=HEADERS, timeout=30)
resp.raise_for_status()
data = resp.json()

result = data.get("resultSet") or data["resultSets"][0]
cols = result["headers"]

players = []
for row in result["rowSet"][:10]:
    p = dict(zip(cols, row))
    players.append({
        "id": p["PLAYER_ID"],
        "rank": p["RANK"],
        "name": p["PLAYER"],
        "team": p["TEAM"],
        "team_id": p["TEAM_ID"],
        "gp": p["GP"],
        "min": p["MIN"],
        "pts": p["PTS"],
        "reb": p["REB"],
        "ast": p["AST"],
        "stl": p["STL"],
        "blk": p["BLK"],
        "tov": p["TOV"],
        "fg_pct": p["FG_PCT"],
        "fg3_pct": p["FG3_PCT"],
        "ft_pct": p["FT_PCT"],
        "photo": f"https://cdn.nba.com/headshots/nba/latest/1040x760/{p['PLAYER_ID']}.png",
        "team_logo": f"https://cdn.nba.com/logos/nba/{p['TEAM_ID']}/global/L/logo.svg",
    })

with open("players.json", "w", encoding="utf-8") as f:
    json.dump(players, f, ensure_ascii=False, indent=2)

print(f"Spremljeno {len(players)} igraca.")
for pl in players:
    print(pl["rank"], pl["name"], pl["team"], pl["pts"])