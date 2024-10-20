# Movie Details Finder

A simple Flask web application that allows users to search for movie details using the OMDb API. The app takes a movie title as input and returns details such as the title, year, genre, language, director, actors, plot, awards, and IMDb rating. Users can also manage a watchlist by adding and removing movies.

## Features

- **Search for Movie Details:** Users can input a movie title to fetch information.
- **Movie Information Display:** Includes movie poster, director, genre, language, actors, plot, awards, and IMDb rating.
- **Watchlist Management:** Users can add movies to a watchlist and remove them later.
- **Error Handling:** Displays appropriate error messages when movie data cannot be fetched.

## Tech Stack

- **Python:** Core programming language for backend logic.
- **Flask:** Web framework for serving HTTP requests.
- **HTML/CSS:** For rendering the web interface.
- **OMDb API:** Used to fetch movie details.

## Dependencies
- **Flask:** A lightweight WSGI web application framework in Python.
- **Requests:** A library to send HTTP requests in Python.

## Getting Started

Follow the steps below to get the project running on your local machine.

### Prerequisites

- Python 3.x installed on your system.
- Flask installed (`pip install flask`).
- OMDb API key (You can get your free API key from [OMDb](http://www.omdbapi.com/)).

### Installation Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/hafeezabhanu9/OMDB---Movies.git
    cd OMDB---Movies
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OMDb API key:
    - Open `app.py` and replace the value of `API_KEY` with your OMDb API key:
    ```python
    API_KEY = "your_api_key"
    ```

### Running the Application

1. Run the application:
    ```bash
    python app.py
    ```

2. Access the application:
    - Open a web browser and navigate to `http://127.0.0.1:5000/` to start searching for movie details.

### Docker Instructions

- Build the Docker image:
  
    ```bash
    docker build -t movie-details-finder .
    ```

- Run the container:
  
    ```bash
    docker run -p 5000:5000 movie-details-finder
    ```

## Project Structure

```bash
.
├── app.py               # The main Flask app
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker setup
└── README.md            # Project documentation

```

## Usage

- Navigate to http://127.0.0.1:5000 in your web browser.
- Search for a movie by entering the title in the search bar.
- Browse the search results and click on a movie to view more details.
- Add the movie to your watchlist by clicking the Add to Watchlist button.
- You can view and manage your watchlist on the homepage.

## API Usage

The app interacts with the OMDb API to fetch movie data. You will need to use your own OMDb API key in `app.py`.

## Features to Implement

- **Search Suggestions:** Implement real-time suggestions as the user types in the movie title.
- **Related Movies:** Display related movies based on the movie genre.

## Authors

- **Hafeeza Bhanu Mohammad**
- **Lalam Divya Sri**

## Acknowledgements

- **OMDb API:** For providing movie data.
