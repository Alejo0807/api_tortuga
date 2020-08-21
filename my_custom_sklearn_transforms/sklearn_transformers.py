from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing


# All sklearn Transforms must have the `transform` and `fit` methods
class Transformations(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
       
        data = data.drop(labels=self.columns, axis='columns')
        return data.dropna()
        