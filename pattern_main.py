from pattern_generator_class import PatternGenerator
pg = PatternGenerator()

def menu():
    print("\n=== Number Pattern Generator ===")
    print("1. Pyramid")
    print("2. Reverse Pyramid")
    print("3. Floyds Triangle")
    print("4. Pascal Triangle")
    print("5. Fibonacci Series")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter Choice: ")

    if choice == "6":
        print("Exited!")
        break

    try:
        n = int(input("Enter Size (1-20): "))

        if choice == "1":
            p = pg.generate_pyramid(n)

        elif choice == "2":
            p = pg.generate_reverse_pyramid(n)

        elif choice == "3":
            p = pg.generate_floyd(n)

        elif choice == "4":
            p = pg.generate_pascal(n)

        elif choice == "5":
            p = pg.generate_fibonacci(n)

        else:
            print("Invalid! Please Choose Correct option")
            continue

        print("\n" + p)
        pg.save_pattern(choice, p)

    except ValueError as e:
        print("Error:", e)
