from utils import execute_algorithm, execute_inverted_algorithm


def main():
    print('Press 1 to execute domino algorithm',
          'Press 2 to execute inverted domino algorithm', sep='\n')
    choice = int(input())
    print("Insert domino setup: ")
    setup = list(input())
    print("Insert number of iterations: ")
    x = int(input())

    if(choice == 1):
        for i in range(x):
            setup = ''.join(execute_algorithm(setup))
        print(setup)
    elif(choice == 2):
        for i in range(x):
            setup = ''.join(execute_inverted_algorithm(setup))
        print(setup)
    else:
        print('Unknown choice')


if __name__ == "__main__":
    main()
