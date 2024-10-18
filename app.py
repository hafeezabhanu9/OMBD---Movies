from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "a43183c2"
OMDB_API_URL = "http://www.omdbapi.com/"

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

            .movie-details {
                text-align: center;
            }

            .error {
                color: red;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Movie Details Finder</h1>
            <form action="/get_movie" method="POST">
                <input type="text" name="title" placeholder="Enter movie title" required>
                <button type="submit">Search</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/get_movie', methods=['POST'])
def get_movie_details():
    movie_title = request.form.get('title')

    if not movie_title:
        return redirect(url_for('home'))

    params = {
        'apikey': API_KEY,
        't': movie_title
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
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="movie-details">
                        <h2>{movie_data["Title"]} ({movie_data["Year"]})</h2>
                        <img src="{movie_data["Poster"]}" alt="{movie_data["Title"]}">
                        <p><strong>Director:</strong> {movie_data["Director"]}</p>
                        <p><strong>Actors:</strong> {movie_data["Actors"]}</p>
                        <p><strong>Awards:</strong> {movie_data["Awards"]}</p>
                        <p><strong>Plot:</strong> {movie_data["Plot"]}</p>
                        <p><strong>IMDB Rating:</strong> {movie_data["imdbRating"]}</p>
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
            </body>
            </html>
            '''
    else:
        return '''
        <html>
        <body>
            <p class="error">Error fetching movie details</p>
        </body>
        </html>
        '''

app.run(debug=True, host='0.0.0.0')
