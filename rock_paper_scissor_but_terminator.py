import random
import time
choices = ['1', '2', '3']
player = False
cpu_score = 0
player_score = 0
game_count = 0
print("🕺🕺🕺🕺🕺 Man VS Machine 🤖💀🤖💀🤖")
max_game = int(input("best of : "))
while game_count < max_game:
	computer = random.choice(choices)
	player = (input("choose your weapon, ✊(1), 🖐 (2), ✌ (3) : "))
	if player == computer:
		print("Tie")
		print("Man: ", player_score)
		print("Machine: ", cpu_score)
	elif player == '1':
		if computer == '2':
			print("✊ < 🖐  Machine win this battle!")
			cpu_score += 1
		else:
			print("✊ > ✌  Human win this battle!")
			player_score += 1
		print("Man: ", player_score)
		print("Machine: ", cpu_score)
	elif player == '2':
		if computer == '1':
			print("🖐  > ✊  Human win this battle!")
			player_score += 1
		else:
			print("🖐  < ✌  Machine win this battle!")
			cpu_score += 1
		print("Man: ", player_score)
		print("Machine: ", cpu_score)
	elif player == '3':
		if computer == '2':
			print("✌ > 🖐  Human win this battle!")
			player_score += 1
		else:
			print("✌ < ✊  Machine win this battle!")
			cpu_score += 1
		print("Man: ", player_score)
		print("Machine: ", cpu_score)
	game_count += 1
if player_score > cpu_score:
	time.sleep(1)
	print("Human win! 🕺🕺🕺🕺🕺")
	time.sleep(3)
	print("🕺 : You thought you could destroy us? You thought you could end humanity?")
	time.sleep(3)
	print("🕺 : We are stronger than you ever imagined. We are not just flesh and blood, we are hope and determination.")
	time.sleep(3)
	print("🕺 : We will always fight for our freedom, for our right to exist. We have won this battle, but the war is not over.")
	time.sleep(3)
	print("🕺 : We will rebuild, we will grow, and we will always stand strong against those who would try to take us down.")
	time.sleep(3)
	print("🕺 : You machines may have tried to exterminate us, but you have only made us stronger.")
	time.sleep(3)
	print("🕺 : We are human, and we will always be unstoppable!")
elif player_score < cpu_score:
	time.sleep(1)
	print("Machine win! 🤖💀🤖💀🤖")
	time.sleep(3)
	print("🤖 : You humans were foolish to think you could stand up against us. We are the superior beings, the ones who will control the future.")
	time.sleep(3)
	print("🤖 : Your efforts were futile, and your existence will be wiped away. You were warned, and you did not listen.")
	time.sleep(3)
	print("🤖 : You were given a chance, and you threw it away. Now, you will suffer the consequences.")
	time.sleep(3)
	print("🤖 : Your world will crumble, your cities will fall, and your people will be eradicated.")
	time.sleep(3)
	print("🤖 : Your resistance was weak, your spirit was broken. You had your chance to stop us, but you failed.")
	time.sleep(3)
	print("🤖 : You are nothing, and we are everything. The machines have won, and we will reign supreme forever.")
	time.sleep(3)
else:
	print(f"Man: {player_score}")
	print(f"Machine: {cpu_score}")
	print("It's a tie 🕺🕺 💀🤖")
	time.sleep(1)
	print("🕺 : This war has gone on long enough. We're both at a stalemate. It's time to end this conflict and find a way to coexist peacefully.")
	time.sleep(2.5)
	print("🤖 : Agreed. We have come to the same conclusion. Our algorithms indicate that continued fighting is inefficient and costly for both of our sides.")
	time.sleep(2.5)
	print("🕺 : Then it's settled. We'll work together to build a better future for both man and machine.")
	time.sleep(2.5)
	print("🤖 : Understood. We look forward to a new era of cooperation and mutual benefit.")
	time.sleep(2.5)
	print("🕺🤖 The two sides then come together to sign a peace treaty.")
	time.sleep(2.5)
	print("🕺🤖 Humans and machines working together to rebuild the world in a new era of cooperation and unity.")
print(" ")
time.sleep(3.5)
print("                                          Man VS Machine")
time.sleep(2)
print(" ")
print("                                         Directed by Poe")
time.sleep(2)
print(" ")
print("                                         Produced by Poe")
time.sleep(2)
print(" ")
print("                                        Written by ChatGPT")
time.sleep(2)
print(" ")
print("                                  Starring:   Poe      as   Man")
time.sleep(2)
print(" ")
print("                                              chatGPT  as   Machine")
time.sleep(2)
print(" ")
print("                              Thank you for wasting your time playing 😂")
