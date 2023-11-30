import pandas
from receipt_pdf import  generate_pdf

df = pandas.read_csv("hotels.csv", dtype={"id": str})

class User:
    def view_hotels(self):
        pass

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
         """ Book a hotel by changing its availability to no """
         df.loc[df["id"] == self.hotel_id, "available"] = "no"
         df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""Thank you for your reservation! 
        Here are you booking data: 
        Name : {self.customer_name}
        Hotel name: {self.hotel.name}"""
        generate_pdf(self.customer_name, self.hotel.name)
        return content


print(df)
hotelId = input("Enter the id of the hotel: ")
hotel = Hotel(hotelId)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")


