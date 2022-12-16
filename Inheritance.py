class person:

    _name = 'sudh'
    __surname = 'kumar'
    yob = 1990
    def _age(self, current_year):
        return current_year - self.yob
    def __age1(self, current_year):
        return current_year - self.yob

obj = person()


class emp(person):
    pass

obj1 = emp()
#print(obj1)
#print(obj1.yob, obj1._name)

# for private object can call using with class variable
#print(obj1._person__surname)
#print(obj1._emp__surname)