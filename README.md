# Disease Prediction Using Machine Learning

## Description

The Disease Prediction Using Machine Learning project is an innovative web application developed with Streamlit. It harnesses advanced machine learning techniques and algorithms to accurately predict potential diseases based on user-provided symptoms.

This project represents an Internship Project under [Innovians Technologies](https://innovianstechnologies.com/), aimed at deepening insights into machine learning applications in predictive healthcare.

## Features

- **Number of Diseases Predictable**: The application can classify up to 42 different diseases.
- **Selectable Values**: Users can choose from 132 different symptom values.
- **Interactive Web Interface**: Easily select symptoms and receive instant disease predictions.
- **Classifier Algorithm**: Utilizes a Logistic Regression classifier for accurate predictions.
- **User-Friendly Design**: Streamlit-powered interface ensures simplicity and accessibility.
- **Real-Time Predictions**: Get immediate disease predictions as symptoms are selected.

## Technical Details

**Dataset (Data Source)**: Utilizes a curated dataset of symptoms and diseases for training the machine learning model. For dataset details, refer to [Dataset Link](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning).

**Models Trained**:
- **Logistic Regression**: Implemented in the Streamlit application.
- **Support Vector Machine (SVM)**: Trained but not integrated into the current Streamlit app.
- **K-Nearest Neighbors (KNN)**: Trained but not integrated into the current Streamlit app.

## Usage

The application functions by inputting selected symptoms into a trained machine learning model, which computes disease probabilities or classifications based on the symptom inputs.

For installation and utilization of the model, refer to or download the [Model](https://github.com/Neelkanth-khithani/Disease-Prediction-Using-ML/blob/main/model_app.py).

**Deployed Streamlit Link for Usage**: [Disease Prediction Web App](https://disease-prediction-using-ml-neelkanth.streamlit.app/)

## Model Performance Metrics

After training and evaluating the machine learning model, the following performance metrics were obtained on the test dataset:

| Model                      | Precision |
|----------------------------|-----------|
| Logistic Regression        | 0.1$       |
| Support Vector Machine (SVM)| 0.1$      |
| K-Nearest Neighbors (KNN)  | 0.1$     |

$ Full precision due to exceptionally clean and binary data
  
These metrics demonstrate that the model performs exceptionally well on the test data, achieving perfect accuracy, precision, recall, and F1-score. It indicates that the model can make predictions with high confidence and accuracy based on the symptoms provided.

For more details on the model evaluation process and implementation, refer to the project documentation and code files.

## Future Improvements

Future enhancements may include:

- **Enhanced UI/UX**: Refinement of visual aesthetics and user interface to optimize user experience.
- **Integration with Health APIs**: Connecting with external health data APIs to enhance disease prediction accuracy.
- **User Accounts and History**: Implementing features for users to store symptom history and past predictions.
- **Advanced Machine Learning Models**: Integration of more sophisticated models for improved disease prediction capabilities.

## Disclaimer

This application is designed solely for informational purposes and should not substitute professional medical advice, diagnosis, or treatment. Users are encouraged to consult qualified healthcare providers for medical concerns.

## Acknowledgements
Special thanks to [Ameen Manna](https://github.com/ameenmanna8824/) Sir for his invaluable guidance and support throughout. His expertise and mentorship were crucial in shaping my approach and understanding of Basic AI / ML.

## Resources
1. https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning
2. https://streamlit.io/
3. https://www.datacamp.com/tutorial/streamlit
4. https://www.analyticsvidhya.com/blog/2021/05/5-classification-algorithms-you-should-know-introductory-guide/
