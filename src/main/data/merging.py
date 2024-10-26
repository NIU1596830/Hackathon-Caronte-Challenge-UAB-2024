import pandas as pd

def merge_datasets(activitats: pd.DataFrame, notes: pd.DataFrame, trameses: pd.DataFrame) -> pd.DataFrame:
    # prepare data for merging
    activitats_prev = activitats.rename({"grade": "grade_max"}, axis=1)

    # merging
    joined1 = pd.merge(trameses, activitats_prev, on="activitat_id")
    joined2 = pd.merge(joined1, notes, on=["userid", "aula_id"])

    # data normalization
    joined2["grade"] = joined2["grade"] / joined2["grade_max"]
    joined2_cleaned = joined2.drop(labels=["grade_max"], axis=1)
    # joined2_cleaned.sort_values(by="aula_id", ascending=True).describe()

    # amount of activities done by a user for each class
    joined2_cleaned['actCount'] = joined2_cleaned.groupby(['aula_id', 'userid'])['activitat_id'].transform('nunique')

    # mean of the grades of the activities by the user for each class
    joined2_cleaned["grades_mean"] = joined2_cleaned.groupby(['aula_id', 'userid'])['grade'].transform('mean')


    return joined2_cleaned