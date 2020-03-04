from skopt.space import Integer, Real

from evalml.model_family import ModelFamily
from evalml.pipelines import PipelineBase


class CatBoostRegressionPipeline(PipelineBase):
    """
    CatBoost Pipeline for regression problems.
    CatBoost is an open-source library and natively supports categorical features.

    For more information, check out https://catboost.ai/

    Note: impute_strategy must support both string and numeric data
    """
    name = "CatBoost Regressor w/ Simple Imputer"
    model_family = ModelFamily.CATBOOST
    component_graph = ['Simple Imputer', 'CatBoost Regressor']
    problem_types = ['regression']
    hyperparameters = {
        "impute_strategy": ["most_frequent"],
        "n_estimators": Integer(10, 1000),
        "eta": Real(0, 1),
        "max_depth": Integer(1, 8),
    }

    def __init__(self, objective, parameters, number_features=0, random_state=0, n_jobs=-1):
        super().__init__(objective=objective,
                         parameters=parameters,
                         number_features=number_features,
                         random_state=random_state,
                         n_jobs=n_jobs)
