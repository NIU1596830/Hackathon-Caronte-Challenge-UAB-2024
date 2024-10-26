
import pandas as pd

def train_model_with_dataset(model, dataset: pd.DataFrame):
    (dataset_copy, target) = separate_dataset_and_target(dataset)

    model.fit(dataset_copy, target)

    return model

def test_model(model, dataset: pd.DataFrame) -> float:
    (dataset_copy, target) = separate_dataset_and_target(dataset)

    predicted = model.predict(dataset_copy)

    return mse(target, predicted)


def separate_dataset_and_target(dataset: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    dataset_copy = dataset.copy()

    target = dataset_copy.pop("FF_Grade")
    
    return (dataset_copy, target)

def mse(target: pd.Series, predicted: pd.Series) -> float:
    return target.sub(predicted).pow(2).mean()