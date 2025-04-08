import statistics
import random
import requests
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API_KEY")
URL = f"http://www.omdbapi.com/?apikey={api_key}&t="



class MovieApp:
    def __init__(self, storage):
        """ Initialize the MovieApp with a storage backend. """
        self._storage = storage


    def _command_list_movies(self):
        """ Displays a list of all movies stored in the database with their ratings. """
        movies = self._storage.list_movies()

        print()
        print(f"{len(movies)} movies in total")

        for movie, info in movies.items():
            print(f"{movie}: {info['Rating']}")


    def _command_add_movie(self):
        """
        Sends GET request to the OMDb API to fetch movie information based on the provided title.
        After successful GET request, data is stored to the corresponding file through the add_movie storage method.
        """
        user_title = input("Enter new movie name: ").strip()

        if not user_title:
            print("Didn't find movie  in the API")
            return

        try:
            data = requests.get(URL + user_title)
            data = data.json()

            if data.get("Response") == "False":
                print(f"Error: {data.get('Error')}")
                return

            title = data.get("Title")
            year = int(data.get("Year", 0))
            rating = float(data.get("imdbRating", 0.0))
            poster = data.get("Poster")

            self._storage.add_movie(title, year, rating, poster)

            print(f"Movie {title} successfully added")

        except requests.exceptions.ConnectionError:
            print("Error: no connection to OMDb API!")


    def _command_delete_movie(self):
        """ Deletes data of the specified movie title. """

        movie_to_be_deleted = input("Enter movie name to delete: ")
        self._storage.delete_movie(movie_to_be_deleted)


    def _command_movie_stats(self):
        """
        Displays movie statistics including average, median rating,
        best-rated and worst-rated movies.
        """
        movies = self._storage.list_movies()

        if not movies:
            print("No movies in storage.")
            return

        movies_dict = {}
        sum_ratings = 0

        for movie, info in movies.items():
            rating = float(info["Rating"])
            movies_dict[movie] = rating
            sum_ratings += float(rating)


        average_rating = sum_ratings / len(movies_dict)
        print()

        median_rating = statistics.median(map(float, movies_dict.values()))

        best_movie = max(movies, key=lambda x: movies[x]["Rating"])

        worst_movie = min(movies, key=lambda x: movies[x]["Rating"])

        print(f"Average rating: {average_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movie: {best_movie} ({movies[best_movie]['Rating']})")
        print(f"Worst movie: {worst_movie} ({movies[worst_movie]['Rating']})")


    def _command_random_movie(self):
        """ Picks and displays a random movie from the database. """
        movies = self._storage.list_movies()

        if not movies:
            print("No movies available.")
            return

        random_movie = random.choice(list(movies.keys()))
        random_movie_rating = movies[random_movie]['Rating']

        print()
        print(f"Your movie for tonight: {random_movie}, it's rated {random_movie_rating}")


    def _command_search_movie(self):
        """ Searches for movies by partial name (case-insensitive). """
        movies = self._storage.list_movies()

        part_movie_name = input("\nEnter part of movie name: ").strip().lower()

        found = False

        for movie, info in movies.items():
            if part_movie_name in movie.lower():
                print(f"{movie} ({info['Year']}): {info['Rating']}")
                found = True

        if not found:
            print("No matching movies found.")


    def _command_movies_ranking(self):
        """ Displays the ranking of all movies from highest to lowest rating. """
        movies = self._storage.list_movies()

        sorted_movies_ranking = sorted(movies.items(), key=lambda item: item[1]['Rating'], reverse=True)
        for movie, info in sorted_movies_ranking:
            print(f"{movie} ({info['Year']}): {info['Rating']}")


    def _generate_website(self):
        """ Generate a static HTML page listing all movies with titles years and posters. """
        movies = self._storage.list_movies()

        movies_website_content = ""

        if movies:
            for movie, info in movies.items():
                movies_website_content += f"<li>\n"
                movies_website_content += f"<div class='movie'>\n"
                movies_website_content += f"<img class='movie-poster' src='{info['Poster']}' title>\n"
                movies_website_content += f"<div class='movie-title'> {movie} </div>\n"
                movies_website_content += f"<div class='movie-year'> {info['Year']}</div>\n"
                movies_website_content += f"</div>\n"
                movies_website_content += f"</li>\n"

        with open ("_static/index_template.html", "r") as fobj:
            website_content = fobj.read()

        html_content_string = ""

        for line in website_content:
            html_content_string += f"{line}\n"

        html_dynamic_content = html_content_string.replace("__TEMPLATE_MOVIE_GRID__", movies_website_content)

        with open("_static/index.html", "w") as fobj:
            fobj.write(html_dynamic_content)

        print("Website created successfully.")


    def run(self):
        """
        Starts the main interactive loop of the MovieApp.
        Presents a menu to the user to choose from various operations.
        """
        print("********** My Movies Database **********\n")
        while True:
            movies = self._storage.list_movies()

            print("Menu:")

            menu_list = [
                "0. Exit", "1. List movies", "2. Add movie", "3. Delete movie", "4. Update movie",
                "5. Stats", "6. Random movie", "7. Search movie", "8. Movies sorted by rating", "9. Generate website"
            ]
            for menu_direction in menu_list:
                print(menu_direction)

            try:
                user_choice = input("\nEnter choice (0-9): ")
            except ValueError:
                print("Invalid input! Please enter a number between 0-8.")
                continue

            if user_choice == "0":
                print("Bye")
                break

            if user_choice == "1":
                self._command_list_movies()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "2":
                self._command_add_movie()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "5":
                self._command_movie_stats()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "6":
                self._command_random_movie()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "7":
                self._command_search_movie()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "8":
                self._command_movies_ranking()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue

            if user_choice == "9":
                self._generate_website()
                continue_app = input("\nPress enter to continue\n")
                if continue_app == "":
                    continue




