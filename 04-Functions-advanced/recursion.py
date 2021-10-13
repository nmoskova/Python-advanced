def factorial(n):
    print(f"Calculating f({n})")

    if n > 1:
        result = n * factorial(n-1)
        print(f"f({n}) = {result}")

        return result
    return 1

factorial(6)
