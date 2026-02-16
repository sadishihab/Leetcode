class SegmentTree:
    def __init__(self, size, func=max, default=0):
        """
        size   : maximum number of elements
        func   : function for range query (max, sum, min)
        default: default value (0 for sum/max, inf for min)
        """
        self.size = size
        self.tree = [default] * (4 * size)
        self.func = func
        self.default = default

    def update(self, index, value, node=1, start=1, end=None):
        if end is None:
            end = self.size

        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2

        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)

        self.tree[node] = self.func(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left, right, node=1, start=1, end=None):
        if end is None:
            end = self.size

        # no overlap
        if right < start or left > end:
            return self.default

        # total overlap
        if left <= start and end <= right:
            return self.tree[node]

        # partial overlap
        mid = (start + end) // 2
        left_result = self.query(left, right, 2 * node, start, mid)
        right_result = self.query(left, right, 2 * node + 1, mid + 1, end)
        return self.func(left_result, right_result)
