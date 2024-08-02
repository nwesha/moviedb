# MovieDB

MovieDB is a web application that allows users to search, explore, and manage movies. It provides details about movies, including title, description, genre, release date, and ratings. The application is built using Django, and movie data is added directly through the user interface or the admin panel, without the need for an external API.

![image](https://github.com/user-attachments/assets/9a5d77f0-4214-4d99-ba94-99a48f190f6b)

### ScreenRec of the working of the Project
[Link to Google Drive](https://drive.google.com/drive/folders/1c6Yyegn7ucSCi2-a7Xq1Oh-VR6mV9n3x?usp=sharing)

## Features

- **Search Movies**: Users can search for movies by title.
- **Movie Details**: Displays detailed information about each movie, including its genre, release date, and rating.
- **Add Movies**: Admins can add new movies directly through the application interface or via the Django admin panel.
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.
- **User Authentication**: Users can sign up, log in, and save their favorite movies (if implemented).
- **Admin Panel**: Admins can add, edit, and delete movies directly through the Django admin interface.

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
    Create a `.env` file in the project root and add your settings:
    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key
    ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
   Follow the prompts to set up your admin credentials.

7. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.
    - Access the admin panel at `http://127.0.0.1:8000/admin/` to manage movies.

## Usage

- **Add Movies**: Admins can add new movies directly through the application's user interface or via the Django admin panel.
- **Search for Movies**: Enter a movie title in the search bar to find information about it.
- **View Movie Details**: Click on a movie from the search results to see more details.
- **Admin Panel**: Log in as an admin to add, edit, or delete movies.

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

- Django documentation and community for guidance and support.
