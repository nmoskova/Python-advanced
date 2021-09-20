num_guests = int(input())
guest_list = {input() for _ in range(num_guests)}

while True:
    command = input()

    if command == "END":
        break

    guest = command
    guest_list.remove(guest)

vip_guests = sorted({g for g in guest_list if g[0].isdigit()})
regular_guests = sorted(guest_list.difference(vip_guests))

print(len(guest_list))
[print(guest) for guest in vip_guests]
[print(guest) for guest in regular_guests]
