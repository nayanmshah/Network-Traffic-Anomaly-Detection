
# Network Traffic Anomaly Detection

This project demonstrates the process of anomaly detection in network traffic data using the KDD Cup 1999 dataset. The objective is to detect abnormal network behavior (such as attacks or malicious activities) using unsupervised machine learning techniques.

## **Overview**

- **Dataset**: The project uses the KDD Cup 1999 dataset, which contains labeled network traffic data, and is widely used for research in intrusion detection.
- **Technique**: We use **Isolation Forest**, an unsupervised machine learning algorithm, to detect anomalies in network traffic data.
- **Preprocessing**: The data is preprocessed through steps like encoding categorical variables, normalizing numeric features, and handling missing values.
- **Goal**: To build a model that can detect anomalies in real-time network traffic based on the features and patterns learned from the historical data.

---

## **Project Structure**

```
Network-Traffic-Anomaly-Detection/
├── data/                   # Folder for storing datasets
│   ├── kddcup.data         # Your raw dataset
├── notebooks/              # Folder for Jupyter notebooks
│   ├── anomaly_detection.ipynb   # Data cleaning, encoding, scaling, Isolation Forest, PCA visualization
├── src/                    # Folder for Python scripts
│   ├── preprocess.py       # Data preprocessing code (cleaning, scaling, encoding)
│   ├── anomaly_detection.py  # Anomaly detection using Isolation Forest
│   ├── utils.py            # Helper functions if needed
├── requirements.txt        # List of dependencies
├── README.md               # Project description and setup instructions
└── .gitignore              # Files to ignore (data, environment files)
```

## **Usage**

### **Data Preprocessing and Anomaly detection**

The first step is preprocessing the data, which involves:
- **Loading the dataset**: Raw data is loaded from the KDD Cup 1999 dataset.
- **Encoding categorical features**: Columns like `protocol_type`, `service`, and `flag` are one-hot encoded.
- **Scaling**: Numerical features are scaled using `StandardScaler`.
- **Handling missing values**: Any missing or invalid data is replaced with `0`.

Next, we use the **Isolation Forest** algorithm for anomaly detection. This is an unsupervised model that can detect outliers (anomalies) in the data.

Run the notebook `anomaly_detection.ipynb` for 
- Preprocessing steps
- Train the **Isolation Forest** model.
- Predict anomalies.
- Visualize the anomalies using **PCA**.

```bash
jupyter notebook notebooks/data_preprocessing.ipynb
```


```bash
jupyter notebook notebooks/02_anomaly_detection.ipynb
```

### **3. Model Evaluation**

The model is evaluated based on the number of anomalies it detects in the test data. Since this is an unsupervised learning problem, we visually inspect the results using PCA to reduce the dimensions of the data to 2D and plot the anomalies.

---

## **Scripts and Modules**

### **`anomaly_detection.py`**

This module handles the data preprocessing steps, including:
- Loading the dataset.
- Encoding categorical columns.
- Scaling numerical features.
- Handling missing values.

This module performs anomaly detection using **Isolation Forest**:
- **Training the model**: Using the training data to learn the normal behavior patterns.
- **Predicting anomalies**: Predicting which instances are anomalies (outliers).
- **Visualizing the results**: Using PCA to reduce the data to 2D and plotting anomalies.


## **Output**
![Screenshot 2025-04-24 at 5 45 21 PM](https://github.com/user-attachments/assets/320a8705-a9ec-4e3c-bd5c-1d6db668b9dc)



---

