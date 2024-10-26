from sklearn.tree import DecisionTreeRegressor

def decision_tree(max_depth: int):
    return DecisionTreeRegressor(max_depth=max_depth)
