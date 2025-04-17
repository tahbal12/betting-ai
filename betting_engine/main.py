print("Betting AI core running...")

sports = ["NBA", "Football", "Tennis"]
matchups = ["Team A vs Team B", "Team C vs Team D", "Team E vs Team F"]
odds = [2.1, 1.8, 2.4]

best_index = odds.index(max(odds))
print(f"Recommended bet: {sports[best_index]} - {matchups[best_index]} at {odds[best_index]} odds")
