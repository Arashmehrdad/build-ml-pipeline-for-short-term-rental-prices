# Build an ML Pipeline for Short-Term Rental Prices in NYC

This repository contains my completed project for the Machine Learning DevOps Engineer program. In this project, I built an end-to-end machine learning pipeline to estimate short-term rental prices for NYC properties using similar listing characteristics. The goal was not only to train a working model, but also to package the full workflow in a reproducible MLOps pipeline that can be rerun as new weekly data arrives.

The project covers the full lifecycle of an ML workflow: exploratory data analysis, data cleaning, validation, data splitting, model training, hyperparameter optimization, model selection, testing, pipeline visualization, and release management. I used MLflow to orchestrate the pipeline, Hydra for configuration management, and Weights & Biases for experiment tracking and artifact versioning.

## Project Overview

The business scenario is based on a property management company that rents rooms and properties for short stays across online platforms. Because new data is received in bulk on a regular basis, the pricing model needs to be retrained on a recurring schedule. To support that requirement, I implemented a reusable pipeline that can process incoming data, validate quality, train and evaluate a model, and support future retraining with minimal manual effort.

## What I Implemented

This project includes the following main stages:

* Exploratory data analysis to understand feature distributions, missing values, and outliers
* Basic data cleaning to remove invalid prices and correct data types
* Data quality checks to validate row counts and acceptable price ranges
* Train/validation/test splitting using reusable pipeline components
* Random Forest model training for baseline price prediction
* Hyperparameter optimization using Hydra multi-run experiments
* Model selection based on the lowest MAE
* Regression model testing on a held-out test set
* Pipeline visualization and artifact lineage tracking in Weights & Biases
* Versioned project release for reproducible reruns on new data samples

## Technical Stack

The project uses the following tools and frameworks:

* Python 3.13
* MLflow
* Hydra
* Weights & Biases
* scikit-learn
* pandas
* cookiecutter
* conda

## Key Learning Outcomes

Through this project, I practiced building a machine learning workflow as a production-style pipeline rather than as a one-off notebook experiment. The most important lessons from this work were:

* structuring ML code into modular, reusable pipeline steps
* tracking datasets and model artifacts properly
* using configuration-driven experimentation instead of hardcoding values
* validating data before training to catch issues early
* managing model releases and reruns in a more realistic MLOps setting

## Running the Project

To run the full pipeline from the project root:

```bash
mlflow run .
```

To run only selected steps during development:

```bash
mlflow run . -P steps=download,basic_cleaning
```

To override configuration values with Hydra:

```bash
mlflow run . \
  -P steps=train_random_forest \
  -P hydra_options="modeling.random_forest.max_features=0.5"
```

## License [License](LICENSE.txt)

## Author

Arash Mehrdad
