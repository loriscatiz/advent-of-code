from pprint import pprint


def get_input():
    with open("input.txt") as file:
        lines = file.readlines()

        num_of_lines = len(lines)



        sanitized_lines = []
        for line in lines:
            line = [el for el in line.split() if el.strip()]
            sanitized_lines.append(line)



        retval = [[] for _ in range(len(sanitized_lines[0]))]

        for i in range(len(sanitized_lines[0])):
            for j in range(num_of_lines):
                line = lines[j].split()
                retval[i].append(line[i])


    return retval




class FirstStar:
    def __init__(self, data: list[list[str]]) -> None:
        self.data = data
    
    def col_result(self, idx: int):
        col = self.data[idx]


        op = col.pop()



        acc = 1 if op == "*" else 0

        for num in col:
            acc = acc * int(num) if op == "*" else acc + int(num)
        return acc

    def solution(self):
        acc = 0 
        for i in range(len(self.data)):
            acc += self.col_result(i)
        return acc

class SecondStar(FirstStar):
    def col_result(self, idx: int):
        col = self.data[idx]

        op = col.pop()


        a = [[digit for digit in num] for num in col]




        acc = 1 if op == "*" else 0

        for num in col:
            acc = acc * int(num) if op == "*" else acc + int(num)
        return acc




def main():
    data = get_input()


    first_star_solution = FirstStar(data).solution()
    second_star_solution = SecondStar(data)

    second_star_solution.col_result(-1)
    print(data[-1])

    # pprint("=== FIRST STAR SOLUTION ===")
    # pprint(first_star_solution)
    # pprint("=== SECOND STAR SOLUTION ===")
    # second = SecondStar(ranges)
    # second_star_solution = second.count_fresh_ids()
    # pprint(second_star_solution)


if __name__ == "__main__":
    main()
