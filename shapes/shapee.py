import math


class Shape:
    def __init__(
        self,
        topleft: tuple[float] = (-math.inf, math.inf),
        botright: tuple[float] = (math.inf, -math.inf),
    ):
        self.topleft = topleft
        self.botright = botright

    def __lt__(self, other):
        return self.area < other.area

    @property
    def area(self):
        raise NotImplementedError

    @property
    def horizontal_midpoint(self):
        return (self.topleft[0] + self.botright[0]) / 2

    @property
    def vertical_midpoint(self):
        return (self.topleft[1] + self.botright[1]) / 2

    def split_horizontally(self):
        assert not math.isinf(self.topleft[1]), ValueError(
            "Can't find the midpoint of infinity"
        )
        assert not math.isinf(self.botright[1]), ValueError(
            "Can't find the midpoint of infinity"
        )

        return (
            Shape(self.topleft, (self.botright[0], self.vertical_midpoint)),
            Shape((self.topleft[0], self.vertical_midpoint), self.botright),
        )

    def split_vertically(self):
        assert not math.isinf(self.topleft[1]), ValueError(
            "Can't find the midpoint of infinity"
        )
        assert not math.isinf(self.botright[1]), ValueError(
            "Can't find the midpoint of infinity"
        )

        return (
            Shape(self.topleft, (self.horizontal_midpoint, self.botright[1])),
            Shape((self.horizontal_midpoint, self.topleft[1]), self.botright),
        )
