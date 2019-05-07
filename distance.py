import numpy as np
import pandas as pd

def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        dist = []
        for centroid in model.cluster_centers_:
            dist.append(np.linalg.norm(Xa-centroid))
         
        distance.set_value(i, min(dist))
    return distance