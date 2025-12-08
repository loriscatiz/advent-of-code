from pprint import pp, pprint
from time import sleep


def get_input():
    with open("input.txt") as file:
        raw = file.read()
        ranges, ids = raw.split("\n\n")
    return ranges, ids


def get_ranges(raw_ranges: str):
    raw_ranges_list: list[str] = raw_ranges.strip().split("\n")
    retval = []
    for raw_range in raw_ranges_list:
        min, max = raw_range.split("-")
        retval.append((int(min), int(max)))
    return retval


def get_ids(raw_ids: str):
    return [int(raw_id) for raw_id in raw_ids.strip().split("\n")]


class FirstStar:
    def __init__(self, ranges, ids) -> None:
        self.ranges = ranges
        self.ids = ids

    def _is_fresh_id(self, id):
        for min, max in self.ranges:
            if min <= id <= max:
                return True
        return False

    def count_fresh_ids(self):
        count = 0
        for id in self.ids:
            if self._is_fresh_id(id):
                count += 1
        return count


class SecondStar(FirstStar):
    def __init__(self, ranges: list) -> None:
        self.ranges = sorted(ranges, key=lambda r: r[0])

        merged = []

        for left_range, right_range in self.ranges:
            if not merged:
                merged.append((left_range, right_range))
                continue

            last_left_range, last_right_range = merged[-1]

            if left_range > last_right_range:
                merged.append((left_range, right_range))

            else:
                a = last_left_range if left_range > last_left_range else left_range
                b = last_right_range if right_range < last_right_range else right_range
                merged[-1] = (a, b)

        self.fresh_ids = merged

    def count_fresh_ids(self):
        count = 0
        for left, right in self.fresh_ids:
            count += right - left + 1
        return count


def main():
    raw_ranges, raw_ids = get_input()
    ranges = get_ranges(raw_ranges)
    ids = get_ids(raw_ids)

    first = FirstStar(ranges, ids)
    first_star_solution = first.count_fresh_ids()

    pprint("=== FIRST STAR SOLUTION ===")
    pprint(first_star_solution)
    pprint("=== SECOND STAR SOLUTION ===")
    second = SecondStar(ranges)
    second_star_solution = second.count_fresh_ids()
    pprint(second_star_solution)


if __name__ == "__main__":
    main()
