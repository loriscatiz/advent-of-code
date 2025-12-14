from re import split


def get_input(file_name: str) -> list[str]:
    with open(file_name) as file:
        lines = file.readlines()

    return lines


class FirstStar:
    splits = 0

    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.beams_indexes = {data[0].find("S"): True}

    def split(self, split_indexes: list[int]):
        print(split_indexes)
        for i in split_indexes:
            self.beams_indexes.update(
                {
                    i: False,
                    i + 1: True,
                    i - 1: True,
                }
            )
            self.splits += 1

    def solve(self):
        for line in self.data:
            split_indexes = []
            for idx in self.beams_indexes:
                if self.beams_indexes[idx]:
                    if line[idx] == "^":
                        split_indexes.append(idx)
            self.split(split_indexes)
        return self.splits


class SecondStar(FirstStar):
    paths = 0
    split_indexes = []

    def solve(self):
        for i, line in enumerate(self.data):
            split_indexes = []
            for idx in self.beams_indexes:
                if self.beams_indexes[idx]:
                    if line[idx] == "^":
                        split_indexes.append(idx)
            self.split(split_indexes)
            if split_indexes:
                self.split_indexes.append(split_indexes)
            print(self.split_indexes)

        for i in range(len(self.split_indexes)):
            for j in range(len(self.split_indexes[i])):
                if i > 0:
                    current = self.split_indexes[i][j]
                    if (
                        current + 1 in self.split_indexes[i - 1]
                        and current - 1 in self.split_indexes[i - 1]
                    ):
                        print("double", "current:", current, "i:", i, "j:", j)
                        self.paths += 4
                    elif (
                        current + 1 in self.split_indexes[i - 1]
                        or current - 1 in self.split_indexes[i - 1]
                    ):
                        print("single", "current:", current, "i:", i, "j:", j)
                        self.paths += 2
                else:
                    if i == 0:
                        print("first")
                        self.paths += 2

        return self.paths


def main():
    data = get_input("input.txt")
    example_data = get_input("example_input.txt")
    first = FirstStar(data)
    second = SecondStar(example_data)
    print(second.solve())


if __name__ == "__main__":
    main()
