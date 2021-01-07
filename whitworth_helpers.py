import numpy as np
import pandas as pd

def fitTable(fitParam, fitCov, paramLabels = ['slope', 'intercept']):
    return pd.DataFrame(data = [fitParam, 2*np.sqrt(np.diagonal(fitCov))], columns = paramLabels, index = ['value', 'uncertainty'])