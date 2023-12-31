# Breast Cancer Recurrence Prediction

## Overview
This project focuses on developing a classification model to predict the likelihood of breast cancer recurrence or death based on patient information and tumor characteristics.

## Project Structure
- **Deployment**: Contains files related to deploying the breast cancer recurrence prediction model.
  - `gbsg_without_unmamed.csv`: Dataset used for training and testing the model.
  - `random_forest_model.pkl`: Trained Random Forest model.
  - `requirements.txt`: List of required Python packages for deployment.
  - `app.py`: Code for deploying the model and making predictions.
- **Documentation**: Contains the project proposal, final report, and presentation slides.
- **Data**: Includes the dataset in CSV format.
- **Images**: Houses all the images used in the project report.
- **Notebooks**:
  - `Breast Cancer Data Wrangling.ipynb`: Notebook for data preprocessing and cleaning.
  - `Breast Cancer Exploratory Analysis.ipynb`: Notebook for exploring and visualizing the dataset.
  - `Breast Cancer Feature Engineering and Modeling.ipynb`: Notebook for feature engineering and building the classification model.

### Requirements
- Python 3.x
- Jupyter Notebooks
- Required Python packages can be installed using:
  ```bash
  pip install -r requirements.txt

### Running the Notebooks
- 1-	Open Jupyter Notebook.
- 2-	Navigate to the Notebooks directory.
- 3-	Open and run the notebooks in the following order:
    * Breast Cancer Data Wrangling.ipynb
    * Breast Cancer Exploratory Analysis.ipynb
    * Breast Cancer Feature Engineering and Modeling.ipynb.

### Running the Deployment Code
To deploy the model and make predictions, follow these steps:

Install the required Python packages in requirement.txt
Run the deployment code by executing the app.py file.

### Results
In summary, the project has achieved success in constructing predictive models for breast cancer recurrence, showcasing particularly impressive performance with the RandomForestClassifier. The thorough evaluation of these models has yielded valuable insights, establishing a robust foundation for informed decision-making. To further enhance model efficacy, continuous refinements and explorations are recommended. The meticulous fitting of models to the dataset, coupled with comprehensive assessments of accuracy, precision, recall, and F1-score, has provided a detailed understanding of their predictive capabilities. Notably, the classification reports have placed a specific emphasis on predicting breast cancer recurrence or death (class 1).

### Acknowledgments
The primary data source is the breast cancer dataset from Kaggle

### Contact
Martin E. Vodanovic

Email: martinevodanovic@gmail.com

Feel free to customize it further based on your specific project details.

