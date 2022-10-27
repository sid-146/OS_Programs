import pandas as pd
import numpy as np

FCFS = {
    'process_id': pd.Series(dtype= pd.Float64Dtype),
    'arrival_time': pd.series(dtype= pd.Float64Dtype),
    'burst_time': pd.Series(dtype= pd.Float64Dtype),
    'completion_time':pd.Series(dtype= pd.Float64Dtype),
    'turn_aroud_time':pd.Series(dtype= pd.Float64Dtype),
    'waiting_time':pd.Series(dtype= pd.Float64Dtype),
    'is_executed':pd.Series(dtype= pd.BooleanDtype)
}


process_runtime_records= {
    'run_id':pd.Series(dtype=pd.Int64Dtype)
}