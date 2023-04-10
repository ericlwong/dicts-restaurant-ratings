"""Restaurant rating lister."""


file = open('scores.txt')

# {'Penne For Your Thoughts' : '4'}
ratings_dict = {}
sorted_dict = {}

for line in file:
    # new line escape character : \n
    # strip(), lstrip(), rstrip()
    # will use rstrip()
    clean_line = line.rstrip()
    # will split using :
    # restaurants = ['Penne For Your Thoughts', '4']
    restaurants = clean_line.split(':')

    # tokenize
    # list[0]
    # dict['key'] = value -> if key exists, modify it else add key-value pair to dict
    # {'Penne For Your Thoughts': '4', 
    # 'Ramen On Empty': '3', 
    # 'Spaghettisburg': '3', 
    # 'Donut You Want Me Baby': '1', 
    # 'Eclair And Present Danger': '5', 
    # 'Polenta To Go Around': '2', 
    # 'In Perfect Hominy': '2', 
    # 'Ponzu Scheme': '3', 
    # 'Tamago Never Dies': '5', 
    # 'Water Pollo': '1', 
    # 'Loaf Of My Life': '3', 
    # 'Matzah-Chew-Sits': '4'}
    ratings_dict[restaurants[0]] = int(restaurants[1])

# First, print that the user has three choices
# 1. See all ratings in alphabetical order
# 2. Add a new restaurant and rating
# 3. Quit
print('You have three choices for using these restaurant ratings.')
print('1 see all ratings in alphabetical order')
print('2 add a new restaurant and rating')
print('3 Quit')
user_choice = int(input('Input your choice here as 1, 2, or 3: '))

if user_choice == 1 or user_choice == 2:
    if user_choice == 2:
        # prompt user for new restaurant and score
        new_restaurant = input('New restaurant: ')
        # while loop (loop forever until score is valid)
        invalid_score = True
        while invalid_score:
            new_score = int(input('New score (enter a score between 1 and 5): '))
            #new_score >= 1 and new_score <= 5
            if new_score < 1 or new_score > 5:
                print("Invalid score. Please try again.")
            else:
                invalid_score = False

        ratings_dict[new_restaurant] = new_score
    
    # will need .items() to get all restaurant names in a list
    # then, use sorted() (gets us a new list, so will need to assign to new var)
    restaurant_names = ratings_dict.items() #.items() returns a list of tuples
    sorted_names = sorted(restaurant_names)

    for name, rating in sorted_names:
        sorted_dict[name] = rating

    for name in sorted_dict:
        print(f"{name} is rated at {sorted_dict[name]}")
elif user_choice == 3:
    print('You are exiting the program.')

