import pandas as pd

def load_trameses(data_path: str) -> pd.DataFrame:
    # cargamos notes
    trameses = pd.read_csv(data_path + 'trameses.csv', encoding='latin-1', sep=',')

    # data cleansing

    trameses_clean = trameses.drop(labels=["grader"], axis=1)

    trameses_clean["grade"] = trameses_clean["grade"].fillna(0) #CAMBIEM NULLS DE GRADES A 0

    # data enchancing
    timestamp_min = trameses_clean.groupby(['activitat_id', 'userid'])['datesubmitted'].transform('min')
    timestamp_max = trameses_clean.groupby(['activitat_id', 'userid'])['datesubmitted'].transform('max')
    trameses_clean['timediff'] = (timestamp_max - timestamp_min)
    trameses_clean = trameses_clean.sort_values(by=['grade','datesubmitted'], ascending=[False, True])

    # eliminem files de la mateixa activitat i usuari
    # i mantenim la fila amb nota mes alta y que ha trigat menys, amb prioritat sobre la nota mes alta
    trameses_clean = trameses_clean.drop_duplicates(subset=['activitat_id', 'userid'], keep='first')
    trameses_clean = trameses_clean.drop(labels=["datesubmitted"], axis=1)

    return trameses_clean
