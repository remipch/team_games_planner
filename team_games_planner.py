# Paramètres globaux
teams_count = 6
games_count = 5
turns_count = 6

# Contient l'indice du 'game' pour une paire de 'team'
# sous forme de liste de dictionnaires
# de telle sorte que 'team_pair_games[team_a][team_b] = game'
team_pair_games = []

# Contient l'indice du 'turn' pour une paire de 'team'
# sous forme de liste de dictionnaires
# de telle sorte que 'team_pair_turns[team_a][team_b] = turn'
team_pair_turns = []

# Contient les indices des 'game' déjà joués par chaque 'team'
# sous forme de liste de liste
# de telle sorte que 'game in team_games[team]' indique si l'équipe 'team' a déjà joué le jeu 'game'
team_games = []

# Contient les indices des 'turn' déjà joués par chaque 'team'
# sous forme de liste de liste
# de telle sorte que 'turn in team_turns[team]' indique si l'équipe 'team' a déjà joué le tour 'turn'
team_turns = []

# Contient les indices des 'game' déjà joués à chaque 'turn'
# sous forme de liste de liste
# de telle sorte que 'game in turn_games[turn]' indique si le jeu 'game' est déjà plannifié pour le tour 'turn'
turn_games = []

# Initialise les variables globales vides
for team in range(teams_count):
	team_pair_games.append({})
	team_pair_turns.append({})
	team_games.append([])
	team_turns.append([])
for team in range(turns_count):
	turn_games.append([])

def search_sub_solution(level,team_a,team_b,game,turn):
	print("  " * level + "team_a:" + str(team_a) + " team_b:" + str(team_b) + " game:" + str(game) + " turn:" + str(turn))

	team_pair_games[team_a][team_b] = game
	team_pair_turns[team_a][team_b] = turn
	team_games[team_a].append(game)
	team_games[team_b].append(game)
	team_turns[team_a].append(turn)
	team_turns[team_b].append(turn)
	turn_games[turn].append(game)

	if search_next_solution(level,team_a,team_b):
		return True

	team_games[team_a].pop()
	team_games[team_b].pop()
	team_turns[team_a].pop()
	team_turns[team_b].pop()
	turn_games[turn].pop()
	return False

def search_next_solution(last_level,last_team_a,last_team_b):
	if last_team_b < teams_count - 1:
		next_team_a = last_team_a
		next_team_b = last_team_b + 1
	elif last_team_a < teams_count - 2:
		next_team_a = last_team_a + 1
		next_team_b = next_team_a + 1
	else:
		return True

	return search_solution(last_level + 1,next_team_a,next_team_b)

def search_solution(level,team_a,team_b):
	for game in range(games_count):
		if not game in team_games[team_a] and not game in team_games[team_b]:
			# Aucune des deux équipes n'a déjà joué ce jeu
			for turn in range(turns_count):
				if not game in turn_games[turn]:
					# Ce jeu n'est pas déjà occupé pour ce tour
					if not turn in team_turns[team_a] and not turn in team_turns[team_b]:
						# Aucune des deux équipes n'est déjà occupée sur ce tour
						if search_sub_solution(level,team_a,team_b,game,turn):
							return True
	return False

if search_solution(0,0,1):
	print("solution found :-)")
	print()
	for team_a in range(teams_count):
		for team_b in range(team_a + 1,teams_count):
			game = team_pair_games[team_a][team_b]
			turn = team_pair_turns[team_a][team_b]
			print("team_a:" + str(team_a) + " team_b:" + str(team_b) + " game:" + str(game) + " turn:" + str(turn))
		print()
else:
	print("no solution found :-(")
