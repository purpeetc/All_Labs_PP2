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


#1 function imdb above 5.5
def imdb_rating(movies):
    if(list(filter(lambda x: x["imdb"] > 5.5, movies))):
        return True
    
print(imdb_rating(movies))


#2 function imdb above 5.5 list
def imdb_rating_list(movies):
    return list(filter(lambda x: x["imdb"] > 5.5, movies))

print(imdb_rating_list(movies))


#3 function for find category
def find_category(movies, category):
    return list(filter(lambda x: x["category"] == category, movies))

print(find_category(movies, "Romance"))


#4 function list of movies average imdb
def average_imdb(movies):
    return sum([x["imdb"] for x in movies]) / len(movies)

print(average_imdb(movies))


#5 function for find average imdb in this category
def average_imdb_category(movies):
    categories = list(set([x["category"] for x in movies]))
    for category in categories:
        movies_category = find_category(movies, category)
        print(f"Average imdb rating for {category}: {average_imdb(movies_category)}")

average_imdb_category(movies)
