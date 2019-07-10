from sys import exit
import random
import pickle
import os

# This function is called when game start new, player will select name and select stat to addd
# bonus point. Player stat will be generated randomly
def char_create():
	char = {}

	# creat list for character info
	char['name'] = raw_input("Before you start your quest, could you tell me your name? > ")
	char['str'] = random.randint(5,15)
	char['int'] = random.randint(5,15)
	char['lck'] = random.randint(5,15)
	char['vit'] = random.randint(5,15)

	formatter = "I see, your name is: %s\nAnd here is your stat:\nSTR:%d\nINT:%d\nLCK:%d\nVIT:%d\n"
	print formatter % (char['name'], char['str'], char['int'], char['lck'], char['vit'])
	bonus_point_total = 5
	print """With this stat, you may found it difficult in your adventure, so let me give you some power up.
I will give you %d bonus point, please select stat you want to power up or you can skip this gift""" % bonus_point_total
	print "Ex: str 2 => add 2 point to str"
	print "Ex: skip => not add bonus stat"
	
	while bonus_point_total > 0:
		bonus = raw_input("> ").split()
		stat_name = bonus[0]
		if "skip" in bonus[0]:
			print "I see, you don't need any help, I like that spirit of your."
			break
		elif (len(bonus) == 2 and not(char.get(stat_name) is None)): 
			add_amount = int(bonus[1])
			if (bonus_point_total - add_amount) < 0:
				print "You don't have enough bonus point, please choose again"
			else: 
				char[stat_name] += add_amount
				bonus_point_total -= add_amount
				print "You add %d point to %s, You remain %d point" % (add_amount, stat_name, bonus_point_total)
		else:
			print "I don't understand what you mean, please choose again"
	
	char['lvl'] = 1
	char['exp'] = 0
	
	char['hp'] = char['str'] * 10
	char['phy_atk'] = char['str'] * 2
	char['phy_def'] = char['str'] * 1

	char['mp'] = char['int'] * 10
	char['mag_atk'] = char['int'] * 2
	char['mag_def'] = char['int'] * 1

	print "Good luck on your quest"

	return char


# display character information
def display_info(char):
	formatter = """Name:%s		| Lvl: %d
-------------------------------------
STR:%d		| HP: 		%d
INT:%d		| MP: 		%d
LCK:%d		| Phy.Atk: 	%d
VIT:%d		| Phy.Def:	%d
      		| Mag.Atk: 	%d
      		| Mag.Def:	%d
	"""
	print formatter % (char['name'], char['lvl'], char['str'], char['hp'],
					char['int'], char['mp'], char['lck'], char['phy_atk'],
					char['vit'], char['phy_def'], char['mag_atk'], char['mag_def'])

# get word from line of look up file
def get_random_word(fp, word_1, word_2):
	lines = fp.readlines()
	max_line = len(lines)
	out_word_1 = ""
	out_word_2 = ""
	# check if generate word is same as previous word
	while True:
		ran_num_1 = random.randint(0, max_line)
		ran_num_2 = random.randint(0, max_line)
		out_words_1 = lines[ran_num_1]
		out_words_2 = lines[ran_num_2]
		out_word_1 = out_words_1.split()
		out_word_2 = out_words_2.split()
 		if (word_1 + word_2) != (out_word_1 + out_word_2) and (word_1 + word_2) != (out_word_1 + out_word_2) : 
			break
	return out_word_1 , out_word_2

