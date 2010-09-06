# A dictionary of movie critics and their ratings of a small set of movies 
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0}, 
 'Yong Bakos': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 
  'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
  'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 
 'Superman Returns': 3.5, 'The Night Listener': 4.0}, 
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5}, 
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5}, 
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

# Returns a linear distance based similarity score for person1 and person2
def euclidean_distance(preferences, person1, person2):
  # similar_items: a set of movies rated by both person1 and person2
  similar_items = {}
  for item in preferences[person1]:
    if item in preferences[person2]:
      similar_items[item] = 1
  if len(similar_items) == 0: return 0
  sum_of_squares = sum([pow(preferences[person1][item]-preferences[person2][item],2)
    for item in preferences[person1] if item in preferences[person2]])
  print similar_items
  return 1 / (1 + sqrt(sum_of_squares))

# Returns the Pearson correlation coefficient for person1 and person2
def pearson_correlation(preferences, person1, person2):
  # Create a list of mutually rated item keys
  similar_items = {}
  for item in preferences[person1]:
    if item in preferences[person2]: similar_items[item] = 1
  # Declare the number of elements
  num_of_elements = len(similar_items)
  # If there are no ratings in common, the correlation is 0.
  if num_of_elements == 0: return 0
  # Add up all the ratings
  person1_rating_sum = sum([preferences[person1][movie] for movie in similar_items])
  person2_rating_sum = sum([preferences[person2][movie] for movie in similar_items])
  # Sum the squares of each person's ratings
  person1_scores_squared_sum = sum([pow(preferences[person1][movie], 2) for movie in similar_items])
  person2_scores_squared_sum = sum([pow(preferences[person2][movie], 2) for movie in similar_items])
  # Sum the products of person1's and person2's ratings for all movies
  ratings_products_sum = sum([preferences[person1][movie] * preferences[person2][movie] for movie in similar_items])
  # Calculate Pearson correlation 'score'
  # p = covariance(x, y) / (stdev(x) * stdev(y))
  # pNumerator: covariance(x, y)
  # pDenominator: (stdev(x) * stdev(y))
  pNumerator = ratings_products_sum - (person1_rating_sum * person2_rating_sum / num_of_elements)
  pDenominator = sqrt((person1_scores_squared_sum - pow(person1_rating_sum, 2) / num_of_elements) *
                      (person2_scores_squared_sum - pow(person2_rating_sum, 2) / num_of_elements))
  if pDenominator == 0: return 0
  return (pNumerator / pDenominator)

# Returns the most similar ratings from the preferences dictionary for a given person.
# number_of_results and similarity_function are optional parameters.
def similar_critics(preferences, person, number_of_results = 5, similarity_function = pearson_correlation):
  scores = [(similarity_function(preferences, person, compared_person), compared_person)
                  for compared_person in preferences if compared_person != person]
  # Sort the list so the most similar person appears at the top
  scores.sort()
  scores.reverse()
  return scores[0:number_of_results]
