"""Pytest based test‑suite for *smoke_math*.

A small parameterised test collection that exercises both the *add* and
*multiply* helpers with three sample inputs each.
"""

from __future__ import annotations

import pathlib
import sys

# Ensure the directory that contains *smoke_math.py* (which lives directly
# inside the *tests* directory) is on *sys.path* so that ``import smoke_math``
# works regardless of how the tests are invoked.
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import smoke_math  # noqa: E402  (import after sys.path manipulation)

import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-5, 10, 5),
    ],
)
def test_add(a, b, expected):
    """Verify *smoke_math.add*."""

    assert smoke_math.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 12),
        (0, 5, 0),
        (-2, -3, 6),
    ],
)
def test_multiply(a, b, expected):
    """Verify *smoke_math.multiply*."""

    assert smoke_math.multiply(a, b) == expected
