from code.Theater import Theater,Show


l1 = [Show("Dune","7:30"),Show("1917","9:30")] # List with shows

teatro = Theater(2,1,l1) # Instantiate theater with given seats and shows
print("SHOWS")
teatro.show_shows()
teatro.add_user("dave","vip")
teatro.sell_tickets(1,0,"Dune","7:30","nick") # Not registered
teatro.sell_tickets(2,1,"Dune","7:30","dave") # Not enough spaces
teatro.sell_tickets(1,2,"Interestellar","9:30","dave") # Movie not shown
teatro.sell_tickets(1,1,"Dune","9:00","dave")   # Wrong time

teatro.add_user("nick","reg") # Nick is registered
teatro.sell_tickets(1,0,"Dune","7:30","nick") # Movie is already full


