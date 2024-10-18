# Movie Details Finder

A simple Flask web application that allows users to search for movie details using the OMDb API. The app takes a movie title as input and returns details such as the title, year, director, actors, plot, awards, and IMDB rating. 

## Features
- **Search for Movie Details:** Users can input a movie title to fetch information.
- **Movie Information Display:** Includes movie poster, director, actors, plot, awards, and IMDB rating.
- **Error Handling:** Displays appropriate error messages when movie data cannot be fetched.

## Getting Started

Follow the steps below to get the project running on your local machine.

### Prerequisites

- Python 3.x installed on your system.
- Flask installed (`pip install flask`).
- OMDb API key (You can get your free API key from [OMDb](http://www.omdbapi.com/apikey.aspx)).

### Installation Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/hafeezabhanu9/movie-details-finder.git
    cd movie-details-finder
    ```

2. **Install dependencies:**
    Install the required Python packages

3. **Set up your OMDb API key:**
    
    - Open `app.py` and replace the value of `API_KEY` with your OMDb API key:

    ```python
    
    API_KEY = "a43183c2"
    
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Access the application:**
    - Open a web browser and navigate to `http://127.0.0.1:5000/` to start searching for movie details.

### Project Structure

```bash
.
├── app.py     
├── Dockerfile              
└── README.md 

```

## API Usage
- The app interacts with the OMDb API to fetch movie data. You will need to use your own OMDb API key in app.py.

### Features to Implement
- Search Suggestions: Implement real-time suggestions as the user types in the movie title.
- Watchlist: Add functionality to save movies to a watchlist during the session.
- Related Movies: Display related movies based on the movie genre.

## Author
- **Hafeeza Bhanu Mohmmad**
- **Lalam Divya Sri**

### Acknowledgements
- OMDB-API: For providing the API.
