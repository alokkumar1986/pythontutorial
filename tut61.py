class Num():
    __count =0
    def add(self, count):
        self.__count = count+1

        print(self.__count)
    def show(self):
        pass
        # print(__count)

n = Num()
count = 10
n.add(count)
