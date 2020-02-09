import time
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
class mcd():
    def euclides(self, a, b):
        r = 0
        while (b > 0):
            r = b
            b = a % b
            a = r
        return a

if __name__ == '__main__':
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    max_digits= 100

    total_time = 0

    time_matrix = pd.DataFrame(columns = ["num_1","num_2","num_digits_1","num_digits_2","time"])
    df = pd.DataFrame(time_matrix["time"],index=time_matrix["num_digits_2"],columns=time_matrix["num_digits_2"])
    total_past = time.time()
    for i in range(1,max_digits+1):
      c_time = 0
      num1 = num1 + random.randint(1,9)*10**i
      for j in range(1,max_digits+1):
        #print("Los numero a analizar son {} y {}".format(num1,num2))
        past = time.time()
        mcd().euclides(num1,num2)
        c_time = time.time()-past
        time_matrix = time_matrix.append({"num_1":num1,"num_2":num2,"num_digits_1":i,"num_digits_2":j,"time": c_time}, ignore_index = True)
        num2 = num2 + random.randint(1,9)*10**i


    print("Tiempo en ejecutar los loops {} veces: {}".format((max_digits)**2 ,time.time() - total_past))
    df = time_matrix.pivot(index = "num_digits_1", columns = "num_digits_2", values = "time")
    ax = sns.heatmap(df)
    ax.invert_yaxis()
