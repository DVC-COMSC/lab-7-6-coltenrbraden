
def getInput():
    user_input = input("Enter a list ")
    int_list = list(map(int, user_input.split()))
    return int_list


def makeReverse(numbers):
    leng = len(numbers) // 2
    end = len(numbers) - 1
    for i in range(leng):
        temp = numbers[i]
        numbers[i] = numbers[end - i]
        numbers[end - i] = temp
        
    return numbers


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
