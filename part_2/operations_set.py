print('Operations Set')

set_environment = {'movies', 'popcorn', 'candy', 'hall'}
set_movies = {'horror', 'comedy', 'hall'}
set_ht = set_environment.union(set_movies)
print(f'Union Set = {set_ht}')

set_ht2 = set_environment | set_movies
print(f'Union Set = {set_ht2}')

set_ht3 = set_environment.intersection(set_movies)
print(f'Intersection Set = {set_ht3}')

set_ht4 = set_environment & set_movies
print(f'Intersection Set = {set_ht4}')

set_ht5 = set_environment.difference(set_movies)
print(f'Difference Set = {set_ht5}')

set_ht6 = set_environment - set_movies
print(f'Difference Set = {set_ht6}')

set_ht7 = set_environment.symmetric_difference(set_movies)
print(f'Symmetric Difference Set = {set_ht7}')

set_ht7 = set_environment ^ set_movies
print(f'Symmetric Difference Set = {set_ht7}')









