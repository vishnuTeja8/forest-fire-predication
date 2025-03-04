# Forest Fire Prediction 

This project aims to predict the likelihood of forest fires in Algeria based on environmental factors such as temperature, humidity, wind speed, rainfall, and other meteorological indices. The dataset contains historical data from two regions: Bejaia and Sidi-Bel Abbes . A machine learning model (e.g., Random Forest) is trained to classify whether a given set of conditions indicates a high risk of fire (fire) or not (not fire).
## Features
Data Preprocessing : Handles missing values, encodes categorical variables, and ensures consistent numeric data types.

Machine Learning Model : Trains a Random Forest classifier to predict forest fire risks.

Streamlit App : Provides a user-friendly interface for making predictions in real-time.

Model Persistence : Saves the trained model for reuse in future predictions.



## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
- [How to Run Tests](#how-to-run-tests)

## Dataset Description
The dataset is split into two regions:

Bejaia Region Dataset : Contains 186 rows of data.

Sidi-Bel Abbes Region Dataset : Contains 186 rows of data.

Each row includes the following features:

day, month, year: Date-related information.

Temperature: Temperature in °C.

RH: Relative Humidity (%).

Ws: Wind Speed (km/h).

Rain: Rainfall (mm).

FFMC: Fine Fuel Moisture Code.

DMC: Duff Moisture Code.

DC: Drought Code.

ISI: Initial Spread Index.

BUI: Buildup Index.

FWI: Fire Weather Index.

Classes: Target variable (fire or not fire).



## Installation

Instructions on how to install and set up your project.

```bash
# Clone the repository
git clone https://github.com/vishnuteja8/forest-fire-prediction.git

# Navigate to the project directory
cd forest-fire-prediction

# Install dependencies
pip install -r requirements.txt
```

## Usage

Instructions and examples for using your project.
navigate to the project directory 
```bash
cd src
```
run the streamlit app
```bash
streamlit run app.py
```
## Contributing

Guidelines for contributing to the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

Your Name - [Your Email](mailto:vishnutejaperumandla@gmail.com)

Project Link: [https://github.com/vishnuteja8/forest-fire-prediction](https://github.com/vishnuteja8/forest-fire-prediction)

## Acknowledgements

- Hat tip to anyone whose code was used
- Inspiration
- References



List any relevant features here.

## How to Run Tests

Instructions on how to run tests for your project.

```bash
# Run tests
npm test
```
