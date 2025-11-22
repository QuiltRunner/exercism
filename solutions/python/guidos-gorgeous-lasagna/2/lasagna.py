# Define EXPECTED_BAKE_TIME variable.

EXPECTED_BAKE_TIME = 40

# Define bake_time_remaining to calculate the remaining bake time in minutes. 

def bake_time_remaining(cook_time):
	"""Calculate the bake time remaining in minutes. 

	:param cook_time: expected_bake_time - int. 
	:return: the remaining bake time in minutes. 

	This functions takes two integers representing the expectated bake time and the time (in minutes) the lasagna has been baking. 
	"""

	return EXPECTED_BAKE_TIME - cook_time

# Define preparation_time_in_minutes to calculate the prep time in minutes. 

def preparation_time_in_minutes(number_of_layers):
	"""Calculate the preparation time in minutes. 

	:param number_of_layers: number of layers in the lasgana multiplied by 2 minutes.
	:return: total preparation time based on number of layers.

	This function takes two integers representing the number of lasagna layers and the time (in minutes) needed to prepare each layer.
	"""

	return number_of_layers * 2

# Define elapsed_time_in_minutes to calculate the total elapsed time in minutes. 

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
	"""Calculate the elapsed cooking time.

	:param number_of_layers: int - the number of layers in the lasagna. 
	:param elapsed_bake_time: int - elapsed cooking time. 
	:return: int - total time elapsed (in minutes) preparing and cooking. 

	This function takes two integers representing the number of lasagna layers and the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
	"""
	
	return number_of_layers * 2 + elapsed_bake_time
