class House:
    color: str
    window_count: int

    def __init__(self, color: str, window_count: int) -> None:
        self.color = color
        self.window_count = window_count

    def get_color(self) -> str:
        return f'elewacja budynku jest koloru {self.color}'

    def add_windows(self, amount: int) -> None:
        self.window_count += amount