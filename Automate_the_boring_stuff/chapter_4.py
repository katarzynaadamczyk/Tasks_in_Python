def return_text(lst_of_things):
    if len(lst_of_things) == 1:
        return str(lst_of_things[0])
    ret = ''
    if len(lst_of_things) > 2:
        for i in lst_of_things[:len(lst_of_things) - 2]:
            ret += str(i) + ', '
    ret += str(lst_of_things[len(lst_of_things) - 2]) + ' and ' + str(lst_of_things[len(lst_of_things) - 1])
    return ret


def print_grid(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end='')
        print('')



def main():
    lst = ['apples', 'bananas', 'tofu', 'cats']
    print(lst)
    print(return_text(lst))

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['0', '0', '0', '0', '0', '.'],
            ['.', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    print_grid(grid)


if __name__ == '__main__':
    main()