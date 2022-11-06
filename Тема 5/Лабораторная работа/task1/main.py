# TODO решить с помощью list comprehension и распечатать его
import pprint

dicts = []

new_dict = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pprint.pprint(new_dict)
