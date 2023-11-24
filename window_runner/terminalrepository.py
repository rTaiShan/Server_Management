import libtmux
from .window import Window

DEFAULT_PANE_WIDTH = 200

class TerminalRepository:
    def __init__(self) -> None:
        self.windows : list[Window] = []
        self.server = libtmux.Server()
        self.session = self.server.new_session(
            kill_session=True, 
            attach=False, 
            x=DEFAULT_PANE_WIDTH
        )

    def create_window(self, window_name=None, attach=False):
        """
        Create new Window
        attach -> Immediately selects new Window if True 
        """
        window = Window(self.session, window_name, attach)
        self.windows.append(window)
        return window

    def select_window(self, window : Window):
        self.session.select_window(window.tmux_window.index)
