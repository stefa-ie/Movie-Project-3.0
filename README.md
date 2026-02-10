# 🎬 Movie App — OOP + Web

A Python CLI movie database that uses the OMDb API to add films, stores them via pluggable backends (JSON or CSV), and generates a static website with posters. Built with OOP: a single `MovieApp` class and an abstract `IStorage` interface so you can swap storage without changing app logic.

## ✨ Features

- **List movies** — View all stored movies with ratings
- **Add movie** — Fetch title, year, rating, and poster from OMDb by name
- **Delete movie** — Remove a movie from storage by title
- **Stats** — Average and median rating, best and worst movie
- **Random movie** — Pick a random movie from your list
- **Search** — Find movies by partial name (case-insensitive)
- **Movies by rating** — Sorted list from highest to lowest rating
- **Generate website** — Build a static HTML page (`_static/index.html`) with a movie grid (titles, years, posters), using a template and CSS

## 🚀 Getting Started

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install requests python-dotenv
```

Add your OMDb API key. Create a `.env` file in the project root:

```
API_KEY=your_omdb_api_key
```

Get a free key at [OMDb API](https://www.omdbapi.com/apikey.aspx).

Run the app:

```bash
python3 main.py
```

## 🗂️ Project Structure

- `main.py` — Entry point; wires `MovieApp` to a storage (JSON or CSV) and runs the menu
- `movie_app.py` — Core `MovieApp` class: menu loop, OMDb integration, and all commands (list, add, delete, stats, random, search, ranking, generate website)
- `storage/istorage.py` — Abstract `IStorage` interface (list_movies, add_movie, delete_movie, update_movie)
- `storage/storage_json.py` — JSON file implementation of `IStorage`
- `storage/storage_csv.py` — CSV file implementation of `IStorage`
- `storage/db/` — Default location for `movies.json` and `movies.csv`
- `_static/index_template.html` — HTML template with placeholders for title and movie grid
- `_static/style.css` — Styles for the generated movie page
- `_static/index.html` — Generated output (created when you choose “Generate website”)

## 🎮 How to Use

1. Run `python3 main.py` to start the interactive menu.
2. Use **1** to list movies, **2** to add (by title, via OMDb), **3** to delete.
3. Use **5** for stats, **6** for a random pick, **7** to search, **8** for ranking.
4. Use **9** to generate the website; open `_static/index.html` in a browser to view it.
5. Use **0** to exit.

## 🛠️ Customization

- **Storage backend** — In `main.py`, switch between `StorageJson` and `StorageCsv` (or add your own `IStorage` implementation) and pass it to `MovieApp`.
- **Data files** — Point storage classes to different paths (e.g. another JSON/CSV file).
- **Website** — Edit `_static/index_template.html` and `_static/style.css` to change layout and styling of the generated page.

## 🧰 Tech Stack

- **Python 3**
- **requests** — OMDb API calls
- **python-dotenv** — Load `API_KEY` from `.env`
- **OMDb API** — Movie metadata and posters
- HTML/CSS for the generated static site
