class BinarySearch:

    def __init__(self, array, n, t):

        self.array = array
        self.n = n
        self.t = t


    def orderArray(self):

        list.sort(self.array)
        return self.array

    def findElement(self):
        l = 0
        r = self.n - 1

        while l <= r:
            mid =  (l + r)/2
            mid = int(mid)
            if self.array[mid] < self.t:
                l = mid + 1
            elif self.array[mid] > self.t:
                r = mid - 1
            else:
                print("Number has found at index {}".format(mid))
                exit()


a = BinarySearch([3,2,1,4,5,7,8,6],8, 3)
a.orderArray()
a.findElement()

