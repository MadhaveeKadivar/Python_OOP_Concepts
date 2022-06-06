class Mobile:
    def mobile_features(self):
        print("Mobile has basic features like : Calling , Game playing , Displying time and date")

class Samsung(Mobile):
    def brand(self):
        print("Mobile Brand : Samsung")
    def os(self):
        print("Mobile Operating System : Android") 

class SamsungS10Lite(Samsung):
    def model(self):
        print("Mobile Model name : Samsung S10 Lite")
    def specifications(self):
        print("Samsung S10 Lite mobile Specification")
        print("Battery : 6000mah")
        print("Camera : 64mp")
        print("RAM : 16 GB")
        print("Storage : 500GB")