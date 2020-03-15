from django.shortcuts import render,redirect
from .models import Movies
from imdb import IMDb
import re
def MovieDetails(request):
	query=request.POST.get('urlquery')
	print(query)
	obj = obj=Movies.objects.all()
	if query:
		data=IMDb()
		movie_id=re.findall('\d+',query)
		movie=data.get_movie(str(movie_id[0]))

		title=movie['title']

		directors=movie['directors']
		dirs=','.join(map(str,directors))

		writer=movie['writers']
		writers =',\t'.join(map(str,writer))

		cast=movie['cast']
		casts =',\t'.join(map(str,cast))

		plot=movie['plot']

		rating=movie['rating']

		poster=movie['cover url']

		mov=Movies()
		mov.title=title
		mov.Director=dirs
		mov.writer=writers
		mov.cast=casts
		mov.plot=plot[0]
		mov.rating=rating
		exist=Movies.objects.filter(title=title,)
		if exist:
			return render(request,'index.html',{'obj':exist,'poster':poster})
		else:
			mov.save()
			obj=Movies.objects.filter(title=title,)
			return render(request,'index.html',{'obj':obj,'poster':poster})
	return render(request,'index.html')
		