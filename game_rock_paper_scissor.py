rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Trophy = '''
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
          jgs  _/_______\_
              /___________\
'''

Robot = '''
                                  _____
                                 |     |
                                 | | | |
                                 |_____|
                           ____ ___|_|___ ____
                          ()___)         ()___)
                          // /|           |\ \\
                         // / |           | \ \\
                        (___) |___________| (___)
                        (___)   (_______)   (___)
                        (___)     (___)     (___)
                        (___)      |_|      (___)
                        (___)  ___/___\___   | |
                         | |  |           |  | |
                         | |  |___________| /___\
                        /___\  |||     ||| //   \\
                       //   \\ |||     ||| \\   //
                       \\   // |||     |||  \\ //
                        \\ // ()__)   (__()
                              ///       \\\
                             ///         \\\
                           _///___     ___\\\_
                          |_______|   |_______|
'''

#Write your code below this line 👇
import random

player_choice = input(print(f"Choose 1 for rock, 2 for paper or 3 for scissor, good luck!"))
machine_choice = random.randint(1, 3)
if player_choice == "1" and machine_choice == 1:
    print(f"Bouth rock\n{rock}\n Draw.")
elif player_choice == "1" and machine_choice == 2:
    print(f"You\n{rock} Machine\n{paper}\n Machine Wins {Robot}")
elif player_choice == "1" and machine_choice == 3:
    print(f"You\n{rock} Machine\n{scissor}\n You Win {Trophy}.")
elif player_choice == "2" and machine_choice == 1:
    print(f"You\n{paper} Machine\n{rock}\n You Win {Trophy}.")
elif player_choice == "2" and machine_choice == 2:
    print(f"Bouth paper\n{paper}\n Draw.")
elif player_choice == "2" and machine_choice == 3:
    print(f"\nYou\n{paper} Machine\n{scissor}\n Machine Wins {Robot}.")
elif player_choice == "3" and machine_choice == 1:
    print(f"\nYou\n{scissor} Machine\n{rock}\n Machine Wins {Robot}.")
elif player_choice == "3" and machine_choice == 2:
    print(f"\nYou\n{scissor} Machine\n{paper}\n You Win {Trophy}.")
elif player_choice == "3" and machine_choice == 3:
    print(f"Bouth scissor\n{scissor}\n Draw.")
else:
    print("Escolha uma das opções.")
