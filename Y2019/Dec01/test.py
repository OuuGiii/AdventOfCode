def main():
    number1 = 10 / 3  #should be 3
    number2 = 11 / 3  #should be 3
    number3 = 59 / 10  #should be 5

    number4 = 10 % 3  #should be 3
    number5 = 11 % 3  #should be 3
    number6 = 59 % 10  #should be 5

    # Correct option
    number7 = int(10 / 3)  #should be 3
    number8 = int(11 / 3)  #should be 3
    number9 = int(59 / 10)  #should be 5

    print("Number1: {}, Number2: {}, Number3: {}".format(
        number1, number2, number3))
    print("Number4: {}, Number5: {}, Number5: {}".format(
        number4, number5, number6))
    print("Number7: {}, Number8: {}, Number9: {}".format(
        number7, number8, number9))


main()
