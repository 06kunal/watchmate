# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     # created a dictionary because json response only accepts dictionary.
#     data = {
#         'movies': list(movies.values())
#     }
#     # jason response 
#     return JsonResponse(data)

# # The model contains objects. And when we do movie.objects.all(), it returns a list of objects in a complex query set. So, we convert this query set to dictionary. and this conversion is called Serialisation. So, then we render this dictionary into json.

# # So, python dictionary to complex datatype or query set -> Deserailization




# def movie_details(request, pk):
#     movie = Movie.objects.get(pk = pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
    