"""
A very simple simulator of the Monty Hall problem, with the possibility to set whether to switch doors at the end and how many simulations that are to be run. Displays the result at the end.

Author: Victor Nilsson
Date: 2021-08-07
Github: vanilsson
"""

import random


def monty_hall_sim(switch: bool) -> bool:
	"""
	Simulates the scenario described in the Monty Hall problem.
	
	:param switch: If a switch of doors it to be done at the end.
	:return: If the correct door was selected in the end.
	"""
	possible_doors = {1, 2, 3}
	winning_door = random.randint(1, 3)
	chosen_door = random.randint(1, 3)
	
	doors_to_open = possible_doors ^ {winning_door, chosen_door}  # Symmetric difference, i.e. the elements not contained in both sets.
	
	open_door = random.choice(tuple(doors_to_open))
	
	(switch_door,) = possible_doors ^ {open_door, chosen_door}
	
	if switch and switch_door == winning_door:
		return True
	elif not switch and chosen_door == winning_door:
		return True
	else:
		return False


tries = 100000  # Number of Monty Hall problem simulations to run.
switch = True  # Whether to switch doors at the end.
wins = [win for win in [True] * tries if monty_hall_sim(switch)]  # Length of the list is the number of times the function monty_hall_sim returns True (i.e. that the correct door was chosen).
convert_to_percent = 100 / tries

print(f"Number of wins in scenario where option to switch is set to {switch} is {len(wins)} out of {tries}, percentage = {round(convert_to_percent * len(wins), 2)} %")
