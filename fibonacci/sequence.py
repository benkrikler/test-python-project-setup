from __future__ import annotations

from functools import lru_cache
from typing import List


@lru_cache
def nth_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(f"Need n >= 0, received {n}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def get_list(n_items: int) -> List[int]:
    return [nth_fibonacci(i) for i in range(n_items)]


if __name__ == "__main__":
    print("The first 10 fibonacci numbers are:")  # noqa: T201
    print(get_list(10))  # noqa: T201
