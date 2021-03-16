from game.match import Match


class Division:
    def __init__(self, number, game_intance):
        self.division_number = number
        self.matches = []
        # Note: all teams from all divisions!
        self.game = game_intance

        for index_a in range(self.division_number * 8, (self.division_number + 1) * 8):
            for index_b in range(self.division_number * 8, (self.division_number + 1) * 8):
                if index_a == index_b:
                    continue
                self.matches.append((index_a, index_b))

        self.current_round_number = 0
        self.current_round = []

    def build_round(self):
        self.current_round_number += 1
        self.current_round = [Match(self.matches[0][0],
                                    self.matches[0][1])]
        round_match_indices = [0]
        for m in range(len(self.matches)):
            is_a_round_match = True
            for rm in self.current_round:
                if rm.team_a in list(self.matches[m]) or rm.team_b in list(self.matches[m]):
                    is_a_round_match = False
                    break
            if is_a_round_match:
                self.current_round.append(Match(self.matches[m][0],
                                                self.matches[m][1]))
                round_match_indices.append(m)
        for i in range(len(round_match_indices) - 1, -1, -1):
            self.matches.pop(round_match_indices[i])

    def run(self, time_step):
        # RODA UM POUQUINHO A MAIS DE CADA UMA DAS 4 PARTIDAS DESSA DIVISAO
        pass
