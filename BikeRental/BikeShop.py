import datetime


class Customer():
    globals
    rent_time = datetime.datetime.now()
    rent_type = ""
    count = 0
    rent_payment = 0
    def __init__(self, first, last, phone):
        self.name = first + " " + last
        self.phone = phone
        self.email = first +"."+ last + "@email.com"

    def __repr__(self) -> str:
        return "Name: " + self.name

class BikeShop():
    rent_fee = 0
    stock = 100
    def __init__(self, cls):
        self.name = cls.name
        self.cls = cls

    def display_stock(self):
        repr = print(f"We have {self.stock} bikes available.")
        return repr
        
    def rent_type(self, type):
        action = type
        match action:
            case "hourly":
                self.rent_fee = 5
            case "daily":
                self.rent_fee = 20
            case "weekly":
                self.rent_fee = 100

    def price(self, type, rent_time):
        action = type
        now = datetime.datetime.now()
        day, month, hour = int(now.day), int(now.month), int(now.hour)
        rent_day, rent_month, rent_hour = int(rent_time.day), int(rent_time.month), int(rent_time.hour)
        rent_date = str(rent_time.date)
        match action:
            case "hourly":
                rent_duration = (hour - rent_hour)
                return rent_duration
            
            case "daily":
                if month != rent_month:
                    if rent_hour < hour:
                        rent_duration = (month - rent_month) * 30 + (day - rent_day) - 1
                    else:
                        rent_duration = (month - rent_month) * 30 + (day - rent_day)
                    return rent_duration
                else:
                    if rent_hour < hour:
                        rent_duration = (day - rent_day) - 1
                    else:
                        rent_duration = (day - rent_day)
                    return rent_duration
                
            case "weekly":
                if month != rent_month:
                    rent_duration = (month - rent_month) * 30 + (day - rent_day) / 7
                else:
                    rent_duration = (day -  rent_day) / 7
                return rent_duration

    def rent(self):
        type = input("Please enter the rental type(hourly, daily, weekly):")
        count = int(input("How many bikes you want to rent?"))
        if count > self.stock:
            return f"Sorry {self.name}, we don't have enough bikes for you."
        else:
            now = datetime.datetime.now()
            self.rent_type(type)
            print("You have rented a {} bike(s) on {} basis today at {}.".format(count, type, now))
            print(f"You will be charged ${self.rent_fee} per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= count
            self.cls.time = now
            self.cls.rent_type = type
            self.cls.count = count
            self.cls.rent_payment = self.rent_fee



    def return_bike(self, cls):
        price = self.price(cls.rent_type, cls.time)
        print(f" the total price is: {(price * cls.count) * cls.rent_payment: .2f} from {cls.time}")



john = Customer("john", "john@john.com", 12345678)
bike = BikeShop(john)
total_rent = bike.rent()
print(john.rent_type)

john.time = datetime.datetime.strptime("2023-03-25", "%Y-%m-%d")

bike.return_bike(john)
