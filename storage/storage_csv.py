from dataclasses import field

from storage.istorage import IStorage
from pathlib import Path
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path="storage/db/movies.csv"):
        """ Initializes CSV-storage file and checks if the storage folder exists. """
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, "w") as fobj:
                writer = csv.DictWriter(fobj, fieldnames=["Title", "Year", "Rating", "Poster"])
                writer.writeheader()


    def load_storage(self):
        """ Loads the CSV file data into dictionary. """
        movies = {}

        with open(self.file_path, "r") as fobj:
            reader = csv.DictReader(fobj)
            for row in reader:
                title = row["Title"]
                movies[title] = {
                    "Year": int(row["Year"]),
                    "Rating": float(row["Rating"]),
                    "Poster": row["Poster"]
                }
        return movies


    def save_storage(self, movies):
        """ Saves given data dictionary into the CSV file. """
        with open(self.file_path, "w") as fobj:
            writer = csv.DictWriter(fobj, fieldnames=["Title", "Year", "Rating", "Poster"])
            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    "Title": title,
                    "Year": info["Year"],
                    "Rating": info["Rating"],
                    "Poster": info["Poster"]
                })

    def list_movies(self):
        """ Returns the list of movies from the storage. """
        return self.load_storage()


    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to the storage. """
        movies = self.load_storage()

        movies[title] = {
            "Year": year,
            "Rating": rating,
            "Poster": poster
        }
        self.save_storage(movies)


    def delete_movie(self, title):
        """ Deletes a movie from storage if it exists. """
        movies = self.load_storage()

        if title in movies:
            del movies[title]
            self.save_storage(movies)
            print(f"Movie {title} successfully deleted")
        else:
            print(f"Movie '{title}' not found.")


    def update_movie(self, title, rating):
        movies = self.load_storage()

        if title in movies:
            movies[title]["Rating"] = rating
            self.save_storage(movies)
        else:
            print(f"Movie '{title}' not found.")


