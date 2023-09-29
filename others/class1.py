class doner:
    def __init__(self,name,id):
        self.__name = name
        self.__id = id
    def get_name(self, new_name):
        self.name = new_name
        return new_name
    def get_id(self,new_id):
        self.id = new_id
        return new_id
a_doner = doner("Utsho", "007637")
print(a_doner)
