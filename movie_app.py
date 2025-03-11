class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movies = self._storage.list_movies()
        ...

    def _command_movie_stats(self):
        ...

    ...

    def _generate_website(self):
        ...

    def run(self):
      # Print menu
      # Get use command
      # Execute command