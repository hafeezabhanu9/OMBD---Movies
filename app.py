from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = "a43183c2"
OMDB_API_URL = "http://www.omdbapi.com/"

watchlist = []

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Movie Details Finder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background-color: white;
                padding: 2rem;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                width: 80%;
                max-width: 600px;
            }

            h1 {
                color: #333;
                text-align: center;
            }

            form {
                display: flex;
                justify-content: center;
                margin-bottom: 2rem;
            }

            input[type="text"] {
                padding: 0.5rem;
                font-size: 1rem;
                width: 70%;
                margin-right: 1rem;
            }

            button {
                padding: 0.5rem 1rem;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 4px;
            }

            button:hover {
                background-color: #0056b3;
            }

            .watchlist {
                margin-top: 2rem;
            }

            .watchlist ul {
                list-style-type: none;
                padding: 0;
            }

            .watchlist li {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .remove {
                padding: 0.5rem;
                background-color: #FF5733;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            .remove:hover {
                background-color: #C70039;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Movie Details Finder</h1>
            <form action="/search_movie" method="POST">
                <input type="text" name="title" placeholder="Enter movie title" required>
                <button type="submit">Search</button>
            </form>

            <h2>Watchlist</h2>
            <div class="watchlist">
                <ul>
                    ''' + ''.join(
                        [f"<li>{movie} <form action='/remove_movie' method='POST' style='display:inline;'><input type='hidden' name='title' value='{movie}'><button type='submit' class='remove'>Remove</button></form></li>" for movie in watchlist]
                    ) + '''
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/search_movie', methods=['POST'])
def search_movie():
    movie_title = request.form.get('title')
    params = {
        'apikey': API_KEY,
        's': movie_title
    }
    response = requests.get(OMDB_API_URL, params=params)

    if response.status_code == 200:
        movies_data = response.json()
        if movies_data.get('Response') == "True":
            movie_list = movies_data.get('Search', [])
            results_html = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Search Results</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}

                    .container {{
                        background-color: white;
                        padding: 2rem;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        border-radius: 8px;
                        width: 80%;
                        max-width: 600px;
                    }}

                    h1 {{
                        color: #333;
                        text-align: center;
                    }}

                    .results-container {{
                        text-align: center;
                        margin-top: 2rem;
                    }}

                    .results-container ul {{
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }}

                    .results-container li {{
                        margin: 1rem 0;
                    }}

                    .results-container a {{
                        color: #007BFF;
                        text-decoration: none;
                    }}

                    .results-container a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Search Results for "{movie_title}"</h1>
                    <div class="results-container">
                        <ul>
                        {' '.join(f'<li><a href="/get_movie?imdbID={movie["imdbID"]}">{movie["Title"]} ({movie["Year"]})</a></li>' for movie in movie_list)}
                        </ul>
                        <a href="/">Back to Home</a>
                    </div>
                </div>
            </body>
            </html>
            '''
            return results_html
        else:
            return f'''
            <html>
            <body>
                <p class="error">{movies_data.get('Error')}</p>
                <a href="/">Back to Home</a>
            </body>
            </html>
            '''
    else:
        return '''
        <html>
        <body>
            <p class="error">Error fetching movie details</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
        '''

@app.route('/get_movie', methods=['GET'])
def get_movie_details():
    imdb_id = request.args.get('imdbID')
    params = {
        'apikey': API_KEY,
        'i': imdb_id
    }
    response = requests.get(OMDB_API_URL, params=params)

    if response.status_code == 200:
        movie_data = response.json()
        if movie_data.get('Response') == "True":
            return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{movie_data["Title"]} Details</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}

                    .container {{
                        background-color: white;
                        padding: 2rem;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        border-radius: 8px;
                        width: 80%;
                        max-width: 600px;
                    }}

                    h1 {{
                        color: #333;
                        text-align: center;
                    }}

                    .movie-details {{
                        text-align: center;
                    }}

                    .movie-details img {{
                        width: 100px;
                        height: auto;
                        margin-bottom: 1rem;
                    }}

                    .error {{
                        color: red;
                        text-align: center;
                    }}

                    .add-to-watchlist {{
                        padding: 0.5rem;
                        background-color: #28A745;
                        color: white;
                        border: none;
                        cursor: pointer;
                        border-radius: 4px;
                        margin-top: 1rem; /* Added margin for line gap */
                    }}

                    .add-to-watchlist:hover {{
                        background-color: #218838;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="movie-details">
                        <h2>{movie_data["Title"]} ({movie_data["Year"]})</h2>
                        <img src="{movie_data["Poster"]}" alt="{movie_data["Title"]}">
                        <p><strong>Director:</strong> {movie_data["Director"]}</p>
                        <p><strong>Actors:</strong> {movie_data["Actors"]}</p>
                        <p><strong>Genre:</strong> {movie_data["Genre"]}</p>
                        <p><strong>Language:</strong> {movie_data["Language"]}</p>
                        <p><strong>Awards:</strong> {movie_data["Awards"]}</p>
                        <p><strong>Plot:</strong> {movie_data["Plot"]}</p>
                        <p><strong>IMDB Rating:</strong> {movie_data["imdbRating"]}</p>
                        <form action="/add_to_watchlist" method="POST">
                            <input type="hidden" name="title" value="{movie_data["Title"]}">
                            <button type="submit" class="add-to-watchlist">Add to Watchlist</button>
                        </form>
                        <br> <!-- Line gap before "Back to Home" -->
                        <a href="/">Back to Home</a>
                    </div>
                </div>
            </body>
            </html>
            '''
        else:
            return f'''
            <html>
            <body>
                <p class="error">{movie_data.get('Error')}</p>
                <a href="/">Back to Home</a>
            </body>
            </html>
            '''
    else:
        return '''
        <html>
        <body>
            <p class="error">Error fetching movie details</p>
            <a href="/">Back to Home</a>
        </body>
        </html>
        '''

@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    movie_title = request.form.get('title')
    watchlist.append(movie_title)
    return redirect(url_for('home'))

@app.route('/remove_movie', methods=['POST'])
def remove_movie():
    movie_title = request.form.get('title')
    if movie_title in watchlist:
        watchlist.remove(movie_title)
    return redirect(url_for('home'))

app.run(debug=True)
