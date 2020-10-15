#!/usr/bin/env
import sys
from math import ceil


class Interview:
    def boxes(self, order):
        """order ->  positive integer smaller than 101 as an input
        returns -> dict with qtys of required boxes
        common box max capacity: 3 large boxes
        """

        if not isinstance(order, int):
            raise TypeError("Order has to be positive integer")
        if order < 1:
            raise ValueError("Order has to be bigger than 0")
        if order > 100:
            raise ValueError("Order can't be bigger than 100")

        qty = {"small": 0, "medium": 0, "large": 0, "common": 0}

        if order < 4:
            qty["small"] += 1
            return qty
        if order < 7:
            qty["medium"] += 1
            return qty
        if order < 10:
            qty["large"] += 1
            return qty
        if order < 13:
            qty["medium"] += 2
            qty["common"] += 1
            return qty
        if order < 18:
            qty["large"] += 2
            qty["common"] += 1
            return qty

        qty["large"] = order // 9
        # comon box max capacity 3 large boxes -> 27 items
        qty["common"] = ceil(order / 27)

        itemsLeft = order - qty["large"] * 9

        if itemsLeft <= 0:
            return qty
        if itemsLeft > 6:
            qty["large"] += 1
            return qty
        if itemsLeft > 3:
            qty["medium"] += 1
            return qty

        qty["small"] += 1

        return qty


if __name__ == "__main__":
    obj = Interview()
    try:
        o = int(sys.argv[1])
        print(obj.boxes(o))
    except ValueError as e:
        print(e)
