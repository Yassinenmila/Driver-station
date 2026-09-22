from .cleaning import x,y
from sklearn.model_selection import train_test_split
import pandas as pd

x_train, x_test, y_train, x_test= train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=10
)
