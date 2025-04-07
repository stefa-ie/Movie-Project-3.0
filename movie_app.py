import statistics
import random


class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _command_list_movies(self):
        movies = self._storage.list_movies()

        print()
        print(f"{len(movies)} movies in total")

        for movie, details in movies.items():
            print(f"{movie}: {details['Rating']}")


    def _command_movie_stats(self):
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
        movies = self._storage.list_movies()

        if not movies:
            print("No movies available.")
            return

        random_movie = random.choice(list(movies.keys()))
        random_movie_rating = movies[random_movie]['Rating']

        print()
        print(f"Your movie for tonight: {random_movie}, it's rated {random_movie_rating}")


    def _command_search_movie(self):
        movies = self._storage.list_movies()

        part_movie_name = input("\nEnter part of movie name: ").strip().lower()

        found = False

        for movie, details in movies.items():
            if part_movie_name in movie.lower():
                print(f"{movie} ({details['Year']}): {details['Rating']}")
                found = True

        if not found:
            print("No matching movies found.")


    def _command_movies_ranking(self):
        movies = self._storage.list_movies()

        sorted_movies_ranking = sorted(movies.items(), key=lambda item: item[1]['Rating'], reverse=True)
        for movie, details in sorted_movies_ranking:
            print(f"{movie} ({details['Year']}): {details['Rating']}")


    def _generate_website(self):
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




