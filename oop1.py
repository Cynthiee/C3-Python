class MyClass:
    name = input('Enter your name: ')  # class attribute
    def __init__(self, name, mat_no, dept):
        self.name = name
        self.mat_no = mat_no # instance attribute
        self.dept = dept
        
    def course(self):
        course = input('Enter your course: ') # instance attribute
        print(f'Hello, {self.name}.\nYou are studying {course}. {MyClass.name}' )
        print(f'Your mat_no is {self.mat_no}\nYour dept is {self.dept}')

        
adanna = MyClass('Adanna', 'PY12484', 'Python')
adanna.course()
#Another object
justice = MyClass('Justice', 'JS23893', 'JavaScript')
justice.course()
# Another object


a= 'yfjgjghjg'
a.casefold()