class QuickSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        a = self.data
        self._quickSort(a, 0, len(a) - 1)
        print(a)

    def _quickSort(self, a, low, hi):
        if low < hi:
            p = self._partition(a, low, hi)
            self._quickSort(a, low, p - 1)
            self._quickSort(a, p + 1, hi)

    def _getPivot(self, a, low, hi):
        mid = (hi + low) // 2
        pivot = hi
        if a[low] < a[mid]:
            if a[mid] < a[hi]:
                pivot = mid
        elif a[low] < a[hi]:
            pivot = low
        return pivot

    def _partition(self, a, low, hi):
        pivot_index = self._getPivot(a, low, hi)
        pivot_value = a[pivot_index]
        a[pivot_index], a[low] = a[low], a[pivot_index]
        border = low

        for i in range(low, hi + 1):
            if a[i] < pivot_value:
                border += 1
                a[i], a[border] = a[border], a[i]
        a[low], a[border] = a[border], a[low]

        return border