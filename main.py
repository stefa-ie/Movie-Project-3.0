from movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv


# Calling MovieApp.run() to start the application
def main():

    storage_json = StorageJson('storage/db/movies.json')
    storage_csv = StorageCsv('storage/db/movies.csv')

    movie_app_json = MovieApp(storage_json)
    movie_app_csv = MovieApp(storage_csv)

    movie_app_csv.run()


if __name__ == '__main__':
    main()