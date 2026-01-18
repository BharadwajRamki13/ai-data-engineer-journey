class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is ', self.name)
        print('My age is ',self.age)

def main():
    person1 = Person('Bharadwaj',25)
    person1.introduce()

def main2():
    person2 = Person('Akash',23)
    person2.introduce()

if __name__ == '__main__':
    main()
    main2()