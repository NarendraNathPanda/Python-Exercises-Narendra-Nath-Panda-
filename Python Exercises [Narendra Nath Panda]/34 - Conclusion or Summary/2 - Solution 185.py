def Narendra(y_true, y_pred):
    return round(sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)]) / len(y_true), 3)