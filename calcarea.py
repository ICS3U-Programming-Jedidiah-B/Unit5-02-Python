def calc_area(base, height):
    # calculate area

    # process
    area = base * height / 2
    # output
    print("the area is {}".format(area))


def main():
    # this function gets lenght and width

    # input
    try:
        base = float(input("what is base"))
        height = float(input("what is height"))
    except ValueError:
        print("input should be float")

    # call functions
    calc_area(base, height)


if __name__ == "__main__":
    main()
