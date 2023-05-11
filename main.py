from replit import clear
from art import logo

# Create empty dictionary with necessary keys
bid_info = {}

# Define function to find highest bid
def find_highest_bidder(bid_info):
    max_bid = 0
    tied_bid = 0
    tie_amount = 1
    for bidder in bid_info:
        if bid_info[bidder] > max_bid:
            winner = bidder
            max_bid = bid_info[bidder]
        elif bid_info[bidder] == max_bid:
            tie_amount += 1
            tied_bid = max_bid
    # Check for any ties in bids
    if max_bid > tied_bid:
        print(f"The winner is {winner} with a bid of ${max_bid}.")
    else:
        print(f"There has been a {tie_amount}-way tie of ${max_bid}, please restart the bidding process.")

# Greet first user
print(logo)
print("Welcome to the secret auction program!")

bidding = True
while bidding:
    # Collect user information
    bidder_name = input("What is your name?: ")
    bidder_offer_str = input("How much is your bid?: $")
    bidder_offer = round(float(bidder_offer_str))

    # Add user information to dictionary
    bid_info[bidder_name] = bidder_offer
    
    # Check if more users want to bid
    bid_again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if bid_again == "no":
        bidding = False
    else:
        clear()
        print(logo)


# Find the highest bidder
find_highest_bidder(bid_info)