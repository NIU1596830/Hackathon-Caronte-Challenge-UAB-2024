import pandas as pd

def load_activitats(data_path: str) -> pd.DataFrame:
    # cargamos activitats
    activitats = pd.read_csv(data_path + 'activitats.csv', encoding='latin-1', sep=',')
    
    # data cleansing
    activitats_clean = activitats.drop(labels=["activitat"], axis=1)

    # data enchancement
    activitats_clean['actTotal'] = activitats_clean.groupby('aula_id')['activitat_id'].transform('nunique')

    return activitats_clean
