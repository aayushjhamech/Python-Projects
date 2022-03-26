import flask
from pymongo import MongoClient

try:
    conn= MongoClient()
    print("Connected to database")
except:
    print("Couldn't connect to database!")

db= conn.movie_collection

collection= db.movies

def new_movies():
        print("Enter movie details: ")
        movie_name= input("Movie Name: ")
        movie_year= input("Movie Year: ")
        movie_length= input("Movie Duration: ")
        movie= {"movie_name": movie_name,
                "movie_year": movie_year,
                "movie_length": movie_length}
        rec_id1= collection.insert_one(movie)
        print("Data inserted with record ids: ", rec_id1)


def listall():
    x= collection.find()
    for data in x:
        print(data)

def findmovie(movie_title):
    query= {"movie_name" : movie_title}
    print()
    x= collection.find(query)
    results= list(x)
    if len(results) != 0:
        for data in x:
            print(data)
    else:
        print("Movie not in collection!")

if __name__== "__main__":


    while(True):
        print("""\n1. Enter a new movie.
2. List all movies.
3. Search for a movie.
4. To exit the application, type "q" """)
        decide = input("What do you want to do? ")
        if decide == "1":
            new_movies()
            #break
        elif decide == "2":
            listall()
            # break
        elif decide == "3":
            title= input("Enter the movie name: ")
            findmovie(title)
            #break
        elif decide == "q":
            break
