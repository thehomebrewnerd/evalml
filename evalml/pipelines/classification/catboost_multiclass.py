from evalml.pipelines import MulticlassClassificationPipeline


class CatBoostMulticlassClassificationPipeline(MulticlassClassificationPipeline):
    """
    CatBoost Pipeline for multiclass classification.
    CatBoost is an open-source library and natively supports categorical features.

    For more information, check out https://catboost.ai/
    Note: impute_strategy must support both string and numeric data
    """
    component_graph = ['Simple Imputer', 'CatBoost Classifier']
    custom_hyperparameters = {
        'Simple Imputer': {
            "impute_strategy": ["most_frequent"],
        }
    }
