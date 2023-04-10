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
    ratings_dict[restaurants[0]] = restaurants[1]

# prompt user for new restaurant and score
new_restaurant = input('New restaurant: ')
new_score = input('New score: ')

ratings_dict[new_restaurant] = new_score

# will need .items() to get all restaurant names in a list
# then, use sorted() (gets us a new list, so will need to assign to new var)
restaurant_names = ratings_dict.items() #.items() returns a list of tuples
sorted_names = sorted(restaurant_names)

for name, rating in sorted_names:
    sorted_dict[name] = rating

for name in sorted_dict:
    print(f"{name} is rated at {sorted_dict[name]}")

        