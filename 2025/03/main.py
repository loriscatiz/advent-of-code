from pprint import pprint


def get_input() -> list[str]:
    retval = []
    with open("input.txt") as f:
        for l in f:
            retval.append(l.strip())
    return retval


def get_map(bank: str):
    my_map = {
        "9": [],
        "8": [],
        "7": [],
        "6": [],
        "5": [],
        "4": [],
        "3": [],
        "2": [],
        "1": [],
        "0": [],
    }

    for index, joltage in enumerate(bank):
        my_map[joltage].append(index)

    return my_map


def get_first_num_and_index(my_map: dict[str, list[int]]) -> tuple[int, int]:
    for key in my_map:
        if my_map[key] != [99] and my_map[key] != []:
            val = int(key)
            index = my_map[key][0]
            return val, index
    return -1, -1


def get_second_num(my_map: dict[str, list[int]], index: int):
    for key in my_map:
        for candidate_indx in my_map[key]:
            if candidate_indx > index:
                return int(key)
    print(index)
    return -1


def first_star(data: list[str]):
    pprint("=== FIRST STAR ===")
    retval = 0
    for bank in data:
        my_map = get_map(bank)
        first_num, index = get_first_num_and_index(my_map)
        if first_num == -1 and index == -1:
            pprint("Something wrong in func get_first_num_and_index")
            return
        second_num = get_second_num(my_map, index)
        if second_num == -1:
            pprint("Something wrong in func get_second_num")
            return
        bank_joltage = (first_num * 10) + second_num
        retval += bank_joltage

    return retval


class SecondStar:
    def __init__(self, data: list[str]) -> None:
        self.data = data

    class Bank:
        def __init__(self, batteries_remaining: int, data: str) -> None:
            self.batteries_remaining = batteries_remaining
            self.data = data
            self.prev_idx = -1

        @property
        def lowest_valid_idx(self):
            return len(self.data) - self.batteries_remaining

        def _get_num(self, my_map):
            for key in my_map:
                for idx in my_map[key]:
                    if idx <= self.lowest_valid_idx and self.prev_idx < idx:
                        self.prev_idx = idx
                        return key

        def get_joltage(self):
            joltage = ""
            my_map = get_map(self.data)
            while self.batteries_remaining:
                val = self._get_num(my_map)
                joltage += str(val)
                self.batteries_remaining -= 1
            return int(joltage)

    def solution(self):
        retval = 0
        for row in self.data:
            bank = self.Bank(12, row)
            retval += bank.get_joltage()

        return retval


def main():
    data = get_input()

    first_star_result = first_star(data)
    pprint({"first_star_result": first_star_result})

    second_star = SecondStar(data)
    sol = second_star.solution()

    print(sol)


if __name__ == "__main__":
    main()
