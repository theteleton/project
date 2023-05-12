import numpy as np
import pandas as pd

class PowerBIComparator:
    def __init__(self, data_path1, data_path2):
        self.path1 = data_path1
        self.path2 = data_path2
    def unique(self, list):
        res = []
        for x in list:
            if x not in res:
                res.append(x)

        return res

    def compare(self, df1, df2, key_word, new_feature=0):
        n_rows_1 = len(df1)
        n_rows_2 = len(df2)
        n_cols_1 = len(df1.columns)
        n_col2_2 = len(df2.columns)
        print(df1)
        print(df2)
        unique_vals = self.unique(df1[key_word].to_list() + df2[key_word].to_list())

        rows1 = []
        rows2 = []
        n_equal = 0
        visited = []
        for x in unique_vals:
            if x in df1[key_word].to_list() and x in df2[key_word].to_list():
                visited.append(x)
                rows1.append(df1.loc[df1[key_word] == x].values.flatten().tolist()[:new_feature])
                rows2.append(df2.loc[df2[key_word] == x].values.flatten().tolist()[:new_feature])
        
        for x in unique_vals:
            if x in visited:
                continue
            if x in df1[key_word].to_list():
                rows1.append(df1.loc[df1[key_word] == x].values.flatten().tolist()[:new_feature])
            else:
                rows2.append(df2.loc[df2[key_word] == x].values.flatten().tolist()[:new_feature])

        df1_new = pd.DataFrame(rows1, columns=df1.columns[:1])
        df2_new = pd.DataFrame(rows2, columns=df2.columns[:1])
        print(df1_new)
        print(df2_new)
    
    def convert_to_normal_csv():
        pass

    def input_tables(self):

        df1 = pd.read_csv(self.path1 + "/Sales quantity.csv")
        df2 = pd.read_csv(self.path2 + "/Sales quantity.csv")
        new_list1 = []
        for i in range(len(df1)):
            new_list1.append(str(df1["Month short"][i] + str(df1["Date week"][i])))
        df1["Week"] = new_list1
        new_list2 = []
        for i in range(len(df2)):
            new_list2.append(str(df2["Month short"][i] + str(df2["Date week"][i])))
        df2["Week"] = new_list2

        self.compare(df1, df2, "Week", new_feature=0)

    def create_results(self):
        pass

