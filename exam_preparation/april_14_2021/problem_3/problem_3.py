def flights(*args):
    flights_data = {}
    i = 0
    while i < len(args):
        ch = args[i]
        if ch == "Finish":
            return flights_data

        if ch not in flights_data:
            flights_data[ch] = int(args[i+1])
        else:
            flights_data[ch] += int(args[i+1])
        i += 2

    return flights_data


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))




