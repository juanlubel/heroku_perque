class QuickSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        a = self.data
        self._quickSort(a, 0, len(a) - 1)
        self.data = a

    def _quickSort(self, a, low, hi):
        if low < hi:
            p = self._partition(a, low, hi)
            self._quickSort(a, low, p - 1)
            self._quickSort(a, p + 1, hi)

    def _partition(self, a, low, hi):
        pivot_index = self._getPivot(a, low, hi)
        pivot_value = a[pivot_index]['buy_price']
        a[pivot_index], a[low] = a[low], a[pivot_index]
        border = low

        for i in range(low, hi + 1):
            if a[i]['buy_price'] < pivot_value:
                border += 1
                a[i], a[border] = a[border], a[i]
        a[low], a[border] = a[border], a[low]

        return border

    def _getPivot(self, a, low, hi):
        mid = (hi + low) // 2
        pivot = hi
        if a[low]['buy_price'] < a[mid]['buy_price']:
            if a[mid]['buy_price'] < a[hi]['buy_price']:
                pivot = mid
        elif a[low]['buy_price'] < a[hi]['buy_price']:
            pivot = low
        return pivot