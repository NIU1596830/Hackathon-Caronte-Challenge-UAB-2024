import pandas as pd

def load_notes(data_path: str) -> pd.DataFrame:
    # cargamos notes
    notes = pd.read_csv(data_path + 'notes.csv', encoding='UTF-8', sep=';')
    # conversion de tipo de datos
    notes_clean['P_Grade'] = pd.to_numeric(notes_clean['P_Grade'].replace(',', '.', regex=True), errors='coerce')
    notes_clean['F_Grade'] = pd.to_numeric(notes_clean['F_Grade'].replace(',', '.', regex=True), errors='coerce')
    notes_clean['R_Grade'] = pd.to_numeric(notes_clean['R_Grade'].replace(',', '.', regex=True), errors='coerce')

    # data cleansing
    notes["avalContinua"] = notes['P_Grade_Date'].notnull()
    notes_clean = notes.drop(labels=["P_Grade_Date"], axis=1)

    notes_clean = notes_clean.drop(labels=["F_Grade_Date"], axis=1)
    notes_clean = notes_clean.drop(labels=["R_Grade_Date"], axis=1)

    notes_clean = notes_clean.dropna(subset=['F_Grade', "R_Grade"], how="all")

    # SE PUEDEN APROBAR ASIGNATURAS SOLO PRESENTANDOTE A LA RECUPERACIÓN
    recuperacion = notes[notes['F_Grade'].isna() & notes['R_Grade'].notna()]

    filtro = notes[notes['P_Grade'].notna() & notes['P_Grade_Date'].isna()]

    # put a flag for the passed grades
    notes_clean["passed"] = (notes_clean["F_Grade"] >= 5) | (notes_clean["R_Grade"] >= 5)


    notes_clean