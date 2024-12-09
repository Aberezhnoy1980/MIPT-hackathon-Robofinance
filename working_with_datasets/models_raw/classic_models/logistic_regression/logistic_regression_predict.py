from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

def log_regression_predict_with_target(test_data:pd.DataFrame, test_target:pd.Series, model_save_dir:str) -> None:

    file_dir = model_save_dir + 'logistic_regression_model.pkl'
    # target = test_df['target']
    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)

    log_reg_predict = log_reg_model.predict(test_data)
    print(f'LogRegression test score: {log_reg_model.score(test_data, test_target)}')

    return log_reg_predict


def log_regression_predict_without_target(test_df:pd.DataFrame, model_save_dir:str) -> None:    
    file_dir = model_save_dir + 'logistic_regression_model.pkl'
    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)
    log_reg_predict = log_reg_model.predict(test_df)

    return log_reg_predict
    
    
    
    