import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 347782959  # Ваш chat ID, не меняйте название переменной
alpha = 0.01


def solution(x, y) -> bool:
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < alpha
