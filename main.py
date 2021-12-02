#  Annabelle Poer

team_dict = {}

i = 1

count = 1

for i in range(1,6):
    jersey_number = int(input('Enter player {}\'s jersey number: '.format(i)))

    rating = int(input('Enter player {}\'s rating: '.format(i)))

    print()

print("ROSTER")
print(team_dict)

while True:
    choice = input('MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\nChoose an option: ')

if choice == 'a':
    jersey = int(input('Enter a new player\'s jersey number: '))
    rating = int(input('Enter the player\'s rating: '))
    players[jersey] = rating

elif choice == 'u':
    jersey = int(input('Enter a jersey number: '))

