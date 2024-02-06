# Ex 1
def print_highly_rated_movie(movie):
    if movie["imdb"] > 5.5:
        print(movie["name"], " - True")
    else:
        print(movie["name"], " - false")
        
# Ex 2
def sublist(movies):
    goodmovies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            goodmovies.append(movie["name"])
    print(goodmovies)

# Ex 3
def names(movies):
    for movie in movies:
        print(movie["name"])
        
# Ex 4
def average_score(movies):
    average = 0
    for movie in movies:
        average+=movie["imdb"]
    print(average/len(movies))

# Ex 5
def average_category(category):
    average = 0
    count = 0
    for movie in movies:
        if movie["category"] == category:
            count += 1
            average+=movie["imdb"]
    print(average / count, category )   
        
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]               
for movie in movies:
    print_highly_rated_movie(movie)
    
sublist(movies)

names(movies)

average_score(movies)

categories = set(movie["category"] for movie in movies)
for category in categories:
    average_category(category)
