# MovieDB

MovieDB is a web application that allows users to search and explore movies. It provides details about movies, including title, description, genre, release date, and ratings. The application is built using Django and integrates with an external movie database API to fetch movie data.

## Features

- **Search Movies**: Users can search for movies by title.
- **Movie Details**: Displays detailed information about each movie, including its genre, release date, and description.
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.
- **User Authentication**: Users can sign up, log in, and save their favorite movies (if implemented).

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite (default) or PostgreSQL (optional)
- **API Integration**: Movie database API (e.g., The Movie Database API)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nwesha/moviedb.git
    cd moviedb
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:
    Create a `.env` file in the project root and add your API keys and other settings:
    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key
    MOVIE_API_KEY=your_movie_db_api_key
    ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Search for Movies**: Enter a movie title in the search bar to find information about it.
- **View Movie Details**: Click on a movie from the search results to see more details.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-branch-name`
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [The Movie Database API](https://www.themoviedb.org/documentation/api) for providing movie data.
- Django documentation and community for guidance and support.
