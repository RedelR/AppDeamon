class MovingAverage:

    FILLED: int = -1

    def __init__(self, max_items: float):
        self._values = []
        self._max_items = max_items
        self._filled = 0

    def add_value(self, new_value: float):
        if self._filled >= self._max_items:
           self._values.pop(0)
        else:
           self._filled += 1
        self._values.append(new_value)

    def moving_average(self, start: int = 0, end: int = FILLED) -> float:
        if end == self.FILLED:
            end = self._filled
        average = 0.0
        slice_size = end - start
        if slice_size > 0:
            sum = 0.0
            for i in range(start, end):
                sum += self._values[i]
            average = sum / slice_size
        return average

