from joblib import dump
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris(return_X_y=True)
y = iris[1]
X = iris[0]


clf_pipeline = [('scaling', StandardScaler()), ('clf', LogisticRegression())]
pipeline = Pipeline(clf_pipeline)

pipeline.fit(X, y)

dump(pipeline, 'models/ml/iris_dt_v1.joblib')
