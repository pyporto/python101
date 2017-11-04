def three_things():
    print("What's three most important things in your life")

    things = []
    for i in range(3):
        thing = input("Thing number {}: ".format(i + 1))
        things.append(thing)

    print(things)

    print("That's what you named")
    for thing2 in things:
        print(thing2)

if __name__ == '__main__':
    three_things()
