from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class docstring."""

    def __init__(self, first_name, is_alive=True):
        """King constructor."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Set the eyes color to the specified color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hairs color to the specified color."""
        self.hairs = color

    def get_eyes(self) -> str:
        """Return the color of the eyes."""
        return self.eyes

    def get_hairs(self) -> str:
        """Return the color of the hairs."""
        return self.hairs


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
