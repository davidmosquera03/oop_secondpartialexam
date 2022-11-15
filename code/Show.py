from typing import List
import abc 



class AbstractShow(abc.ABC):
    def __init__(self,movie:str, time: str) -> None:
        """
        Class Constructor of AbstractShow

        + movie: movie name
        + vip: number of vip seats (starts at 0)
        + reg: number of regular seats (starts at 0)
        + time: time of screening
        + full: available
        """        
        self.movie = movie
        self.vip:int = 0
        self.reg:int = 0
        check = time.split(":")
        if (int(check[0])<0 or int(check[0])>23) \
        or (int(check[1])<0 or int(check[1])>59):
            raise ValueError("Not valid time") #Validation
        self.time = time

    @abc.abstractclassmethod
    def full(self)->bool:
        """
        Property decorator to calculate
        full attribute

        Full if not any seat on VIP
        or regular is left
        """
        if self.vip == 0 and self.reg == 0:
            return True
        else:
            return False

class Show(AbstractShow):
    

    @property
    def full(self)->bool:
        """
        Property decorator to calculate
        full attribute

        Full if not any seat on VIP
        or regular is left
        """
        if self.vip == 0 and self.reg == 0:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Movie:{self.movie} at {self.time}"

