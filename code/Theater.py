#from TimeError import TimeError
from Usuario import User
from Show import Show
from typing import List

class TimeError(ValueError):
    def __init__(self) -> None:
        """
        Class Constructor of TimeError

        inherits from ValueError
        validates time format
        """
        super().__init__("Unsupported time")

class Theater:
    def __init__(self, vip_seats:int, reg_seats:int, shows:List[Show]=None) -> None:
        """
        Class constructor of Theatre

        + vip_seats: number of vip seats
        + reg_seats: number of regular seats
        + shows: list of Shows in Theatre
        + users: list of users registered in Theatre
        """
        self.vip_seats = vip_seats
        self.reg_seats = reg_seats
        self.shows = []
        self.users = []
        if shows is not None: #adds shows if given on init
            self.add_shows(shows)

    def add_show(self,show:Show):
        """
        Adds a show to shows list

        Sets its seats to those of theatre
        """
        show.vip = self.vip_seats
        show.reg = self.reg_seats
        self.shows.append(show)

    def add_user(self,name:str,preference:str):
        self.users.append(User(name,preference))

    def add_shows(self,shows:List[Show]):
        """
        Adds several shows
        through iteration
        """
        for show in shows:
            self.add_show(show)
    
    def search_available(self,name:str,time:str):
        """
        Shows availability of movie on time

        Arguments
        + name: movie name
        + time
        """
        found = None
        on = False
        for show in self.shows:
            show:Show
            if show.movie == name:
                print(f"{name} is on theatre")
                found = show
                if show.time == time:
                    print(f"And screening at {time}")
                    on = True
                else:
                    print(f"But not at {time}...")
        return found,on
    def search_user(self,name):
        found = None
        for user in self.users:
            user:User
            if user.name == name:
                found = True
        return found

    def sell_tickets(self,vip:int,reg:int,movie:str,time:str,user:str):
        """
        Sells ticket to Show if possible
        
        Arguments
        + vip: desired number of VIP seats
        + reg: desired number of regular seats
        + movie:: movie name
        + time: desired time
        """
        check = time.split(":")
        if (int(check[0])<0 or int(check[0])>23) \
        or (int(check[1])<0 or int(check[1])>59):
            raise TimeError() #Validation
        
        # Sees availability
        reg = self.search_user(user) 
        if reg:
            show,on = self.search_available(movie,time)
            if show is None:
                print(f"{movie} not found on theatre")
            if show and on: # If available
                if show.vip<vip:
                    print("Not enough vip spaces")
                else:
                    print(f"SOLD {vip} VIP tickets")
                    show.vip -= vip
                    print(f"available {show.vip}")

                if show.reg<reg:
                    print("Not enough regular spaces")
                else:
                    print(f"SOLD {vip} regular tickets")
                    show.reg -= reg
                    print(f"available {show.reg}")
                # Sell possible seats
        else:
            print("user not registered")

    def show_shows(self):
        for show in self.shows:
            print(show)

l1 = [Show("Dune","7:30"),Show("1917","9:30")] # List with shows

teatro = Theater(2,1,l1) # Instantiate theater with given seats and shows
teatro.show_shows()
teatro.add_user("dave","vip")

teatro.sell_tickets(1,1,"Dune","7:30","dav") # Sell enough tickets and name is right

