import pandas as pd
from enum import Enum
import random
from game.division import Division
from game.team import Team


class GameState(Enum):
    MANAGER_STATE = 0
    DIVISION_ROUND_STATE = 1
    CLASSIFICATION_STATE = 2


class Game:
    def __init__(self, manager_list, country_list):
        # load teams file data base
        team_db = pd.read_csv("../data/times.csv")
        # load players file data base
        players_db = pd.read_csv("../data/jogadores.csv")
        # load coaches file data base
        coaches_db = pd.read_csv("../data/tecnicos.csv")
        # filter teams by country list
        self.team_list = team_db[team_db['nacionalidade'].isin(country_list)]
        # check if we have at least 32 teams
        if len(self.team_list) < 32:
            print("TODO: generate teams to get 32")
        # create division championships
        self.teams = []
        self.divisions = []
        for i in range(4):
            df = self.team_list[self.team_list.score >= i * 5]
            df = df[df.score < (i + 1) * 5]
            selected_teams = df.sample(8)
            for index, row in selected_teams.iterrows():
                self.teams.append(
                    Team(
                        players_data=players_db[players_db.time == index],
                        team_data=row,
                        money=1000000,
                        coach=coaches_db.sample(1),
                        moral=1
                    ))
            # create division
            self.divisions.append(Division(i, self))

        # human players
        self.managers = []
        indices = [x for x in range(0, 8)]
        for manager in manager_list:
            random_index = random.randint(0, len(indices) - 1)
            team_id = indices[random_index]
            indices.pop(random_index)
            self.teams[team_id].human = True
            self.managers.append((manager, team_id))

        self.current_time = 0
        self.current_state = GameState.MANAGER_STATE

    def run(self):
        if self.current_state == GameState.DIVISION_ROUND_STATE:
            if self.current_time == 0:
                for division in self.divisions:
                    division.build_round()
            self.current_time += 1
            for division in self.divisions:
                division.run(self.current_time)
            if self.current_time >= 90:
                self.current_state = GameState.MANAGER_STATE
                self.current_time = 0
        elif self.current_state == GameState.MANAGER_STATE:
            pass
