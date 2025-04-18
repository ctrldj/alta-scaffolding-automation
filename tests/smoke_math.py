"""Simple math utility functions with a tiny self‑test harness.

This module defines:
    add(a, b)        -> a + b
    multiply(a, b)   -> a * b

If the file is executed as a script (``python smoke_math.py``) it will run a
handful of assertions against the two functions and print a short summary. The
module contains *no* external dependencies, so it is safe to execute in any
environment that has a standard Python interpreter.
"""

from __future__ import annotations


def add(a: float | int, b: float | int):
    """Return the sum of *a* and *b*."""

    return a + b


def multiply(a: float | int, b: float | int):
    """Return the product of *a* and *b*."""

    return a * b


def _self_test() -> tuple[int, int]:
    """Run a very small set of self‑tests.

    Returns
    -------
    tuple[int, int]
        (<number of passed tests>, <total number of tests>)
    """

    test_vectors = {
        "add": [
            (1, 2, 3),
            (0, 0, 0),
            (-5, 10, 5),
        ],
        "multiply": [
            (3, 4, 12),
            (0, 5, 0),
            (-2, -3, 6),
        ],
    }

    passed = 0
    total = 0

    for a, b, expected in test_vectors["add"]:
        total += 1
        if add(a, b) == expected:
            passed += 1

    for a, b, expected in test_vectors["multiply"]:
        total += 1
        if multiply(a, b) == expected:
            passed += 1

    return passed, total


if __name__ == "__main__":
    passed, total = _self_test()
    status = "PASSED" if passed == total else "FAILED"
    print(f"Self‑test {status}: {passed}/{total} assertions succeeded.")
