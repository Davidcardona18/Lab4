
#David Cardona - October 15, 2024
# Fixed assignment operator, added missing colons, replaced '&&' with 'and', and completed 'elif' condition.
year = int(input("Hey! What time are you from? "))

if year <= 1900:
    print('Huh, That is way far back!')
elif year > 1900 and year < 2020:
    print("Cool, not too far in the past!")
elif year >= 2020:
    print("That is impresive, way far in the future!!")