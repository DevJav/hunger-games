import random

events  = ['run', 'supplies', 'weapon']
weights = [1, 1, 1]

selected_event = random.choices(events, weights)


