import libtmux

class Window:
    def __init__(self, session : libtmux.Session, window_name=None, attach=True) -> None:
        self.tmux_window = session.new_window(window_name=window_name, attach=attach)
        # Use single pane
        self.pane = self.tmux_window.attached_pane
        self.stdout_head = 0
        self.stderr_head = 0

    def send_keys(self, keys):
        self.pane.send_keys(keys)

    def _read_buffer(self):
        return self.pane.cmd('capture-pane', '-p')

    def read_stdout(self, from_start=False):
        stdout = self._read_buffer().stdout
        result = stdout if from_start else stdout[self.stdout_head:]
        self.stdout_head = len(stdout)
        return result

    def read_stderr(self, from_start=False):
        stderr = self._read_buffer().stderr
        result = stderr if from_start else stderr[self.stderr_head:]
        self.stderr_head = len(stderr)
        return result
