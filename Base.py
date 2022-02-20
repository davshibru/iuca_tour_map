from grauf_module import *

dictinory = {
    # second

    '217': 's5',
    'library': 's4',
    'coffe room': 's12',
    'money manager': 's10',
    'cash manager': 's6',
    '214': 's16',
    '212': 's18',
    'IT office': 's20',
    '204': 's22',

    # first
    '108': 'f17',
    '111': 'f17',
    'register office': 'f16',
    'locker room': 'f15',
    'sofas' : 'f11',
    'hallway': 'f1',
    'dining room': 'f2',
    'friend zone': 'f5',
}


_from = input('Введите место откуда начинается путь - ')
_to = input('Введите место куда вам нужно добраться - ')

getPath(_from, _to)

# if _from in dictinory and _to in dictinory and _from != _to:
#     getPath(dictinory[_from], dictinory[_to])
# else:
#     if _from not in dictinory or not _to in dictinory:
#         print('Такого места нет в базе')
#     elif _from == _to:
#         print('Введите разные места')