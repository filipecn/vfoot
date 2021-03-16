import graphics
import imgui
from game.game import Game, GameState
from graphics.division_round_screen import DivisionRoundScreen
from graphics.manager_screen import ManagerScreen

game = None
division_round_screen = None
manager_screens = []
current_manager_screen = 0


class ChooseCountriesScreen:
    def __init__(self):
        # screen elements
        self.country_name = ["Pais " + str(i) for i in range(4)]
        self.country_checked = 4 * [False]
        # flow states
        self.active = False

    def country_list(self):
        l = []
        for i in range(4):
            if self.country_checked[i]:
                l.append(i)
        return l

    def draw(self):
        completed = False
        if self.active:
            imgui.begin("##window", False, imgui.WINDOW_NO_TITLE_BAR)

            if imgui.button("Select All"):
                for i in range(len(self.country_checked)):
                    self.country_checked[i] = True
            imgui.same_line()
            if imgui.button("Select None"):
                for i in range(len(self.country_checked)):
                    self.country_checked[i] = False

            for i in range(4):
                _, state = imgui.checkbox(self.country_name[i],
                                          self.country_checked[i])
                self.country_checked[i] = state
            if imgui.button("next"):
                if True in self.country_checked:
                    self.active = False
                    completed = True
            imgui.end()
        return completed


class ChooseManagersScreen:
    def __init__(self):
        # screen elements
        self.manager_label = ["Tecnico " + str(i) for i in range(6)]
        self.manager_name = 6 * [""]
        # flow states
        self.active = False

    def manager_list(self):
        l = []
        for name in self.manager_name:
            if len(name) > 0:
                l.append(name)
        return l

    def draw(self):
        completed = False
        if self.active:
            imgui.begin("##window", False, imgui.WINDOW_NO_TITLE_BAR)
            for i in range(6):
                _, value = imgui.input_text(self.manager_label[i],
                                            self.manager_name[i], 30)
                self.manager_name[i] = value
            if imgui.button("play!"):
                for name in self.manager_name:
                    if len(name):
                        self.active = False
                        completed = True
                        break

            imgui.end()
        return completed


choose_countries_screen = ChooseCountriesScreen()
choose_managers_screen = ChooseManagersScreen()


def draw_new_game_window():
    pass


def draw_main_menu():
    global choose_countries_screen
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("Jogo", True):
            clicked, _ = imgui.menu_item(
                "Novo Jogo", 'Cmd+S', False, True
            )
            if clicked:
                choose_countries_screen.active = True
            clicked, _ = imgui.menu_item(
                "Quit", 'Cmd+Q', False, True
            )
            if clicked:
                exit(1)

            imgui.end_menu()
        imgui.end_main_menu_bar()


def render():
    global game
    global division_round_screen
    global manager_screens
    global current_manager_screen

    draw_main_menu()

    if choose_countries_screen.draw():
        choose_managers_screen.active = True

    if choose_managers_screen.draw():
        game = Game(
            choose_managers_screen.manager_list(),
            choose_countries_screen.country_list())
        # create manager screens
        print(choose_managers_screen.manager_list())
        for manager in choose_managers_screen.manager_list():
            manager_screens.append(ManagerScreen(game, manager))

    if game is not None:
        game.run()
        if game.current_state == GameState.DIVISION_ROUND_STATE:
            if division_round_screen is None:
                division_round_screen = DivisionRoundScreen(game)
            division_round_screen.draw()
        elif game.current_state == GameState.MANAGER_STATE:
            if current_manager_screen >= len(manager_screens):
                current_manager_screen = 0
                game.current_state = GameState.DIVISION_ROUND_STATE
            elif manager_screens[current_manager_screen].draw():
                current_manager_screen += 1


if __name__ == "__main__":
    graphics.app(render)
