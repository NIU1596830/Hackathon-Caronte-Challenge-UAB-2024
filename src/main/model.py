from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor

def decision_tree(max_depth: int):
    return DecisionTreeRegressor(max_depth=max_depth)

def neural():
    return MLPRegressor(hidden_layer_sizes=(16, 8, 4), max_iter=1000000)