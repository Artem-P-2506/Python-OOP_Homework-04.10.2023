from Coin import *
from Bill import *

if __name__ == "__main__":
    coin10 = Coin("Bronze", "None", 10, 2009, "round", 15, "True")
    bill100 = Bill("Paper", "Yellow", 100, 2018, "rectangle", 142, 75, "AK12547863", "waterStamp.png", "facialPicture.png", "backPicture.png")

    print("\n-=-=-=-=-=-=-=-=-=-=- МОНЕТА -=-=-=-=-=-=-=-=-=-=-")
    coin10.show()
    print("\n-=-=-=-=-=-=-=-=-=-=- КУПЮРА -=-=-=-=-=-=-=-=-=-=-")
    bill100.show()