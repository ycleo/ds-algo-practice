def tournamentWinner(competitions, results):
    teamMap = {}
    winner = ""
    winnerPoints = 0

    for game in range(len(results)):
        home, away = competitions[game]
        currWinner = home if results[game] == 1 else away
        teamMap[currWinner] = 3 + teamMap.get(currWinner, 0)
        
        if teamMap[currWinner] > winnerPoints:
            winnerPoints = teamMap[currWinner]
            winner = currWinner

    return winner

# O(c) time | O(n) space
# c: number of competitions
# n: number of teams