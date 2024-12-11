from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

def log_regression_predict_with_target(data:pd.DataFrame, target:pd.Series, model_save_dir:str, model_result_dir:str) -> None:

    X_train, X_test, y_train, y_test = train_test_split(data, target.values, random_state=42, test_size=0.3)

    file_dir = model_save_dir + 'logistic_regression_model.pkl'
    # target = test_df['target']
    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)
        
    variable_names = [x for x in data.columns if x != 'application_id']

    log_reg_predict_train = log_reg_model.predict_proba(X_train[variable_names].values)
    log_reg_predict_test = log_reg_model.predict_proba(X_test[variable_names].values)

    print(f'LogRegression test score: {log_reg_model.score(X_test[variable_names].values, y_test)}')
    print(classification_report(y_test, log_reg_model.predict(X_test[variable_names].values)))

    save_model_results_train = model_result_dir + 'logistic_regression_train_predict.csv'
    save_model_results_test = model_result_dir + 'logistic_regression_test_predict.csv'
    
    log_reg_predict_train_0 = log_reg_predict_train.T[0]
    log_reg_predict_train_1 = log_reg_predict_train.T[1]
    
    log_reg_predict_test_0 = log_reg_predict_test.T[0]
    log_reg_predict_test_1 = log_reg_predict_test.T[1]
    
    predict_df_train = pd.DataFrame({'application_id': X_train['application_id'], 'predict_proba_0': log_reg_predict_train_0, 'predict_proba_1':log_reg_predict_train_1})
    predict_df_test = pd.DataFrame({'application_id': X_test['application_id'], 'predict_proba_0': log_reg_predict_test_0, 'predict_proba_1':log_reg_predict_test_1})
    

    predict_df_train.to_csv(save_model_results_train)

    predict_df_test.to_csv(save_model_results_test)

    return predict_df_train, predict_df_test


def log_regression_predict_without_target(data:pd.DataFrame, model_save_dir:str, model_result_dir:str) -> None:  
    
    variable_names = [x for x in data.columns if x != 'application_id']

    file_dir = model_save_dir + 'logistic_regression_model.pkl'

    with open(file_dir, 'rb') as file:
        log_reg_model = pickle.load(file)

    # log_reg_predict = log_reg_model.predict(data[~'application_id'])

    predict_proba = log_reg_model.predict_proba(data[variable_names].values)

    save_model_results = model_result_dir + 'logistic_regression_no_target_predict.csv'

    # pd.Series(log_reg_predict).to_csv(save_model_results)
    
    predict_proba_0 = pd.Series(predict_proba.T[0])
    
    predict_proba_1 = pd.Series(predict_proba.T[1])
    
    predict_df = pd.DataFrame({'report_dt': data.index, 'application_id':data['application_id'].values,'predict_proba_0': predict_proba_0, 'predict_proba_1':predict_proba_1})
    
    predict_df.set_index('report_dt', inplace=True)
    
    predict_df.to_csv(save_model_results)

    return predict_df
    
    
    
    