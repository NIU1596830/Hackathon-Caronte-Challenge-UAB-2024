import data.activitats
import data.notes
import data.trameses
import data.merging
import model
import training
import inference

from sklearn.model_selection import train_test_split
import sklearn.tree as tree


def main(data_path: str):

    activitats = data.activitats.load_activitats(data_path)
    notes = data.notes.load_notes(data_path)
    trameses = data.trameses.load_trameses(data_path)

    merged = data.merging.merge_datasets(activitats, notes, trameses)
    print(merged)


    treeModel = model.decision_tree(5)

    train, test = train_test_split(merged, test_size=0.2)

    treeModel = training.train_model_with_dataset(treeModel, train)

    error = training.test_model(treeModel, test)

    print(f"error {error}")
    print(tree.export_text(treeModel, feature_names=train.columns.drop("FF_Grade")))


if __name__ == "__main__":
    data_path = './datasets/'
    main(data_path)