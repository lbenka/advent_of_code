from typing import List
from collections import Counter


def get_input() -> List[str]:
    with open("in.txt", "r") as f:
        return f.read()


def anyone():
    all_groups = []

    for g in get_input().split("\n\n"):
        all_groups.append(len(Counter(g.replace("\n", ""))))

    # 6683
    return sum(all_groups)


def everyone():
    all_groups = []

    for g in get_input().split("\n\n"):
        group_size = (Counter(g.strip()).get("\n", 0)) + 1
        group = Counter(g.replace("\n", ""))

        group_for = len([v for v in group.values() if v >= group_size])
        # group_lam = len(list(filter(lambda x: x > 1, group.values())))

        all_groups.append(group_for)
    # 3122
    return sum(all_groups)


if __name__ == "__main__":
    result = anyone()
    print(f"anyone {result}")

    result = everyone()
    print(f"everyone {result}")
