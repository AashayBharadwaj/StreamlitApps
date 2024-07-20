# Breast Cancer Predictor

This Streamlit-based app helps diagnose breast cancer by analyzing cell nuclei measurements from tissue samples.

# Stock Analysis Dashboard
![Breast Cancer Predictor](https://github.com/AashayBharadwaj/StreamlitApps/blob/fad4afabff59862d999baf7dedf7aaf096438f54/Images/Cancer-Prediction.png)

## Key Features
- **Interactive Sliders**: Adjust the values for various cell nuclei measurements, including Radius (mean), Texture (mean), Perimeter (mean), Area (mean), Smoothness (mean), and more.
- **Prediction**: Utilizes a Logistic Regression model to predict whether a breast mass is benign or malignant.
- **Visualizations**: Displays dynamic radar charts that visualize the mean, standard error, and worst values for each measurement.

## Technical Highlights
- **Logistic Regression**: Used for reliable and interpretable predictions.
- **joblib**: Efficiently saves and loads the trained model. joblib is a powerful tool for serializing Python objects, which is essential for saving machine learning models and pipelines. This allows the model to be easily reused and deployed without the need to retrain it every time, ensuring consistency and saving time.
- **User-Friendly Interface**: Built with Streamlit to provide an intuitive user experience.

## Future Scope
- Integration with data from Freestyle Libre, Fitbit, Apple Watch, and other fitness trackers to create more comprehensive health monitoring solutions.

## Installation

To run this app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser.
2. Use the sliders on the sidebar to adjust the values for various cell nuclei measurements.
3. View the prediction to see whether the breast mass is likely benign or malignant.
4. Explore the radar chart to understand the distribution of different measurements.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and create a pull request.

## Feedback

Your feedback and suggestions are always welcome! If you have any questions or suggestions, please reach out.

## Contact

For any inquiries, please contact me at [aashay.bharadwaj@gmail.com](mailto:aashay.bharadwaj@gmail.com).

---
Special thanks to Alejandro AO for the project idea.
https://www.linkedin.com/in/alejandro-ao/

---

# Acknowledgements

This project uses the following libraries and tools:
- [Streamlit](https://streamlit.io/)
- [joblib](https://joblib.readthedocs.io/)
- [Plotly](https://plotly.com/)
- [Scikit-learn](https://scikit-learn.org/)

Thank you for using the Breast Cancer Predictor app!

