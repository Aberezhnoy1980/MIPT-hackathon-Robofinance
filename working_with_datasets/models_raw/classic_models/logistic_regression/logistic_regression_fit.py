from sklearn.linear_model import LogisticRegression
from optbinning import BinningProcess
import pandas as pd
import pickle

def log_regression_fit(data:pd.DataFrame, target:pd.Series, model_save_dir:str) -> None:
    
    log_reg_model = LogisticRegression(random_state=42, max_iter=10000)
    log_reg_model.fit(data, target)
    file_dir = model_save_dir + 'logistic_regression_model.pkl'
    print(f'LogRegression train score: {log_reg_model.score(data, target)}')

    with open(file_dir, 'wb') as file:
        pickle.dump(log_reg_model, file)
    
    