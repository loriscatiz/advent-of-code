from pprint import pprint

def get_input() -> list[tuple[int, int]]:
    retval = []
    with open('input.txt') as file:
        raw_data = file.readline().strip('\n')
        raw_ranges = raw_data.split(',')
        for range in raw_ranges:
            start, finish = range.split('-')
            retval.append((start, finish))
    return retval


def is_valid_id(id: str) -> bool:
    a = len(id)
    if a % 2 != 0:
        return True

    for i in range(0, a//2):
        if id[i] != id[i + (a//2)]:
            return True
    return False





def get_dividers(id: str) -> list[int]:
    """GETS THE VALID LENGHTS OF THE POSSIBLE INVALID NUMBER TO CHECK LATER"""
    dividers = []
    for i in range(1, ( len(id) // 2 ) + 1):
        if len(id) % i == 0:
            dividers.append(i)

    return dividers

def _check(id: str, divider: int):
    substr = id[:divider]

    # pprint({"id": id, "divider": divider, "substr": substr, "count": id.count(substr), "expected": len(id) / divider,})
    return id.count(substr) == int(len(id) / divider)

def check(id: str, dividers: list[int]) -> bool:
    for divider in dividers:
        if _check(id, divider):
            return True
    return False





def first_star():
    pass


def second_star():
    pass



def main():
    data = get_input()
    sum = 0



    pprint("=== FIRST STAR ===")
    # for r in data:
    #     for id in range(int(r[0]), int(r[1])):
    #         if not is_valid_id(str(id)):
    #             sum += id
    # pprint(sum)

    # data = [(1211, 1216)]


    pprint("=== SECOND STAR ===")
    for r in data:
        for id in range(int(r[0]), int(r[1])):
            dividers = get_dividers(str(id))
            if check(str(id), dividers):
                sum += id

    print(sum)



if __name__ == "__main__":
    main()
