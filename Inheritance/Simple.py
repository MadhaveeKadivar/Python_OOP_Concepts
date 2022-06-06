class Father:
    def property(self):
        print("Car : BMW")
        print("Home : 5BHK bunglow")
        print("Land : 10 acre")
class Son(Father):
    def books(self):
        print("Son is studying in 5th So He has study books\n")
    def games(self):
        print("Son has games like Chess,Ludo,etc...\n")
    def father_property(self):
        print("Son also having his father Property")
        property()