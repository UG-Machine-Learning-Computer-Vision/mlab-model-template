"""
Main file for training and testing models.
The name of the function should remain the same.
They should return the results of training and testing respectively.
Using the class TrainResults and TestResults is recommended.
"""

from typing import Any


class TrainResults:
    """Results of training."""
    def __init__(self, history: Any, metrics: dict[str, float], files: []):
        self.history = history
        self.metrics = metrics
        self.files = files

class TestResults:
    """Results of testing."""
    def __init__(self, metrics: dict[str, float], files: [], predictions: []):
        self.metrics = metrics
        self.files = files
        self.predictions = predictions

def train(
    dataset_path: str,
    parameters: dict,
    result_id: str,
) -> TrainResults:
    """
    Train a model
    This function will provide the dataset path, parameters and result_id
    and will return the results of training.
    """


    train_results = TrainResults(
        history={},
        metrics={},
        files=[],
    )

    return train_results


def test(
    dataset_path: str,
    parameters: dict,
    result_id: str,
) -> TestResults:
    """
    Test a model.
    This function will provide the dataset path, parameters and result_id
    and will return the results of testing.
    """

    test_results = TestResults(
        metrics={},
        files=[],
        predictions=[],
    )
    return test_results
