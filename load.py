# Method overloading
class Shares:
    def dividend(self, share=None):
        if share is None:
            print(f'You have no shares {share}!')
        else:
            print('Your dividend is accumulating.')

stock = Shares()
stock.dividend(100)