def calc_area(base, height):
    # calculate area

    # process
    area = base * height / 2
    # output
    print("The area of the triangle is {}".format(area))


def main():
    # this function gets lenght and width

    # input
    try:
        base = float(input("What is the base of the triangle: "))
        height = float(input("What is the height of the triangle: "))
    except ValueError:
        print("Input should be float")

    # call functions
    calc_area(base, height)


if __name__ == "__main__":
    main()
