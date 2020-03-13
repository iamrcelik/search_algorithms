class LinearSearch:

    def __init__(self, array, term):
        self.array = array
        self.term = term

    def Search(self):
        for x in self.array:
            if self.term == x:
                print("Number has found at index {}".format(self.array.index(x)))
                return 1


e1 = LinearSearch([5,6,3,7,9,2,4,8],9)
e1.Search()