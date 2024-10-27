
import pandas as pd
from sklearn.base import clone

def train_model_with_dataset(model, dataset: pd.DataFrame):
    (dataset_copy, target) = separate_dataset_and_target(dataset)

    # esto se hace para no editar el modelo que nos han pasado por parametro
    to_train = clone(model)
    to_train.fit(dataset_copy, target)

    return to_train

def test_model(model, dataset: pd.DataFrame) -> float:
    (dataset_copy, target) = separate_dataset_and_target(dataset)

    predicted = model.predict(dataset_copy)

    return mae(target, predicted)


def separate_dataset_and_target(dataset: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    dataset_copy = dataset.copy()

    target = dataset_copy.pop("FF_Grade")
    
    return (dataset_copy, target)

def mse(target: pd.Series, predicted: pd.Series) -> float:
    return target.sub(predicted).pow(2).mean()

def mae(target: pd.Series, predicted: pd.Series) -> float:
    return target.sub(predicted).abs().mean()

def split_by_aval_cont(dataset: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # dataset = dataset.drop(axis=1, labels=["P_Grade"])
    return (dataset[dataset['P_Grade'].isnull()].drop(axis=1, labels="P_Grade"), dataset[~dataset['P_Grade'].isnull()])
