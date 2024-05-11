from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(this, first_name, is_alive=True):
        print("In character init")
        this.first_name = first_name
        this.is_alive = is_alive

    @abstractmethod
    def die(this):
        """Your docstring for Method die."""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(this, first_name, is_alive=True):
        """Your docstring for Constructor."""
        super().__init__(first_name, is_alive)

    def die(this):
        """Your docstring for Method die."""
        this.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
