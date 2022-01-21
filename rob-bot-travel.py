#define list of destinations
destinations = [
    "london",
    "new york",
    "cape town",
    "shanghai",
    "cairo",
    "sydney",
    "toronto",  
    "reykjavik",
    "helsinki",
    "hong kong",
    "berlin",
    "las vegas"
]

# get input from user
flyingTo = input("Where do you want to fly to? ").lower()
flyingFrom = input("Where do you want to fly from? ").lower()

#if statements to check if destinations and start airport is in list
if flyingTo in destinations and flyingFrom in destinations:
    print("Book your flight now on freerobbotflights.biz! We have a flight for your chosen destination!")
elif flyingTo not in destinations and flyingFrom in destinations:
    print("We have a location at your airport you want to fly from but not the destination! Too bad")
elif flyingTo in destinations and flyingFrom not in destinations: 
    print("We have a location at your destination but not where you want to fly from! Too bad")
else:
    print("You will not leave the country.")