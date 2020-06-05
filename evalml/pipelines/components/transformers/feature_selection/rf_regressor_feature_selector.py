import numpy as np
from sklearn.base import clone as sk_clone
from sklearn.ensemble import RandomForestRegressor as SKRandomForestRegressor
from sklearn.feature_selection import SelectFromModel as SkSelect
from skopt.space import Real

from .feature_selector import FeatureSelector


class RFRegressorSelectFromModel(FeatureSelector):
    """Selects top features based on importance weights using a Random Forest regressor"""
    name = 'RF Regressor Select From Model'
    hyperparameter_ranges = {
        "percent_features": Real(.01, 1),
        "threshold": ['mean', -np.inf]
    }

    def __init__(self, number_features=None, n_estimators=10, max_depth=None,
                 percent_features=0.5, threshold=-np.inf, n_jobs=-1, random_state=0):
        max_features = None
        if number_features:
            max_features = max(1, int(percent_features * number_features))
        parameters = {"percent_features": percent_features,
                      "threshold": threshold,
                      "number_features": number_features}
        estimator = SKRandomForestRegressor(random_state=random_state,
                                            n_estimators=n_estimators,
                                            max_depth=max_depth,
                                            n_jobs=n_jobs)
        feature_selection = SkSelect(estimator=estimator,
                                     max_features=max_features,
                                     threshold=threshold)

        super().__init__(parameters=parameters,
                         component_obj=feature_selection,
                         random_state=random_state)

    def clone(self):
        cloned_obj = RFRegressorSelectFromModel(number_features=self.parameters['number_features'],
                                                percent_features=self.parameters['percent_features'],
                                                threshold=self.parameters['threshold'],
                                                random_state=self.random_state)
        cloned_feature_selector = sk_clone(self._component_obj)
        cloned_obj._component_obj = cloned_feature_selector
        return cloned_obj
