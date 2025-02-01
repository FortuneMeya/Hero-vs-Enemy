class Map:
    _instance = None
    _initialized = False


    def __new__(cls):
        # if _instance is not instantiated yet, create the instance and set it
        if cls._instance is None:
            cls._instance = super().__new__(cls)


        return cls._instance


    def __init__(self):
        if not self._initialized:
            file = open("map.txt")
            self._map = []
            for row in file:
                self._list = []
                for item in row:
                    if item != ' ' and item != '\n':
                        self._list.append(item)
                self._map.append(self._list)


            self._revealed = []
            for i in range(len(self._map)):
                self._list2 = []
                for j in range(len(self._map)):
                    self._list2.append(False)
                self._revealed.append(self._list2)


            self._initialized = True


    def __getitem__(self, row):
        return self._map[row]


    def __len__(self):
        return len(self._map)


    def show_map(self, loc):
        for i in range(len(self._map)):
            for j in range(len(self._map[i])):
                if i == loc[0] and j == loc[1]:
                    print("*", end=" ")
                elif self._revealed[i][j]:
                    print(self._map[i][j], end=" ")
                else:
                    print("x", end=" ")
            print()


        return None


    def reveal(self, loc):
        self._revealed[loc[0]][loc[1]] = True


    def remove_at_loc(self, loc):
        self._map[loc[0]][loc[1]] = 'n'
