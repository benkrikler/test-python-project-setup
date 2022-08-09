from __future__ import annotations

import pytest

from fibonacci.sequence import get_list, nth_fibonacci


def test_nth_fibonacci():
    assert nth_fibonacci(0) == 0
    assert nth_fibonacci(1) == 1
    assert nth_fibonacci(2) == 1
    assert nth_fibonacci(3) == 2
    assert nth_fibonacci(4) == 3
    assert nth_fibonacci(5) == 5

    assert nth_fibonacci(6) == 8
    assert nth_fibonacci(7) == 13
    assert nth_fibonacci(8) == 21
    assert nth_fibonacci(9) == 34
    assert nth_fibonacci(10) == 55
    assert nth_fibonacci(11) == 89

    with pytest.raises(ValueError):
        nth_fibonacci(-1)


def test_get_list():
    values = get_list(12)
    assert len(values) == 12
    assert values == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
