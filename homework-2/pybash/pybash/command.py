class Command:
    def __init__(self, name):
        self.name = name

    # NOTE: Mocked implementation.
    def run(self):
        print(f"executing {self.name}")
