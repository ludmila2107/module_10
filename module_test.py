calls = 0
def count_calls():
	global calls
	calls += 1

def string_info(string):
	count_calls()
	lens_ = len(string)
	upper_ = string.upper()
	lower_ = string.lower()
	return (lens_, upper_, lower_)
def is_contains(string, list_to_search):
	count_calls()
	string = string.lower()
	list_ = []
	for i in list_to_search:
		i = i.lower()
		list_.append(i)

	if string in list_:
		return True
	else:
		return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
#
