# Hawaii Climate Analysis and API

This project explores climate data from Honolulu, Hawaii, using Python, SQLAlchemy, Pandas, Matplotlib, and Flask. It also expands on the original challenge using Google AI to design a front end.

## Original Challenge:

This project was developed to support a trip planning for a vacation in Honolulu, Hawaii, by performing an analysis of the area's climate database.

The project involves the following tasks:

### Part 1: Analyze and Explore the Climate Data

1.  **Database Connection:** Connect to the SQLite database (`hawaii.sqlite`) using SQLAlchemy. Use `automap_base()` to reflect the tables (`station` and `measurement`) into classes. Create a session to link Python to the database and properly close the session upon completion.

2.  **Precipitation Analysis:**
    *   Find the most recent date in the dataset.
    *   Retrieve the previous 12 months of precipitation data, selecting only the 'date' and 'prcp' values.
    *   Load the query results into a Pandas DataFrame with explicit column names.
    *   Sort the DataFrame by date.
    *   Plot the data using the DataFrame's `plot()` method.
    *   Print the summary statistics of the precipitation data using Pandas `describe()` method.

3.  **Station Analysis:**
    *   Calculate the total number of stations in the dataset.
    *   Identify the most active stations by listing stations and their observation counts in descending order.
    *   Determine the station ID with the greatest number of observations.
    *   Calculate the minimum, maximum, and average temperatures for the most active station.
    *   Retrieve the previous 12 months of temperature observation (TOBS) data for the most active station.
    *   Plot the TOBS data as a histogram with `bins=12`.

### Part 2: Design Your Climate App

1.  **Flask API:** Create a Flask API with the following routes:
    *   `/`: Homepage that lists all available routes.
    *   `/api/v1.0/precipitation`: Returns precipitation data (last 12 months) as a JSON dictionary with date as keys and prcp as values.
    *   `/api/v1.0/stations`: Returns a JSON list of stations.
    *   `/api/v1.0/tobs`: Returns a JSON list of temperature observations (TOBS) for the most active station for the previous year.
    *   `/api/v1.0/<start>`: Returns TMIN, TAVG, and TMAX for all dates greater than or equal to the specified start date.
    *   `/api/v1.0/<start>/<end>`: Returns TMIN, TAVG, and TMAX for dates between the specified start and end dates, inclusive.

## Expanded Challenge: Interactive Webpage with Google AI Assistance

This project expands beyond the base requirements by creating an interactive webpage that leverages the API endpoints developed. It was assisted by Google AI to implement the front-end. This effort includes:

*   **Dynamic API Interaction:** Using HTML, CSS, and JavaScript to build a user interface to interact with each API endpoint.

*   **Interactive Selection:** A dropdown menu to select an API endpoint. The data type returned determines what action the JavaScript will take.
     *   List Types: The data will be displayed as an HTML List
     *   Object Types: The data will be displayed as an HTML Table
     *   Date Range: The data returned will be labeled correctly and the Average temperature will be rounded to 2 decimal places.

*   **Date Input:** Date inputs for start and end dates when the appropriate endpoint is selected.

*   **Plotted Outputs:** The plots generated in the `Climate.ipynb` file are now displayed on the landing page in the `plot-container`.

*   **Visual Appeal:**  The page is styled with a basic CSS, using Hawaiian-inspired colors.

*   **GitHub Pages Deployment:** This project is designed to be easily published to GitHub Pages for demonstrating the project on a live webpage.

## Code and File Structure