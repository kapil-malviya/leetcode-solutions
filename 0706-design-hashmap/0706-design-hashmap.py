class MyHashMap:

    def __init__(self):
        # initialise two lists to store keys and values
        self.keys = []
        self.values = []        

    def put(self, key: int, value: int) -> None:
        # check if key already exists in the keys list
        if key in self.keys:
            
            # if it exists, find its index in keys list
            index = self.keys.index(key)
            # update corresponding value in the values list
            self.values[index] = value
        else:
            # if the key doesn't exist, add it to the keys list
            self.keys.append(key)
            # add the corresponding value to values list
            self.values.append(value)

    def get(self, key: int) -> int:
        # check if key exists in the keys list
        if key in self.keys:
            index = self.keys.index(key)
            # return the corresponding value from the values list
            return self.values[index]
        else:
            # if key doesn't exist, return -1 
            return -1

    def remove(self, key: int) -> None:
        # check if key exists in the keys list
        if key in self.keys:
            # if it exists find its index in keys list
            index = self.keys.index(key)
            
            # remove key-value pair from both lists
            del self.keys[index]
            del self.values[index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)