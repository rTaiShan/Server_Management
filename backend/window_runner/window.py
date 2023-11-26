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

    def read_stdout(self, read_from=None):
        if read_from is None:
            read_from = self.stdout_head
        stdout = self._read_buffer().stdout
        self.stdout_head = len(stdout)
        return stdout[self.stdout_head:]
    
    def read_stderr(self, read_from=None):
        if read_from is None:
            read_from = self.stderr_head
        stderr = self._read_buffer().stderr
        self.stderr_head = len(stderr)
        return stderr[self.stderr_head:]
