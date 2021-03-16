import imgui


class ManagerScreen:
    def __init__(self, game, manager):
        self.manager = manager

    def draw(self):
        imgui.set_next_window_position(340, 160)
        imgui.set_next_window_size(300, 500)
        imgui.begin(self.manager)
        if imgui.button("next"):
            imgui.end()
            return True
        imgui.end()
