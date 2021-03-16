import imgui


class DivisionRoundScreen:
    def __init__(self, game):
        self.game = game
        pass

    def draw(self):
        imgui.set_next_window_position(340, 160)
        imgui.set_next_window_size(300, 500)
        imgui.begin("Round " + str(self.game.divisions[0].current_round_number))
        imgui.progress_bar(self.game.current_time / 90)
        imgui.separator()
        for division in self.game.divisions:
            imgui.text("Division ")
            imgui.separator()
            for match in division.current_round:
                imgui.text(str(match.team_a) + " x " + str(match.team_b))
        imgui.separator()
        imgui.end()
        pass
