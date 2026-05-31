**Weather API Integration Project Documentation**
=====================================================

**Overview**
------------

This project integrates the OpenWeatherMap API to fetch weather data for a given city. The project consists of three modules: Weather Service Module, API Gateway Module, and Controller Module. The Weather Service Module is responsible for fetching weather data from the external API, the API Gateway Module handles incoming requests and routes them to the Weather Service Module, and the Controller Module handles user input and requests to the API Gateway.

**Features**
------------

*   Fetches weather data for a given city from the OpenWeatherMap API
*   Handles incoming requests and routes them to the Weather Service Module
*   Handles user input and requests to the API Gateway
*   Provides API documentation using Swagger

**Installation**
---------------

To install the project, follow these steps:

1.  Clone the project from the repository
2.  Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key in the `application.properties` file
3.  Run the project using the command `mvn spring-boot:run`

**Usage**
---------

To use the project, follow these steps:

1.  Send a GET request to the `/weather` endpoint to fetch weather data for the city "Mumbai"
2.  The API will return the weather data in JSON format

**API Reference**
-----------------

### Weather Service Module

*   **getWeatherData(String city)**: Fetches weather data for the given city from the external API
	+   Parameters: `city` (String)
	+   Returns: `WeatherResponse` object containing the weather data

### API Gateway Module

*   **getWeatherData()**: Handles incoming requests and routes them to the Weather Service Module
	+   Parameters: None
	+   Returns: `WeatherResponse` object containing the weather data

### Controller Module

*   **getWeatherData()**: Handles user input and requests to the API Gateway
	+   Parameters: None
	+   Returns: `WeatherResponse` object containing the weather data

**Code Structure**
-----------------

The project consists of the following packages:

*   `com.weather.api.module.weatherservice`: Contains the Weather Service Module classes
*   `com.weather.api.module.apigateway`: Contains the API Gateway Module classes
*   `com.weather.api.module.controller`: Contains the Controller Module classes
*   `com.weather.api.model`: Contains the model classes for the project

**Dependencies**
----------------

The project uses the following dependencies:

*   `spring-boot-starter-web`: Provides the Spring Boot web framework
*   `spring-boot-starter-swagger2`: Provides the Swagger API documentation
*   `com.fasterxml.jackson.core:jackson-databind`: Provides the Jackson JSON library

**Configuration**
----------------

The project uses the following configuration files:

*   `application.properties`: Contains the configuration properties for the project
*   `pom.xml`: Contains the Maven configuration for the project

**Security**
------------

The project uses the following security features:

*   **API Key**: The project uses an API key to authenticate requests to the OpenWeatherMap API
*   **Swagger Security**: The project uses Swagger security to authenticate requests to the API

**Testing**
------------

The project uses the following testing frameworks:

*   **JUnit**: Provides the JUnit testing framework
*   **Mockito**: Provides the Mockito testing framework

**Commit Messages**
------------------

The project follows the standard commit message format:

*   **Type**: The type of commit (e.g. "feat", "fix", "docs")
*   **Description**: A brief description of the commit
*   **Related Issues**: A list of related issues (e.g. "Closes #123")

**API Documentation**
---------------------

The project uses Swagger to provide API documentation. The API documentation can be accessed at `http://localhost:8080/swagger-ui.html`.

**API Endpoints**
-----------------

The project provides the following API endpoints:

*   **GET /weather**: Fetches weather data for the city "Mumbai"
*   **GET /weather/{city}**: Fetches weather data for the given city

**API Request Body**
---------------------

The project does not use a request body for any API endpoints.

**API Response**
----------------

The project returns the following API responses:

*   **200 OK**: The weather data for the given city
*   **404 Not Found**: The city was not found
*   **500 Internal Server Error**: An error occurred while fetching the weather data