# Weather forecast Back-end
This is the Back-end for the weather forecast project using ReactJs and Vite. To run this project, follow these steps:

1. First, clone the project from repository with:
    ```
    git clone <repository-url>
    ```
2. Make sure you have download and install python before. You can check for it with:
    ```
    python --version
    ```
3. Make sure that you are in the 'weather' directory. If not, use:
    ```
    cd weather
    ```
4. Next, you can create a virtual environment to manage the dependencies for the project.  
To create an environment: 
- go to the App folder using: cd app
- add the venv folder: 
    - with macOS/Linux, run the command: python3 -m venv .venv
    - with windows, run the command: py -3 -m venv .venv

After that, run the command to get to the VE:
- with macOS/Linux: . .venv/bin/activate
- with window: .venv\Scripts\activate
5. Install needed packages with the command:
    ```
    pip install -r requirements.txt
    ```
6. To run it in the development environment, you need to:
- Go the the settings.py 
- Change the DEBUG variable to True
- In the ALLOWED_HOSTS array, add your url (for localhost: 127.0.0.1)
- In the CORS_ALLOWED_ORIGINS array, add your url
7. Before run the app, you need to migrate the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Then run the server with:
    ```
    python manage.py runserver
    ```
9. Run this commant on another terminal for background tasks: (with the background tasks, i'm setting it to send email after 10s and every 10s later)
    ```
    python manage.py process_tasks
    ```
