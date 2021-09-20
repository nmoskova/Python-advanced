from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
prize = int(input())

bullets_left = gun_barrel_size

while locks and bullets:

    current_bullet = bullets.pop()
    current_lock = locks[0]
    bullets_left -= 1
    prize -= bullet_price

    if current_lock >= current_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if bullets_left == 0 and bullets:
        bullets_left = gun_barrel_size
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${prize}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
