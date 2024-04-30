import camelcase
from new_func import goods
# print(dir(camelcase.CamelCase()))

c = camelcase.CamelCase()

greet = 'hello world'
print(c.hump(greet))
print(c.stop_words)
print(c.__sizeof__)


print(goods( 'Oranges', 12))