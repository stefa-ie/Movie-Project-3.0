from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """ Prints the list of movies. """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to the storage. """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """ Deletes a movie from storage if it exists. """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """ Updates the rating if the movie exists. """
        pass

