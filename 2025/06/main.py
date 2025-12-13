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
    thing = []

    def col_result(self, idx: int):
        col = self.data[idx]
        # print(col)

        digits = max(len(s) for s in col)

        op = col[-1]

        nums = []
        for i in range(digits):
            tmp_num = ""
            for num in col[:-1]:
                num = num[::-1]
                # print(i, num, col)
                try:
                    tmp_num += (str(num))[i]
                # print(tmp_num)
                except IndexError:
                    continue
                # print(tmp_num)
            if tmp_num:
                nums.append(int(tmp_num))

        print(op, nums)
        acc = 1 if op == "*" else 0
        for num in nums:
            acc = acc * int(num) if op == "*" else acc + int(num)

        return acc


def main():
    data = get_input()

    second_star = SecondStar(data)

    # for i in range(3, 6):
    #     print(second_star.data[-i])
    #     print(second_star.col_result(-i))
    print(second_star.solution())


if __name__ == "__main__":
    main()
