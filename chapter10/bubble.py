


def bubble_sort(unordered_list):
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp

def main():
    unordered_list = [5, 2]
    i = 0
    first_element = unordered_list[0]
    second_element = unordered_list[1]

    temp = unordered_list[0]
    unordered_list[0] = unordered_list[1]
    unordered_list[1] = temp

    print(unordered_list)
    """########################################################################################"""


    my_list = [4,3,2,1]
    bubble_sort(my_list)
    print(my_list)

    my_list = [1,2,3,4]
    bubble_sort(my_list)
    print(my_list)

if __name__ == "__main__":
    main()