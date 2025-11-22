# Define EXPECTED_BAKE_TIME variable.

EXPECTED_BAKE_TIME = 40

# Define bake_time_remaining to calculate the remaining bake time in minutes. 

def bake_time_remaining(cook_time):
	return EXPECTED_BAKE_TIME - cook_time

# Define preparation_time_in_minutes to calculate the prep time in minutes. 

def preparation_time_in_minutes(number_of_layers):
	return number_of_layers * 2

# Define elapsed_time_in_minutes to calculate the total elapsed time in minutes. 

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
	return number_of_layers * 2 + elapsed_bake_time
