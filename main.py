from app.movie_app import MovieApp
from movie_app import MovieApp
from storage import StorageJson
from storage import StorageCsv


# Calling MovieApp.run() to start the application
def main():

    storage = StorageJson('storage/movies.json')
    movie_app = MovieApp(storage)

    movie_app.run()


if __name__ == '__main__':
    main()