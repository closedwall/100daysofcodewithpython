import os
print("Welcome to the secret auction programme")

running_status = True
bidding_collection=[]
max={"bid":0}



while running_status:
    name=input("What is your name? ")
    bid = int(input("what's your bid value? $"))
    bidding_collection.append({"name":name, "bid":bid})
    if max['bid']<bid:
        max['bid']=bid
        max['name'] = name
    decision = input("are their any other bidders? Type 'yes' or 'no'. ")
    if decision=='no':
        running_status=False
        os.system('cls')
        print(f"the bidding in won by {max['name']} and given ${max['bid']}")
    else:
        os.system('cls')

