import data.activitats
import data.notes
import data.trameses
import data.merging


def main(data_path: str):

    activitats = data.activitats.load_activitats(data_path)
    notes = data.notes.load_notes(data_path)
    trameses = data.trameses.load_trameses(data_path)

    merged = data.merging.merge_datasets(activitats, notes, trameses)

    print(merged)


if __name__ == "__main__":
    data_path = './datasets/'
    main(data_path)