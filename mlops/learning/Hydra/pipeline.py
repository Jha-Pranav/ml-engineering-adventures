from __future__ import annotations

import preprocessors as pp
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def pipeline(config):
    match_pipe = Pipeline(
        [
            (
                "drop_fatures",
                pp.DropUnecessaryFeatures(
                    variables_to_drop=config.variables.drop_features,
                ),
            ),
            (
                "categorical_to_numerical",
                pp.CategoricalToNumerical(
                    variables=config.variables.numerical_vars_from_numerical,
                ),
            ),
            ("numerical_imputer", pp.NumericalImputer()),
            (
                "categorical_imputer",
                pp.CategoricalImputer(
                    variables=config.variables.categorical_vars,
                ),
            ),
            # ('temporal_variable',
            #    pp.TemporalVariableEstimator(
            #       variables=config.TEMPORAL_VARS,
            #        reference_variable=config.DROP_FEATURES)),
            (
                "label extraction",
                pp.LabelExtraction(
                    variables=config.variables.categorical_label_extraction,
                ),
            ),
            (
                "rare label encoder",
                pp.RareLabelCategoricalEncoder(
                    tol=0.01,
                    variables=config.variables.categorical_vars,
                ),
            ),
            (
                "categorical_encoder",
                pp.CategoricalEncoder(
                    variables=config.variables.categorical_vars,
                ),
            ),
            # ('feature hashing',
            #   FeatureHasher(n_features=10, input_type='string')),
            # ('log_transformer',
            #    pp.LogTransformer()),
            ("scaler", MinMaxScaler()),
            ("classifier", LogisticRegression()),
        ],
    )

    return match_pipe
