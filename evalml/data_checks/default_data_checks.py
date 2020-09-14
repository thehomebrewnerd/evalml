from .data_checks import DataChecks
from .highly_null_data_check import HighlyNullDataCheck
from .id_columns_data_check import IDColumnsDataCheck
from .invalid_targets_data_check import InvalidTargetDataCheck
from .label_leakage_data_check import LabelLeakageDataCheck
from .no_variance_data_check import NoVarianceDataCheck


class DefaultDataChecks(DataChecks):
    """A collection of basic data checks that is used by AutoML by default.
    Includes HighlyNullDataCheck, IDColumnsDataCheck, LabelLeakageDataCheck, InvalidTargetDataCheck,
    and NoVarianceDataCheck."""

    def __init__(self, problem_type):
        """
        A collection of basic data checks.
        Arguments:
            problem_type (str): The problem type that is being validated. Can be regression,
        """
        super().__init__([HighlyNullDataCheck, IDColumnsDataCheck,
                          LabelLeakageDataCheck, InvalidTargetDataCheck, NoVarianceDataCheck],
                         data_check_params={"InvalidTargetDataCheck": {"problem_type": problem_type}})
