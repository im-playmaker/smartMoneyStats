# Smart Money Stats

**Smart Money Stats** is a web application built using Django that provides real-time stock market data visualized through interactive graphs. This tool helps traders analyze historical stock data, uncover trends, and make informed decisions to choose the best trading strategies.

## Features

- **Stock Market Data**: Access stock market data, including price history, volume, and other essential metrics.
- **Interactive Graphs**: Visualize stock data in clear, interactive graphs to identify patterns and trends.
- **Historical Data**: Analyze historical data for both short-term and long-term trading strategies.
- **Decision Support**: Insights and visualizations to assist traders in making data-driven decisions.

## Technologies Used

- **Django**: The backend of the application, providing a scalable and secure framework for managing the stock data.
- **PostgreSQL**: A powerful database to store historical stock market data.
- **Matplotlib / Plotly**: For rendering the interactive graphs and visualizations.
- **Celery**: For periodic tasks, such as fetching new stock data.
- **Docker**: For containerization and easy deployment of the application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-money-stats.git
   cd smart-money-stats
