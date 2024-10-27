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

    (aval_unica, aval_cont) = training.split_by_aval_cont(merged)
    print(aval_unica)
    print(aval_cont)

    models = [
        ("Arbol de decisiones", model.decision_tree(5)),
        ("Red Neuronal", model.neural())
    ]

    avaluacions = [
        ("Unica", aval_unica),
        ("Continua", aval_cont)
    ]

    for (aval_name, aval) in avaluacions:
        print(f"Avaluacion {aval_name}")
        train, test = train_test_split(aval, test_size=0.2)
        for (model_name, model_to_train) in models:
            print(f"\tModelo {model_name}")
            trained_model = training.train_model_with_dataset(model_to_train, train)
            error = training.test_model(trained_model, test)
            print(f"\t\terror {error}")

    # print(tree.export_text(treeModel, feature_names=train.columns.drop("FF_Grade")))


if __name__ == "__main__":
    data_path = './datasets/'
    main(data_path)