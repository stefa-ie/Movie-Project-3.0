from istorage import IStorage
import json
from pathlib import Path

class StorageJson(IStorage):
    def __init__(self, file_path="storage/movies.json"):
        """ Initializes storage and checks if the storage folder exists. """
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            with open(self.file_path, "w") as fobj:
                json.dump({}, fobj)

        self.local_data = self.load_storage()


    def load_storage(self):
        """ Loads the JSON file data into local_data. """
        if self.file_path.exists():
            with open(self.file_path, "r") as fobj:
                return json.load(fobj)
        return {}


    def save_storage(self):
        """ Saves local_data back to JSON file. """
        with open(self.file_path, "w") as fobj:
            json.dump(self.local_data, fobj, indent=4)


    def list_movies(self):
        """ Returns the list of movies from the storage. """
        return self.local_data


    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to the storage. """
        self.local_data[title] = {
            "Year": year,
            "Rating": rating,
            "Poster": poster
        }
        self.save_storage()


    def delete_movie(self, title):
        """ Deletes a movie from storage if it exists. """
        if title in self.local_data:
            del self.local_data[title]
            self.save_storage()
        else:
            print(f"Movie '{title}' not found.")


    def update_movie(self, title, rating):
        """ Updates the rating if the movie exists. """
        if title in self.local_data:
            self.local_data[title]["Rating"] = rating
            self.save_storage()
        else:
            print(f"Movie '{title}' not found.")




