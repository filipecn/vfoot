class Team:
    def __init__(self, players_data, team_data, money, coach, moral):
        self.coach = coach
        self.players_data = players_data
        self.team_data = team_data
        self.money = money
        self.moral = moral
        self.human = False
