from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(this, first_name, is_alive=True):
        """Initialize a Baratheon character with a first name and a status\
        of being alive."""
        this.first_name = first_name
        this.is_alive = is_alive
        this.family_name = "Baratheon"
        this.eyes = "brown"
        this.hairs = "dark"

    def die(this):
        """Set the status of the Baratheon character to not alive."""
        this.is_alive = False

    def __str__(this) -> str:
        """Baratheon's method __str__: returns string
        with name, color of eyes and hairs but it goes through repr"""

    def __repr__(this) -> str:
        """Return a string representation of the Baratheon character."""
        return (f"Vector: {(this.family_name, this.eyes, this.hairs)}")


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(this, first_name, is_alive=True):
        """Initialize a Lannister character with a first name and a status\
        of being alive."""
        this.first_name = first_name
        this.is_alive = is_alive
        this.family_name = "Lannister"
        this.eyes = "blue"
        this.hairs = "light"

    def die(this):
        """Set the status of the Lannister character to not alive."""
        this.is_alive = False

    def __str__(this) -> str:
        """Lannister's method __str__: returns string
        with name, color of eyes and hairs but it goes through repr"""

    def __repr__(this) -> str:
        """Return a string representation of the Lannister character."""
        return (f"Vector: {(this.family_name, this.eyes, this.hairs)}")

    @classmethod
    def create_lannister(this, first_name, is_alive):
        """Create a Lannister character with the specified first name\
        and status of being alive."""
        instance = this(first_name)
        instance.is_alive = is_alive
        return (instance)


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}\
        , Alive : {Jaine.is_alive}")
    return (0)


if __name__ == "__main__":
    main()
