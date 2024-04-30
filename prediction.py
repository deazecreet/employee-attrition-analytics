import pandas as pd
import joblib

def load_model(model_path):
    """
    Fungsi untuk memuat model yang telah disimpan.
    """
    return joblib.load(model_path)

# Function to preprocess data
def preprocess_data(df):
    # Handle categorical data (as previously identified)
    categorical_cols = ["JobLevel", "JobInvolvement", "EnvironmentSatisfaction", "PerformanceRating",
                        "StockOptionLevel", "WorkLifeBalance", "RelationshipSatisfaction", 
                        "Education", "JobSatisfaction"]
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    df_object = df.select_dtypes(include=["object"])
    object_columns = df_object.columns.tolist()

    df_category = df.select_dtypes(include=["category"])
    category_columns = df_category.columns.tolist()

    df_numeric = df.select_dtypes(include=["float64", "int64"]).drop(columns=["EmployeeId", "Attrition"])
    numeric_columns = df_numeric.columns.tolist()
    numeric_columns.remove("EmployeeCount")

    # Assuming feature extraction has been completed similarly during training
    X = pd.concat([
        df[numeric_columns], 
        df[category_columns],
        pd.get_dummies(df[object_columns], drop_first=True)
    ], axis=1)
    
    return X

def predict_attrition(data_path):
    # Load the data
    data = pd.read_csv(data_path)
    
    # Preprocess the data
    data_preprocessed = preprocess_data(data)
    
    # Predict
    predictions = model.predict(data_preprocessed)
    
    return predictions

if __name__ == '__main__':
    # Memuat model
    model = load_model('adaboost_model.pkl')
    
    predictions = predict_attrition('test_employee.csv')
    
    # Menampilkan atau menyimpan hasil prediksi
    print(predictions)
    # Misalnya menyimpan hasil prediksi ke CSV
    pd.DataFrame(predictions, columns=['Predicted Attrition']).to_csv('attrition_test_employee.csv', index=False)
