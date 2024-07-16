from art import logo
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

biddings = {}

def addBidding(bidder, value, biddingRecord):
    biddingRecord[bidder] = value

def auctionResults(biddingRecord):
    # highestBid = max(biddingRecord, key=biddingRecord.get)
    highestBid = 0
    for bidder in biddingRecord:
        if biddingRecord[bidder] > highestBid:
            highestBid = biddingRecord[bidder]
            winningPerson = bidder
    print(f"The winner is {winningPerson} with a bid of ${highestBid:.2f}")


endOfAuction = False

print(logo)
print("\nWelcome to the Blind Auction Program.")

while not endOfAuction:
    name = input("Your name: ")
    bid = float(input("Your bid: $"))
    while bid < 0:
        bid = float(input("Please type only positive values.\nYour bid: $"))
    addBidding(name, bid, biddings)

    retry = True
    while retry:
        otherBid = input("Are there any other bidders ? Type 'yes' or 'no'.\n").lower()
        if otherBid == "yes":
            retry = False
            clear_console()
        elif otherBid == "no":
            retry = False
            endOfAuction = True
            clear_console()

auctionResults(biddings)