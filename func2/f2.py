# Dictionary of movies

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


def ScoreAbove5_5(movieName):
    for i in movies:
        if i["name"] == movieName and i["imdb"] > 5.5:
            imdbScore = True
        else:
            imdbScore = False
    return imdbScore
print("What is the name of the movie?")
movieName = input()
print("This movie's IMDB score is above 5.5")
print(ScoreAbove5_5(movieName))

def list5_5(movies):
    newlistabove = []
    for i in movies:
        if i["imdb"] > 5.5:
            newlistabove.append(i["name"])
    return newlistabove
print("Movies with the score above 5.5:")
print(list5_5(movies))

def ScoreUnder5_5(categoryMovie):
    newlistunder = []
    for i in movies:
        if i["category"] == categoryMovie and i["imdb"] < 5.5:
            newlistunder.append(i["name"])
    return newlistunder
print("What is the category of the movies?")
categoryMovie = input()
s1 = "Movies in category {} with score under 5.5:"
print(s1.format(categoryMovie))
print(ScoreUnder5_5(categoryMovie))

def moviesAverageScore(movies):
    movies_scores = []
    for i in movies:
        score = i["imdb"]
        movies_scores.append(score)
    movieAveScore = sum(movies_scores)/len(movies_scores)
    return movieAveScore
print(moviesAverageScore(movies))

def categoryAverageScore(movies):
    category_score = []
    for i in movies:
        if i["category"] == categoryMovie:
            score = i["imdb"]
            category_score.append(score)
    categoryAveScore = sum(category_score)/len(category_score)
    return categoryAveScore
    
print("What is the category of the movies?")
categoryMovie = input()
s1 = "Average score of the movies in category {} is {}:"
ave = categoryAverageScore(movies)
print(s1.format(categoryMovie, ave))