# team_games_planner

Plan some games between some teams

This is a toy project to dicover/play with Python and Github

## But

6 équipes doivent s'affronter 2 à 2 sur différents jeux (fléchettes, babyfoot, billard, échecs, etc.).

Le but est de plannifier l'ordre dans lequel elles vont se défier en respectant quelques contraintes :
- chaque équipe affronte chaque autre équipe une seule et unique fois
- des équipes différentes peuvent jouer simultanément pendant un même tour
- un jeu ne peut pas être utilisé simulanément pendant un même tour
- une équipe ne peut participer qu'à un seul jeu pendant un tour donné
- le nombre de tour est limité à 6

## Code

### Idées générales
- écrire un code minimal qui trouve une solution
- rend une réponse en un temps raisonnable (pour 6 équipes, 5 jeux, 6 tours)
- cette version pourrait être optimisée (assez brutale, elle cherche toutes les combinaisons jusqu'à tomber sur une solution)

### Nommage
- équipe : `team`
- jeu : `game`
- tour : `turn`

Ces éléments sont tous traités comme des indices entre 0 et n-1. Autrement dit la variable `team_a' est l'indice d'une équipe (entre 0 et 4 si on a 5 équipes).

### Principe
- on parcours récursivement chaque paire d'équipes (team_a, team_b)
- pour chaque paire d'équipes on teste chaque combinaison (game, turn) qui respecte toutes les contraintes
- si on n'arrive pas à une solution on teste la combinaison suivante
- si on arrive à la fin (toutes les paires d'équipes ont une paire (game, turn) qui respecte les contraintes) : on a réussi !
