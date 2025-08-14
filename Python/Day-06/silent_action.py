def findWinners(bidderData):
    highestBid = 0
    winner = ""
    for bidder in bidderData:
        bidderPrice = bidderData[bidder]
        if bidderPrice > highestBid:
            highestBid = bidderPrice
            winner = bidder
    return f"The winner is {winner} with a bid of {highestBid}"

bidderData = {}
end_of_bidding = False

while not end_of_bidding:
    name = input("What is your Name? ")
    price = int(input("What is your bid? "))
    bidderData[name] = price  # store name: bid
    more_bidders = input("Do you have more bidders? (yes/no) ").lower()
    if more_bidders == "no":
        end_of_bidding = True
        print(findWinners(bidderData))















