import codecs
import numpy as np
from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    distancia = 0
    c_Ratings = False 
    for key in rating1:
        if key in rating2:
            distancia += abs(rating1[key] - rating2[key])
            c_Ratings = True
    if c_Ratings:
        return distancia
    else:
        return -1 

def euclidean(rating1, rating2):
	distancia = 0
	c_Ratings = False
	for key in rating1:
		if key in rating2:
			distancia += pow(abs(rating1[key]-rating2[key]),2)
			c_Ratings = True
	if c_Ratings:
		return pow(distancia,1/2)
	else:
		return -1



def minkowski(rating1,rating2,r):
	distancia = 0
	c_Ratings = False
	for key in rating1:
		if key in rating2:
			distancia += pow(abs(rating1[key] - rating2[key]),r)
			c_Ratings = True
	if c_Ratings:
		return pow(distancia, 1/r)
	else:
		return -1	


def vecinoCercano(username, users):
	distances=[]
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
			distances.append((distance, user))
	distances.sort()
	return distances

def recomendar(username, users):
	cercano=vecinoCercano(username, users)[0][1]
	recomendar=[]
	ratingVecino=users[cercano]
	userRating=users[username]
	for art in ratingVecino:
		if not art in userRating:
			recomendar.append((art,ratingVecino[art]))
	return sorted(recomendar, key=lambda artTuple: artTuple[1], reverse = True)


def pearson(rating1, rating2):
	sum_xy= 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0
	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x*y
			sum_x += x
			sum_y += y
			sum_x2 += x**2
			sum_y2 += y**2
	if n == 0:
		return 0
	denominator = sqrt(sum_x2 - (sum_x**2)/n)*sqrt(sum_y2 - (sum_y**2)/n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y)/n)/denominator


def loadDatabase(path=''):
    """"loads the music dataset"""
    
    data={}

    f=codecs.open(path+"Movie_Ratings.csv",'r','utf8')

    lineset = [line for line in f]


    users = lineset[0].split(',')
    for i in range(len(users)):
        users[i]=users[i].strip('\n').strip('"')

    for i in range(1,len(lineset)):
        fields = lineset[i].split(',')
        book = fields[0].strip('"')

        currentRatingB={}
        for j in range(1,len(fields)):
            if users[j].strip('"') in data:
                currentRating=data[users[j].strip('"')]
            else:
                currentRating={}
            if fields[j].strip().strip('"'):
                currentRating[book]=float(fields[j].strip().strip('"'))
                data[users[j].strip('"')] = currentRating

    f.close()
    return data

data=loadDatabase()

#print(manhattan(users['Hailey'], users['Veronica']))#banda de musica
#print(euclidean(data['Stephen'],data['Amy']))#movies
#print(euclidean(data['278833'], data['278858']))
print(vecinoCercano('Valerie', data))

#print(pearson(users['Angelica'], users['Bill']))
#print(recomendar('Patrick C', data))

#print(users)
#print(manhattan(users['Hailey'], users['Veronica']))
#print(euclidean(users['Hailey'], users['Jordyn']))
#print(minkowski(users['Angelica'], users['Bill'],1))
#print(minkowski(users['Angelica'], users['Bill'],2))
#print(minkowski(users['Hailey'], users['Jordyn'],1))
#print(minkowski(users['Hailey'], users['Jordyn'],2))
















