# Weather App

<a href="https://weather-provider-app.vercel.app/"><img src="https://img.shields.io/badge/-Website%20Link-4285F4?style=for-the-badge&logo=Google-Chrome&logoColor=white"/></a>

Weather App is a Django project that fetches weather details based on the city input provided by the user. It utilizes the OpenWeatherMap API to retrieve weather data.

## Setup

### Prerequisites

- Python 3.9+
- Django 4.2
- django-environ

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sumitRohilla/Weather-App.git
   cd WeatherApp
   ```

2. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the root directory (same level as `manage.py`).
   - Add your OpenWeatherMap API key to the `.env` file:

     ```
     WEATHER_API_KEY=your_openweathermap_api_key
     ```

### Running the Application

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to `http://localhost:8000` to view the application.

## Usage

- Enter a city name in the provided input field on the homepage (`http://localhost:8000`) and click "Search" to fetch weather details.
- The weather details will be displayed on the same page, including country code, coordinates, temperature, weather description, pressure, and humidity.

## Deployment

The project is set up for deployment on platforms like Vercel. Follow these steps to deploy:

1. Connect your repository to Vercel.
2. Ensure that the `vercel.json`, `build_files.sh`, and `requirements.txt` files are set up correctly.
3. Push your changes to the repository. Vercel will automatically detect and deploy the changes.

## Project Structure

The project is structured as follows:

WeatherApp/\
├── WeatherApp/\
│ ├── __init__.py\
│ ├── settings.py\
│ ├── urls.py\
│ ├── wsgi.py\
│ └── asgi.py\
├── Weather/\
│ ├── __init__.py\
│ ├── admin.py\
│ ├── apps.py\
│ ├── migrations/\
│ │ └── **init**.py\
│ ├── models.py\
│ ├── tests.py\
│ ├── urls.py\
│ └── views.py\
├── static/\
│ └── style.css\
├── templates/\
│ └── index.html\
├── .gitignore\
├── build_files.sh\
├── .env\
├── manage.py\
├── README.md\
├── requirements.txt\
└── vercel.json\


## License

This project is licensed under the MIT License - see the LICENSE file for details.
