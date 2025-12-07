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


def check(id: str, steps: int) -> bool:
    if not int(id) % steps:
        return False

    x = []
    for i in range(steps):
        start = (i * steps)
        x.append(id[start:steps])



def is_valid_id_two(id: str) -> bool:
    steps = 1
    while steps < (len(id) // 2):
        for i in range(len(id) // 2 + 1):
            if id[i] == id[i + steps]:
                print(id)
                print("found match")
                check(id, steps)
        steps += 1






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



    pprint("=== SECOND STAR ===")
    for r in data[:4]:
        for id in range(int(r[0]), int(r[1])):
            is_valid_id_two(str(id))



if __name__ == "__main__":
    main()
