def main():
    movie_night = {
        'name': 'Austin Labrecque',
        'Student ID': '10266387 ',
        'pizza toppings': [
            'mushrooms',
            'sausage',
            'olives'
        ],
        'movies':[
            {
            'title': 'Lord of the Rings',
            'genre': 'Fantasy'
            },
            {'title': 'In Bruges',
            'genre': 'Comedy'
            }
        ]
    }

    new_movie = {'title': 'Eastern Promises', 'genre': 'Drama'}
    movie_night['movies'].append(new_movie)
    
    new_toppings = ('Pepperoni', 'Peppers')
    add_toppings(movie_night, new_toppings)
    
    print_strings(movie_night)
    
def add_toppings(pizza, toppers):
    for t in toppers:
     pizza['pizza toppings'].append(t)
    
def print_strings(movie_night_info):
    print('Hi Joe, my name is', movie_night_info['name']+", and my student No. is: "+movie_night_info['Student ID'])
    
    pizza_string = "My ideal pizza has "
    for x,y in enumerate(movie_night_info['pizza toppings']):
        pizza_string += y
        if x < len(movie_night_info['pizza toppings']) - 2:
            pizza_string+= ', '
        elif x < len(movie_night_info['pizza toppings']) - 1:
            pizza_string+= ', and '
        else:
            pizza_string+= '.'
    genre_string = "I like to watch "
    for i,j in enumerate(movie_night_info['movies']):
        genre_string += j['genre']
        if i < len(movie_night_info['movies']) - 2:
            genre_string+= ', '
        elif i < len(movie_night_info['movies']) - 1:
            genre_string+= ', and '
        else:
            genre_string+= ' movies.'
    fave_string = "Some of my favourites are "
    for a,z in enumerate(movie_night_info['movies']):
        fave_string += z['title']
        if a < len(movie_night_info['movies'])-2:
            fave_string+= ', '
        elif a < len(movie_night_info['movies'])-1:
            fave_string+= ', and '
        else:
            fave_string+= '.'
    print(pizza_string)
    print(genre_string)
    print(fave_string)  

main()