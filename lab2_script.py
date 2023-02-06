def main():

    # Create a complex data structure
    about_me = {
        'full_name' : str("Dhaval Palanpuria"), 
    'student_id' : 10285600,
    'pizza_toppings': [
        'ONIONS',
        'PEPPERS',
        'CHICKEN'
        ],
    'movies':[
        [
            'phir hera pheri','dbs broly','joker','and the exorcist'
        ],
        [
            'action','comdey','suspense','animated','and horror'
        ]
    ]
    
    }
    print_student_name_and_id(about_me) 
    print(f'\n')
    print_pizza_toppings(about_me)
    print(f'\n')
    add_pizza_toppings(about_me,'tomatoes')
    print(f'\n')
    print_movie_genres(about_me)
    print(f'\n')
    print_movie_titles(about_me)

    # Add another movie to the data structure
    new_movie = about_me['movies'][0].append('your name')
    
# Function that prints student name and ID	
def print_student_name_and_id(about_me):
    name = about_me['full_name']
    x = about_me['full_name'].split()
    for x in about_me['full_name']:
        name2= about_me['full_name'][0:6]
    id = about_me['student_id']
    print(f'My name is {name}, but you can call me {name2}. ')
    print(f'My student ID is {id}.')
    return


    
# Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    toppings = about_me['pizza_toppings'].append(toppings)
    print(f'My pizza favourite toppings are:')
    about_me['pizza_toppings'].sort() 
    for a in about_me['pizza_toppings']:
        tppngs = a.lower()
        print(f'- {tppngs}')


    return

# Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f'My pizza favourite toppings are:')
    for a in about_me['pizza_toppings']:
        print(f'- {a}')
    return

# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    for g in about_me['movies']:
        genres = str(g)[1:-1]
        genres = genres.replace("'","")
    print(f'I like to watch {genres} movies.' )
    return 

# Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    movie_list = movie_list['movies']
    for m in movie_list:
        movie = movie_list[0:1]
        movie = str(movie)[2:-2]
        movie = movie.replace("'","")
        movie = movie.title()
    print(f'Some of my favourite movies are {movie}!')

    return
    
if __name__ == '__main__':
    main()
