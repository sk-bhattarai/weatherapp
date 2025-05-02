# Weather Comparison App

A Django-based web application that allows users to compare weather conditions between two cities. The app provides current weather data and a 5-day forecast for each city.

## Features

- Compare weather between two cities
- View current weather conditions including:
  - Temperature
  - Weather description
  - Humidity
  - Wind speed
  - Pressure
- 5-day weather forecast
- Search history tracking
- Responsive design

## Requirements

- Python 3.x
- Django
- requests
- OpenWeatherMap API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/weather-comparison-app.git
cd weather-comparison-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your browser.

## Usage

1. Enter the name of a city in the first input field
2. Optionally enter a second city for comparison
3. Click "Compare Weather" to see the current weather and 5-day forecast for both cities

## API

This project uses the OpenWeatherMap API:
- Current weather data: https://api.openweathermap.org/data/2.5/weather
- 5-day forecast: https://api.openweathermap.org/data/2.5/forecast

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 