import random
print("Heitetään kolikkoa viidesti:")
for amount in range(5):
	flip = random.randint(0, 1)
	if (flip == 0):
		print("Klaava!")
	else:
		print("Kruuna!")
