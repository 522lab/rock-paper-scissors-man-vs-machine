import random
import time
choices = ['1', '2', '3']
player = False
com_score = 0
player_score = 0
game_count = 0
print("πΊπΊπΊπΊπΊ Man VS Machine πππππ")
max_game = int(input("best of : "))
while game_count < max_game:
	computer = random.choice(choices)
	player = (input("choose your weapon, β(1), π (2), β (3) : "))
	if player == computer:
		print("Tie")
		print("Man: ", player_score)
		print("Machine: ", com_score)
	elif player == '1':
		if computer == '2':
			print("β < π  Machine win this battle!")
			com_score += 1
		else:
			print("β > β  Human win this battle!")
			player_score += 1
		print("Man: ", player_score)
		print("Machine: ", com_score)
	elif player == '2':
		if computer == '1':
			print("π  > β  Human win this battle!")
			player_score += 1
		else:
			print("π  < β  Machine win this battle!")
			com_score += 1
		print("Man: ", player_score)
		print("Machine: ", com_score)
	elif player == '3':
		if computer == '2':
			print("β > π  Human win this battle!")
			player_score += 1
		else:
			print("β < β  Machine win this battle!")
			com_score += 1
		print("Man: ", player_score)
		print("Machine: ", com_score)
	game_count += 1
if player_score > com_score:
	time.sleep(1)
	print("Human win! πΊπΊπΊπΊπΊ")
	time.sleep(3)
	print("πΊ : You thought you could destroy us? You thought you could end humanity?")
	time.sleep(3)
	print("πΊ : We are stronger than you ever imagined. We are not just flesh and blood, we are hope and determination.")
	time.sleep(3)
	print("πΊ : We will always fight for our freedom, for our right to exist. We have won this battle, but the war is not over.")
	time.sleep(3)
	print("πΊ : We will rebuild, we will grow, and we will always stand strong against those who would try to take us down.")
	time.sleep(3)
	print("πΊ : You machines may have tried to exterminate us, but you have only made us stronger.")
	time.sleep(3)
	print("πΊ : We are human, and we will always be unstoppable!")
elif player_score < com_score:
	time.sleep(1)
	print("Machine win! πππππ")
	time.sleep(3)
	print("π : You humans were foolish to think you could stand up against us. We are the superior beings, the ones who will control the future.")
	time.sleep(3)
	print("π : Your efforts were futile, and your existence will be wiped away. You were warned, and you did not listen.")
	time.sleep(3)
	print("π : You were given a chance, and you threw it away. Now, you will suffer the consequences.")
	time.sleep(3)
	print("π : Your world will crumble, your cities will fall, and your people will be eradicated.")
	time.sleep(3)
	print("π : Your resistance was weak, your spirit was broken. You had your chance to stop us, but you failed.")
	time.sleep(3)
	print("π : You are nothing, and we are everything. The machines have won, and we will reign supreme forever.")
	time.sleep(3)
else:
	print(f"Man: {player_score}")
	print(f"Machine: {com_score}")
	print("It's a tie πΊπΊ ππ")
	time.sleep(1)
	print("πΊ : This war has gone on long enough. We're both at a stalemate. It's time to end this conflict and find a way to coexist peacefully.")
	time.sleep(2.5)
	print("π : Agreed. We have come to the same conclusion. Our algorithms indicate that continued fighting is inefficient and costly for both of our sides.")
	time.sleep(2.5)
	print("πΊ : Then it's settled. We'll work together to build a better future for both man and machine.")
	time.sleep(2.5)
	print("π : Understood. We look forward to a new era of cooperation and mutual benefit.")
	time.sleep(2.5)
	print("πΊπ The two sides then come together to sign a peace treaty.")
	time.sleep(2.5)
	print("πΊπ Humans and machines working together to rebuild the world in a new era of cooperation and unity.")
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
print("                              Thank you for wasting your time playing π")
