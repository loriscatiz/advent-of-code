from pprint import pprint

def get_input() -> list[dict[str, int]]:
    retval = []
    with open('input.txt') as file:
        for line in file:
            direction = line[0]
            value  = line[1:-1]
            retval.append({
                "direction": direction,
                "value": int(value)
            })
    return retval


def first_star(data: dict[str, int], current_pos=50) -> tuple[int, bool]:
    direction = 1 if data.get("direction") ==  "R" else -1
    remainings = data.get("value", 0)
    while remainings:
        remainings -= 1

        current_pos += 1 * direction
        if current_pos == -1:
            current_pos = 99

    if current_pos % 100 == 0:
        current_pos = 0

    return current_pos, not current_pos % 100


def second_star(data: dict[str, int], found_zeros=0, current_pos=50) -> tuple[int, int]:
    direction = 1 if data.get("direction") ==  "R" else -1
    remainings = data.get("value", 0)
    while remainings:
        remainings -= 1

        current_pos += 1 * direction

        if current_pos % 100 == 0:
            current_pos = 0
            found_zeros += 1

        elif current_pos == -1:
            current_pos = 99


    return current_pos, found_zeros



def main():
    data = get_input()
    current_pos = 50
    found_zeros = 0


    pprint("=== FIRST STAR ===")
    for row in data:
        current_pos, valid = first_star(row, current_pos)
        if valid:
            found_zeros += 1

    print(found_zeros)

    current_pos = 50
    found_zeros = 0
    pprint("=== SECOND STAR ===")
    for row in data:
        current_pos, found_zeros = second_star(row, found_zeros, current_pos)

    print(found_zeros)


if __name__ == "__main__":
    main()
