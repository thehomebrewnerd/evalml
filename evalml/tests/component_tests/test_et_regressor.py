import numpy as np
import pytest
from sklearn.ensemble import ExtraTreesRegressor as SKExtraTreesRegressor

from evalml.exceptions import MethodPropertyNotFoundError
from evalml.model_family import ModelFamily
from evalml.pipelines.components.estimators.regressors import ExtraTreesRegressor
from evalml.problem_types import ProblemTypes


def test_model_family():
    assert ExtraTreesRegressor.model_family == ModelFamily.EXTRA_TREES


def test_problem_types():
    assert ProblemTypes.REGRESSION in ExtraTreesRegressor.supported_problem_types
    assert len(ExtraTreesRegressor.supported_problem_types) == 1


def test_fit_predict(X_y):
    X, y = X_y

    sk_clf = SKExtraTreesRegressor()
    sk_clf.fit(X, y)
    y_pred_sk = sk_clf.predict(X)

    clf = ExtraTreesRegressor()
    clf.fit(X, y)
    y_pred = clf.predict(X)

    np.testing.assert_almost_equal(y_pred, y_pred_sk, decimal=5)


def test_feature_importances(X_y):
    X, y = X_y

    # testing that feature importances can't be called before fit
    clf = ExtraTreesRegressor()
    with pytest.raises(MethodPropertyNotFoundError):
        feature_importances = clf.feature_importances

    sk_clf = SKExtraTreesRegressor(random_state=0)
    sk_clf.fit(X, y)
    sk_feature_importances = sk_clf.feature_importances_

    clf.fit(X, y)
    feature_importances = clf.feature_importances

    np.testing.assert_almost_equal(sk_feature_importances, feature_importances, decimal=5)