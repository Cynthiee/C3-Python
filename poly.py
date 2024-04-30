#Method overriding
class School:
    def message(self):
        print('Welcome to LearnFactory')

class Python(School):
    def message(self):
        print('Welcome to Python class')

class Js(School):
    def message(self):
        print('Welcome to JavaScript class')

# for super class
learnfactory = School()
learnfactory.message()

# first subclass
python = Python()
python.message()

# second subclass
js = Js()
js.message()

