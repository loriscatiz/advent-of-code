from pprint import pp, pprint


def get_input() -> list[list[int]]:
    retval = []
    with open("input.txt") as file:
        for line in file:
            row = []
            for char in line:
                row.append(1 if char == "@" else 0)
            retval.append(row)
    return retval


class FirstStar:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    def can_be_picked(self, x: int, y: int, treshold: int = 4):
        if self.matrix[x][y] == 0:
            return False
        count = 0

        try:
            right = self.matrix[x + 1][y]
            if right:
                count += 1
        except IndexError:
            pass

        try:
            bottom_right = self.matrix[x + 1][y + 1]
            if bottom_right:
                count += 1
        except IndexError:
            pass

        try:
            bottom = self.matrix[x][y + 1]
            if bottom:
                count += 1
        except IndexError:
            pass

        try:
            bottom_left = self.matrix[x - 1][y + 1]
            if x == 0:
                raise IndexError
            if bottom_left:
                count += 1
        except IndexError:
            pass

        try:
            left = self.matrix[x - 1][y]
            if x == 0:
                raise IndexError
            if left:
                count += 1
        except IndexError:
            pass

        try:
            up_left = self.matrix[x - 1][y - 1]
            if x == 0 or y == 0:
                raise IndexError
            if up_left:
                count += 1
        except IndexError:
            pass

        try:
            up = self.matrix[x][y - 1]
            if y == 0:
                raise IndexError
            if up:
                count += 1
        except IndexError:
            pass

        try:
            up_right = self.matrix[x + 1][y - 1]
            if y == 0:
                raise IndexError
            if up_right:
                count += 1
        except IndexError:
            pass

        return count < treshold

    def solution(self):

        count = 0
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                if self.can_be_picked(x, y):
                    count += 1
        return count


class SecondStar(FirstStar):
    total_count = 0
    coordinates_to_remove: list[tuple[int, int]] = []

    def remove_old_coordinates(self):
        for x, y in self.coordinates_to_remove:
            self.matrix[x][y] = 0

    def helper(self):
        count = 0
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                if self.can_be_picked(x, y):
                    self.coordinates_to_remove.append((x, y))
                    count += 1
        self.total_count += count
        if not count == 0:
            self.remove_old_coordinates()
            self.helper()

    def solution(self):
        self.helper()
        return self.total_count


def main():
    data = get_input()
    pprint("=== FIRST STAR SOLUTION ===")
    first_star = FirstStar(data)
    pprint(first_star.solution())
    pprint("=== SECOND STAR SOLUTION ===")
    second_star = SecondStar(data)
    pprint(second_star.solution())


if __name__ == "__main__":
    main()
