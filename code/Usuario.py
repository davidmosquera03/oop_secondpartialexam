class User:
    def __init__(self,name:str,preference:str) -> None:
        """
        Class constructor of User

        + name: name of user
        + preference: type of seat it prefers
        """
        self.name = name
        self.preference = preference

    def __repr__(self):
        return self.name