# creating story line
def story_making(game_diff):

	# item list and boss name list
	item_list = {}
	boss_list = {}
	condition_number = 0
	
	# print the open line
	print "-"*100
	print """Greeting brave adventurer.Finally you have found your way to here, the greatest dungeon of the world. 
Currently, the world is at the edge of destruction. Evil creatures are roaming everywhere, threaten life of 
thousand inocent people. However, there still some hope for mankind, lie within this dungeon, there is an acient 
ritual, which is said to be able to seal the darknest. 
"""
	if 1 <= game_diff <= 3:
		print "In order to perform this ritual, you need following items:"
		condition_number = random.randint(game_diff + 2, game_diff + 3)
		name_format = "%s of %s"
		word_1 = "aaa"
		word_2 = "bbb"
		for i in range(0,condition_number):
			# open look up file
			fp = open("noun")
			word_1,word_2 = get_random_word(fp, word_1, word_2)
			item_list[i] = name_format % (word_1, word_2)
			print "+ %s" % item_list[i]
			fp.close()
	elif 4 <= game_diff <= 6:
		condition_number = random.randint(game_diff + 3, game_diff + 5)
		item_num = random.randint(2, condition_number)
		boss_num = condition_number - item_num
		print "condition: %d, item: %d, boss: %d" % (condition_number,item_num,boss_num)
		name_format = "%s of %s"
		word_1 = "aaa"
		word_2 = "bbb"
		word_3 = "ccc"
		word_4 = "ddd"
		print "In order to perform this ritual, need following items:"
		for i in range(0,condition_number):
			# open look up file
			fp = open("noun")
			word_1,word_2 = get_random_word(fp, word_1, word_2)

			if i == item_num:
				print """\nHowever, after you collect all the ingredients, you also need to kill some monster so that you can 
start the ritual. They are: 
"""
			if i > item_num - 1:
				fp_v = open("verb")
				word_3,word_4 = get_random_word(fp_v, word_3, word_4)
				name_format = "%s The %s %s"
				fp_v.close()
				boss_list[i - item_num] = name_format % (word_1, word_2, word_3)
				print "+ %s" % boss_list[i - item_num]
			else:
				item_list[i] = name_format % (word_1, word_2)
				print "+ %s" % item_list[i]
				
			fp.close()
	elif 7 <= game_diff <= 10:
		condition_number = random.randint(game_diff + 5, game_diff + 7)
		boss_num = random.randint(2, condition_number)
		item_num = condition_number - boss_num
		print "condition: %d, item: %d, boss: %d" % (condition_number,item_num,boss_num)
		name_format = "%s The %s %s"
		word_1 = "aaa"
		word_2 = "bbb"
		word_3 = "ccc"
		word_4 = "ddd"
		print "In order to perform this ritual, you need to kill the demon that guard the seal to the ritual. It name is: "
		for i in range(0,condition_number):
			# open look up file
			fp = open("noun")
			word_1,word_2 = get_random_word(fp, word_1, word_2)

			if i == boss_num:
				print """\nHowever, this demon is very power full, normal weapon can not harm it. You need to seek 
the sacred item so that you can weaken it. They are: 
"""
			if i > boss_num - 1:
				name_format = "%s of %s"
				item_list[i - boss_num] = name_format % (word_1, word_2)
				print "+ %s" % item_list[i - boss_num]
			else:
				fp_v = open("verb")
				word_3,word_4 = get_random_word(fp_v, word_3, word_4)
				fp_v.close()
				boss_list[i] = name_format % (word_1, word_2, word_3)
				print "+ %s" % boss_list[i]
				if i == 0:
					print "And it is protected by other monster which you need to slay before hand. They are: "
				
			fp.close()
	print "-"*100
	return condition_number, item_list, boss_list
	
# save game progress
def save_game(char,condition_number, item_list, boss_list):
	save_dir = "./save/"
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)
	save_name = raw_input("Please enter save name: >")
	

	# check save name exist, ask player want to overwrite or not
	while os.path.exists(save_dir + save_name): 
		choice = raw_input("Save already exits. Do you want to overwrite? (y/n) > ")
		if choice == "y":
			break
		elif choice == "n":
			save_name = raw_input("Please enter other save name: > ")
	if not os.path.exists(save_dir + save_name):
		os.makedirs(save_dir + save_name)
	# save player info
	fp_save_char = open(save_dir + save_name + "/char.pkl","wb")
	pickle.dump(char, fp_save_char)
	fp_save_char.close()

	# save item info
	fp_save_item = open(save_dir + save_name + "/item.pkl","wb")
	pickle.dump(item_list, fp_save_item)
	fp_save_item.close()

	# save boss info
	fp_save_boss = open(save_dir + save_name + "/boss.pkl","wb")
	pickle.dump(boss_list, fp_save_boss)
	fp_save_boss.close()

# load game data
def load_game():
	save_dir = "./save/"
	save_name = os.listdir(save_dir)
	print "Your save files are: "
	for i in save_name:
		print i
	save_name_select = raw_input("Please select your save > ")
	fp_load_char = open(save_dir + save_name_select + "/char.pkl","rb")
	char = pickle.load(fp_load_char)
	fp_load_char.close()

	fp_load_item = open(save_dir + save_name_select + "/item.pkl","rb")
	item_list = pickle.load(fp_load_item)
	fp_load_item.close()

	fp_load_boss = open(save_dir + save_name_select + "/boss.pkl","rb")
	boss_list = pickle.load(fp_load_boss)
	fp_load_boss.close()

	condition_number = len(item_list) + len(boss_list)

	while True:
		game_control(char,condition_number, item_list, boss_list)
		
# generate map and control the game
def game_control(char,condition_number, item_list, boss_list):
	action = raw_input("What is your action? > ")
	if action == "stat":
		# display player stat
		display_info(char)
	elif action == "main menu": 
		# move to main menu, ask player to enter save name to resume when player choose load game
		print "You're changing to the main menu, your progress will be save."
		save_game(char,condition_number, item_list, boss_list)
		main_menu()


# flow of new game: select diff, create char, create story, start game
def new_game():
	game_diff = 11
	# game level is only < 10
	while game_diff > 10:
		game_diff = int(raw_input("Select difficulty level (1->10) > "))
		if game_diff > 10:
			print "Incorrect input, please select from 1 -> 10" 

	condition_number, item_list, boss_list = story_making(game_diff)
	char = char_create() # call character creation
	condition_met = False
	while True: 
		game_control(char,condition_number, item_list, boss_list)

def main_menu():
	print """  Welcome to Dungeon Venture v1.0
	Please choose your action:
	> 1. New game
	> 2. Load game
	> 3. Quit
"""
	while True:
		slect = raw_input("> ")
		if slect == "1":
			new_game()
		elif slect == "2":
			load_game()
		else:
			quit = raw_input("Wrong input, quit game?(y/n) > ")
			if quit == "y":
				exit(0)
main_menu()


