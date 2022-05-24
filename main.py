class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks = ['FE'], score = 0.0):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


    def change_name(self, new_name):
        if len(new_name) < 3:
            print('Name can not be less than 3 characters. Try again')
            return
        if not isinstance(new_name, str):
            print('Please enter a string as the name, and not ', type(new_name))
            return
        self.name = new_name

    def change_age(self, new_age):
        if new_age < 0:
            print('You entered a negative age. Please try again with a positive number.')
            return
        if not (isinstance(new_age, int) or isinstance(new_age, float)):
            print('Please enter a number type as the age. ')
            return
        self.age = int(new_age)

    def add_track(self, *args):
        self.tracks.extend(args)

    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())

