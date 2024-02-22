if __name__ == "__main__":
    with open("numbers.txt", "w") as f1:
        for num in range(5):
            f1.write(f"{num}\n")
    f2 = open("numbers_wrong.txt", "w")
    for num in range(5,10):
        if num == 7:
            f2.write("kiskutya\n")
        else:
            f2.write(f"{num}\n")
    f2.close()

    data = []
    with open("numbers.txt", "r") as f4:
        lines = f4.readlines()
        for line in lines:
            data.append(int(line.rsplit()[0]))
        data.append("kiskutya")
    try:
        sum = 0
        for element in data:
            if type(element) != int:
                raise ValueError("nem összeadható")
            else:
                sum += element



        with open("numbres.txt", "r") as f3:
            lines = f3.readlines()

    except FileNotFoundError:
        print("A fájl nem található")