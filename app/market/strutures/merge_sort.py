class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self._merge_sort2(self.data, 0, len(self.data) - 1)

    def _merge_sort2(self, a, first, last):
        if first < last:
            middle = (first + last) / 2
            self._merge_sort2(a, first, middle)
            self._merge_sort2(a, middle + 1, last)
            self._merge(a, int(first), int(middle), int(last))

    def _merge(self, a, first, middle, last):
        left = a[first:middle + 1]
        right = a[middle + 1:last + 1]
        left.append({"buy_price": 9999999})
        right.append({"buy_price": 9999999})
        i = j = 0
        for k in range(first, last + 1):
            if left[i]['buy_price'] <= right[j]['buy_price']:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
