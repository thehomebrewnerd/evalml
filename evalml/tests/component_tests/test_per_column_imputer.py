import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from evalml.pipelines.components import PerColumnImputer


def test_all_strategies():
    X = pd.DataFrame([[2, 4, 6, "a"],
                      [4, 6, 8, "a"],
                      [6, 4, 8, "b"],
                      [np.nan, np.nan, np.nan, np.nan]])

    X_expected = pd.DataFrame([[2, 4, 6, "a"],
                               [4, 6, 8, "a"],
                               [6, 4, 8, "b"],
                               [4, 4, 100, "a"]])

    X.columns = ['A', 'B', 'C', 'D']
    X_expected.columns = ['A', 'B', 'C', 'D']

    strategies = {
        'A': 'mean',
        'B': 'median',
        'C': ('constant', 100),
        'D': 'most_frequent',
    }

    transformer = PerColumnImputer(impute_strategies=strategies)
    X_t = transformer.fit_transform(X)

    assert_frame_equal(X_expected, X_t, check_dtype=False)

    transformer = PerColumnImputer(impute_strategies=strategies)
    transformer.fit(X)
    X_t = transformer.transform(X)

    assert_frame_equal(X_expected, X_t, check_dtype=False)


def test_col_with_non_numeric():
    # test col with all strings
    X = pd.DataFrame([["a", "a", "a", "a"],
                      ["b", "b", "b", "b"],
                      ["a", "a", "a", "a"],
                      [np.nan, np.nan, np.nan, np.nan]])
    X.columns = ['A', 'B', 'C', 'D']

    # mean with all strings
    strategies = {'A': 'mean'}
    with pytest.raises(ValueError, match="Cannot use mean strategy with non-numeric data"):
        transformer = PerColumnImputer(impute_strategies=strategies)
        transformer.fit_transform(X)
    with pytest.raises(ValueError, match="Cannot use mean strategy with non-numeric data"):
        transformer = PerColumnImputer(impute_strategies=strategies)
        transformer.fit(X)

    # median with all strings
    strategies = {'B': 'median'}
    with pytest.raises(ValueError, match="Cannot use median strategy with non-numeric data"):
        transformer = PerColumnImputer(impute_strategies=strategies)
        transformer.fit_transform(X)
    with pytest.raises(ValueError, match="Cannot use median strategy with non-numeric data"):
        transformer = PerColumnImputer(impute_strategies=strategies)
        transformer.fit(X)

    # most frequent with all strings
    strategies = {'C': 'most_frequent'}
    transformer = PerColumnImputer(impute_strategies=strategies)

    X_expected = pd.DataFrame([["a", "a", "a", "a"],
                               ["b", "b", "b", "b"],
                               ["a", "a", "a", "a"],
                               ["a", "a", "a", "a"]])
    X_expected.columns = ['A', 'B', 'C', 'D']

    X_t = transformer.fit_transform(X)
    assert_frame_equal(X_expected, X_t, check_dtype=False)

    X_t = transformer.transform(X)
    assert_frame_equal(X_expected, X_t, check_dtype=False)

    # constant with all strings
    strategies = {'D': ('constant', 100)}
    transformer = PerColumnImputer(impute_strategies=strategies)

    X_expected = pd.DataFrame([["a", "a", "a", "a"],
                               ["b", "b", "b", "b"],
                               ["a", "a", "a", "a"],
                               ["a", "a", "a", 100]])
    X_expected.columns = ['A', 'B', 'C', 'D']

    X_t = transformer.fit_transform(X)
    assert_frame_equal(X_expected, X_t, check_dtype=False)

    X_t = transformer.transform(X)
    assert_frame_equal(X_expected, X_t, check_dtype=False)
