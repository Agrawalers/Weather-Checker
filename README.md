Django Weather Checker ☀️☁️🌧️
A clean, simple, and responsive web application built with Django to provide real-time weather information for any city in the world. Enter a city name and instantly get the current weather conditions.


✨ Features
City-Based Search: Get the current weather by simply typing in a city's name.

Detailed Weather Info: Displays key information, including:

Temperature (in Celsius)

Weather conditions (e.g., "Clear Sky," "Rain," "Clouds")

Humidity Percentage

Wind Speed

Dynamic Weather Icons: Shows a unique icon that visually represents the current weather condition.

User-Friendly Interface: A minimalist and clean UI that is easy to navigate.

Error Handling: Gracefully handles cases where a city cannot be found.

🛠️ Tech Stack
Category

Technology

Backend

Python, Django

Database

SQLite 3 (Default)

Frontend

HTML, CSS (easily extendable with a framework like Bootstrap or Tailwind)

API

OpenWeatherMap API

🚀 Getting Started
Follow these instructions to get a local copy of the project up and running for development and testing.

Prerequisites
Make sure you have the following installed on your system:

Python (3.8 or higher)

pip (Python package installer)

git (Version control)

Installation & Setup
Clone the Repository

git clone [https://github.com/your-username/your-project-repo.git](https://github.com/your-username/your-project-repo.git)
cd your-project-repo

Create and Activate a Virtual Environment

On macOS and Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
venv\Scripts\activate

Install Required Packages

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file, you can create one with pip freeze > requirements.txt after installing Django and other necessary packages like requests.)

Set Up Environment Variables

Sign up on OpenWeatherMap to get a free API key.

Create a file named .env in the root directory of your project.

Add your API key to the .env file like this:

API_KEY=your_actual_api_key_here

(You will need to ensure your settings.py is configured to read this key. A common way is using a library like python-decouple.)

Apply Database Migrations

python manage.py migrate

Run the Development Server

python manage.py runserver

The application will be running and available at http://127.0.0.1:8000/.

usage
Open your web browser and navigate to http://127.0.0.1:8000/.

You will see a search bar on the homepage.

Enter the name of any city you want to check the weather for (e.g., "London", "Mumbai", "Tokyo").

Press the "Search" button or hit Enter.

The page will refresh to display the current weather details for the specified city.

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE.txt for more information.
(Note: You should add a LICENSE.txt file to your repository if you haven't already).

🙏 Acknowledgements
OpenWeatherMap for providing the free and reliable weather data API.

The Django Project for the amazing web framework.
