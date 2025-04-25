import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    column_names = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 
        'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 
        'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 
        'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 
        'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 
        'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 
        'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 
        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 
        'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'class'
    ]
    
    # Load the dataset
    data = pd.read_csv(file_path, header=None, names=column_names)
    
    return data

def preprocess_data(data):
    # Step 1: Print original data types before preprocessing for diagnostic
    print("Data types before preprocessing:")
    print(data.dtypes)
    
    # Step 2: Remove the target variable (`class` column) before processing
    data = data.drop(columns=['class'])

    # Step 3: One-hot encode categorical columns (`protocol_type`, `service`, `flag`)
    data_encoded = pd.get_dummies(data, columns=['protocol_type', 'service', 'flag'], drop_first=True)

    # Step 4: Print data types after one-hot encoding to confirm no string columns remain
    print("Data types after one-hot encoding:")
    print(data_encoded.dtypes)

    # Step 5: Convert all boolean columns to int (True/False -> 1/0)
    bool_columns = data_encoded.select_dtypes(include=['bool']).columns
    print("Converting boolean columns to integers:")
    print(bool_columns)
    data_encoded[bool_columns] = data_encoded[bool_columns].astype(int)

    # Step 6: Convert all data to numeric, coercing errors into NaN
    data_encoded = data_encoded.apply(pd.to_numeric, errors='coerce')

    # Step 7: Fill NaN values with 0
    data_encoded = data_encoded.fillna(0)

    # Step 8: Print unique values after conversion to numeric for debugging
    print("Unique values in each column after numeric conversion:")
    for column in data_encoded.columns:
        print(f"{column}: {data_encoded[column].unique()}")

    # Step 9: Scale the numeric features
    numerical_columns = data_encoded.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    data_scaled = data_encoded.copy()
    data_scaled[numerical_columns] = scaler.fit_transform(data_encoded[numerical_columns])

    # Return the scaled data
    return data_scaled
