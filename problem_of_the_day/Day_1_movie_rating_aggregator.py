def avg_ratings(reviews):
    average = {}
    for review in reviews:
        if(review["movie"] in average):
            average[review["movie"]] = (average[review["movie"]] + review["rating"])/2

        else:
            average[review["movie"]] = review["rating"]

    return average

def top_rated(reviews):
    highest = {}
    max = 0
    for review in reviews:
        if((review["rating"]) > max):
            max = int(review["rating"])
    for review in reviews:
        if(review["rating"] == max):
            highest[review["movie"]] = max

    return highest
def must_watch(average):
    mustwatch = {"mustwatch": []}
    i = 0
    for key, value in average.items():
        if value >= 8.5:
            mustwatch['mustwatch'].append(key)
    
    return mustwatch
def user_favs(reviews):
    favmovie = {}
    for review in reviews:
        if(review["user"] in favmovie):
            if(review["rating"] > favmovie[review["user"]][1]):
                favmovie[review["user"]] = (review["movie"], review["rating"])
        else:
            favmovie[review["user"]] = review["movie"], review["rating"]

    return favmovie

def main():
    reviews = [
    {"movie": "Inception",  "user": "alice", "rating": 9},
    {"movie": "Dune",       "user": "bob",   "rating": 8},
    {"movie": "Inception",  "user": "bob",   "rating": 7},
    {"movie": "Interstellar","user":"alice",  "rating": 10},
    {"movie": "Dune",       "user": "charlie","rating": 9},
    {"movie": "Interstellar","user":"charlie","rating": 8},
    ]
    average = avg_ratings(reviews)
    print(f"{avg_ratings(reviews)}")
    print(f"{top_rated(reviews)}")
    print(f"{must_watch(average)}")
    print(f"{user_favs(reviews)}")




main()