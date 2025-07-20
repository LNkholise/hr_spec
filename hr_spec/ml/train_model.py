import argparse
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from hr_spec.ml.classifier import KNNClassifier
from sklearn.metrics import classification_report


def train_star_classifier(data_path: str, k: int = 3, model_output_path: str= None) -> tuple[KNNClassifier, float]:
    '''Trains a KNN classifier on the star dataset.

    This function loads a dataset from the given path, preprocesses it,
    trains a KNNClassifier, evaluates its performance.

    Args:
        data_path (str): The path to the CSV file containing the star data.
        k (int): The number of neighbors to use for the KNN classifier. Defaults to 3.


    Returns:
        tuple[KNNClassifier, float]: A tuple containing the trained model
                                     and its accuracy score on the test set.
    '''
    print(f'Loading data from {data_path}...')
    df = pd.read_csv(data_path)

    # Define required and feature columns
    required_cols = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
                     'Absolute magnitude(Mv)', 'Star type', 'Star color',
                     'Spectral Class']
    
    feature_cols = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)',
                    'Absolute magnitude(Mv)', 'Star type', 'Star color']
    
    target_col = 'Spectral Class'

    if not all(col in df.columns for col in required_cols):
        raise ValueError(f'Missing columns in dataset. Required: {required_cols}')

    # Preprocess 'Star color' by stripping whitespace and converting to categorical codes
    df['Star color'] = df['Star color'].str.strip().astype('category').cat.codes

    # Handle imbalanced classes before stratification
    class_counts = df[target_col].value_counts()
    classes_to_remove = class_counts[class_counts < 2].index 
    
    if not classes_to_remove.empty:
        print(f"Warning: Removing classes with fewer than 2 samples to allow for stratification: {list(classes_to_remove)}")
        df = df[~df[target_col].isin(classes_to_remove)]

    # Define features (X) and target (y)
    X = df[feature_cols].values
    y = df[target_col].values

    # Split data into training and testing sets, stratifying by target to maintain distribution
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42, stratify= y)

    # Train the model
    print(f'Training KNNClassifier with k={k}...')
    model = KNNClassifier(k= k)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)

    # Perfomance
    print(f'\nAccuracy: {accuracy:.3f}')
    print('\nClassification Report:')
    print(classification_report(y_test, y_pred))

    # Save the model 
    if model_output_path:
        print(f'Saving trained model to {model_output_path}...')
        joblib.dump(model, model_output_path)

    return model, accuracy


if __name__ == '__main__':
    
    # This allows the script to be run from the command line.
    parser = argparse.ArgumentParser(description='Train a KNN Star Classifier.')

    # Default path assumes the data dir is at the project root.
    default_data_path = Path(__file__).resolve().parent.parent / 'data' / '6_class.csv'
    parser.add_argument('--data-path', type= str, default= str(default_data_path), help= 'Path to the training data CSV file.')
    parser.add_argument('--k', type= int, default= 3, help= 'Number of neighbors for KNN.')
    parser.add_argument('--output-path', type= str, default= 'trained_star_classifier.pkl', help= 'Path to save the trained model.')
    args = parser.parse_args()

    train_star_classifier(data_path= args.data_path, k= args.k, model_output_path= args.output_path)

