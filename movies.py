from bs4 import BeautifulSoup
import requests
import random
# import movieposters as mp

def main_func():

	url = 'https://www.imdb.com/chart/top/'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	movie_tags = soup.select('td.titleColumn')
	inner_tags = soup.select('td.titleColumn a')
	rating_tags = soup.select('td.posterColumn span[name=ir]')

	def get_year(movie_tag):
		moviesplit = movie_tag.text.split()
		year = moviesplit[-1]  # last item
		return year

	years = [get_year(tag) for tag in movie_tags]    
	actors = [tag['title'] for tag in inner_tags]
	titles = [tag.text for tag in inner_tags]
	ratings = [float(tag['data-value']) for tag in rating_tags]
	links_all = [tag['href'] for tag in inner_tags]

	quantity = len(titles) #number of movies

	idx = random.randrange(0, quantity)
	url_movie = 'https://www.imdb.com' + links_all[idx]
	response_m = requests.get(url_movie)

	soup1 = BeautifulSoup(response_m.text, 'html.parser') #open movie page 

	tags = soup1.find_all('img')
	# string1 = str(tags[0]) #prvi image tag! by Tino
	link=tags[0]['src']

	tags2 = soup1.find_all("span", {"data-testid": "plot-xl"})

	# print(tags2)

	movie_description = tags2[0].text
	# split_it = string1.split() #aplit the image tag
	# clean_list = [item for item in split_it if 'src' in item]
	# link = "<img " + clean_list[0] + ">"


	return f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors[idx]}', link, movie_description

