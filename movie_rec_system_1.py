dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user = {"kgf", "zero", "superman", "batman", "evil dead", "sultan",
          "golmaal", "krrish", "bala"}

#scores = {"action":0.33, "comedy":20...} using jaccard distance formula
#find the genre with max score
#recommend movies from that genre which has max score and user has not watched those movies yet...

scores = {}
for item in dataset:
    movies = set(dataset[item])
    intersection = user.intersection(movies)
    union = user.union(movies)
    dist = len(intersection) / len(union)
    scores[item] = round(dist,2)

print(scores)

category = max(scores, key=scores.get)

recommendedMovies = set(dataset[category]) - user
print(recommendedMovies)


















