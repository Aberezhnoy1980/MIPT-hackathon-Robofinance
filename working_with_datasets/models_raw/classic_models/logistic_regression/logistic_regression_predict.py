from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

def log_regression_predict_with_target(final_df:pd.DataFrame, cols_to_drop:list, model_save_dir:str, model_result_dir:str) -> None:
    
    if(len(cols_to_drop) > 0):
        final_data_df = final_df.drop(columns=cols_to_drop)        
    else:
        final_data_df = final_df
        

    variable_names = [x for x in final_data_df.columns if x != 'target']
    data = final_data_df[variable_names]
    target = final_data_df['target']

    X_train, X_test, y_train, y_test = train_test_split(data.values, target.values, random_state=42, test_size=0.3)

    file_dir = model_save_dir + 'logistic_regression_model.pkl'
    # target = test_df['target']
    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)

    log_reg_predict_train = log_reg_model.predict(X_train)
    log_reg_predict_test = log_reg_model.predict(X_test)

    print(f'LogRegression test score: {log_reg_model.score(X_test, y_test)}')
    print(classification_report(y_test, log_reg_predict_test))

    save_model_results_train = model_result_dir + 'logistic_regression_train_predict.csv'
    save_model_results_test = model_result_dir + 'logistic_regression_test_predict.csv'

    pd.Series(log_reg_predict_train).to_csv(save_model_results_train)

    pd.Series(log_reg_predict_test).to_csv(save_model_results_test)

    return log_reg_predict_test


def log_regression_predict_without_target(final_df:pd.DataFrame, cols_to_drop:list, model_save_dir:str, model_result_dir:str) -> None:    
    file_dir = model_save_dir + 'logistic_regression_model.pkl'

    if(len(cols_to_drop) > 0):
        final_data_df = final_df.drop(columns=cols_to_drop)        
    else:
        final_data_df = final_df

    data = final_data_df.values

    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)

    log_reg_predict = log_reg_model.predict(data)

    save_model_results = model_result_dir + 'logistic_regression_no_target_predict.csv'

    pd.Series(log_reg_predict).to_csv(save_model_results)

    return log_reg_predict
    
    
    
    