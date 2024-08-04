calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    cortege = (len(string)
               , string.upper()
               , string.lower())
    count_calls()
    return cortege


def is_contains(string, list1=[]):
    count_calls()
    list2 = []
    for i in list1:
        list2.append(i.lower())

    string2 = string.lower()
    if string2 in list2:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
