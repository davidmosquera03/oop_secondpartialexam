from typing import List

class TimeError(ValueError):
    def __init__(self) -> None:
        """
        Class Constructor of TimeError

        inherits from ValueError
        validates time format
        """
        super().__init__("Unsupported time")

class Show:
    def __init__(self, movie:str, time: str) -> None:
        """
        Class Constructor of Show

        + movie: movie name
        + vip: number of vip seats (starts at 0)
        + reg: number of regular seats (starts at 0)
        + time: time of screening
        + full: available
        """
        self.movie = movie
        self.vip = 0
        self.reg = 0
        check = time.split(":")
        if (int(check[0])<0 or int(check[0])>23) \
        or (int(check[1])<0 or int(check[1])>59):
            raise TimeError() #Validation
        self.time = time