import numpy as np
import pandas as pd
import math
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

    def compare(self, df1, df2, key_word, key_id, new_feature=0):
        n_rows_1 = len(df1)
        n_rows_2 = len(df2)
        n_cols_1 = len(df1.columns)
        n_cols_2 = len(df2.columns)
        unique_columns = self.unique(df1.columns.to_list() + df2.columns.to_list())
        print(unique_columns)
        dict1 = {}
        dict2 = {}
        visited = []
        for x in unique_columns:
            if x in df1.columns.to_list() and df2.columns.to_list():
                dict1[x] = list(df1[x].values)
                dict2[x] = list(df2[x].values)
                visited.append(x)

        for x in unique_columns:
            if x in visited:
                continue
            if x in df1.columns.to_list() :
                dict1[x] = list(df1[x].values)
            else:    
                dict2[x] = list(df2[x].values)

        df1 = pd.DataFrame(dict1, columns=dict1.keys())
        df2 = pd.DataFrame(dict2, columns=dict2.keys())

        unique_vals = self.unique(df1[key_word].to_list() + df2[key_word].to_list())

        rows1 = []
        rows2 = []
        n_equal = 0
        visited = []
        for x in unique_vals:
            if x in df1[key_word].to_list() and x in df2[key_word].to_list():
                visited.append(x)
                rows1.append(df1.loc[df1[key_word] == x].values.flatten().tolist())
                rows2.append(df2.loc[df2[key_word] == x].values.flatten().tolist())
        
        for x in unique_vals:
            if x in visited:
                continue
            if x in df1[key_word].to_list():
                rows1.append(df1.loc[df1[key_word] == x].values.flatten().tolist())
            else:
                rows2.append(df2.loc[df2[key_word] == x].values.flatten().tolist())

        df1_new = pd.DataFrame(rows1, columns=df1.columns)
        df2_new = pd.DataFrame(rows2, columns=df2.columns)
        if new_feature == 1:
            df1_new = df1_new.drop(df1_new.columns[-1], axis=1)
            df2_new = df2_new.drop(df2_new.columns[-1], axis=1)

        dict_delta = {}
        dict_color = {}
        diff_col = 1
        for x in self.unique(df1_new.columns.to_list() + df2_new.columns.to_list()):
            if x in key_id:
                continue
            
            if x in df1_new.columns.to_list() and x in df2_new.columns.to_list():
                dict_color[x] = []
                dict_delta[x] = []
                for i in range(max(len(df1), len(df2))):
                    if i < min(len(df1), len(df2)):
                        value1 = df1[x][i]
                        value2 = df2[x][i]
                        if not isinstance(value1, str) and not isinstance(value2, str):
                            if math.isnan(value1) or math.isnan(value2):
                                if math.isnan(value1) and math.isnan(value2):
                                    dict_color[x].append('00FF00')
                                    dict_delta[x].append("Both values NaN")
                                else:
                                    dict_color[x].append('FF0000')
                                    dict_delta[x].append("One of the value NaN")
                                continue
                        is_currency1 = ""
                        is_currency2 = ""
                        if isinstance(value1, str):
                            if not value1[0].isdigit():
                                is_currency1 = value1[0]
                                value1 = float(value1[1:])
                            elif not value1[-1].isdigit():
                                is_currency1 = value1[-1]
                                value1 = float(value1[:-2])

                        if isinstance(value2, str):
                            if not value2[0].isdigit():
                                is_currency2 = value2[0]
                                value2 = float(value2[1:])
                            elif not value2[-1].isdigit():
                                is_currency2 = value2[-1]
                                value2 = float(value2[:-2])  
                        value2 = float(value2)
                        value1 = float(value1)
                        diff = abs(value1 - value2)

                        if is_currency1 != is_currency2:
                            dict_color[x].append('FF0000')
                            dict_delta[x].append(str(diff) + " " + "(different currencies)")
                        else:
                            if diff == 0:
                                dict_color[x].append('00FF00')
                            else:
                                dict_color[x].append('FF0000')
                            dict_delta[x].append(str(diff))
                    else:
                        dict_color[x].append('FF0000')
                        dict_delta[x].append("Different rows")

            else:
                dict_color["diff_column" + "_" + str(diff_col)] = []
                dict_delta["diff_column" + "_" + str(diff_col)] = []
                for i in range(max(len(df1), len(df2))):
                    dict_color["diff_column" + "_" + str(diff_col)].append('FF0000')
                    dict_delta["diff_column" + "_" + str(diff_col)].append("Different columns")
                dif_col += 1 

        dict_num = {}
        dict_num_col = {}
        
        dict_num["Number of rows"] = [abs(n_rows_1 - n_rows_2)]
        if n_rows_2 != n_rows_1:
            dict_num_col["Number of rows"] = ['FF0000']
        else:
            dict_num_col["Number of rows"] = ['00FF00']

        dict_num["Number of columns"] = [abs(n_cols_1 - n_cols_2)]
        if n_cols_2 != n_cols_1:
            dict_num_col["Number of columns"] = ['FF0000']
        else:
            dict_num_col["Number of columns"] = ['00FF00']    

        delta_df = pd.DataFrame(dict_delta, columns=dict_delta.keys())
        delta_df_np = pd.DataFrame(dict_color, columns=dict_color.keys()).to_numpy()
        num_df = pd.DataFrame(dict_num, columns=dict_num.keys())
        num_df_np = pd.DataFrame(dict_num_col, columns=dict_num_col.keys()).to_numpy()
        return df1_new, df2_new, n_rows_1, n_rows_2, n_cols_1, n_cols_2, delta_df, delta_df_np, num_df, num_df_np
    
    
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
        return self.compare(df1, df2, "Week", key_id=["Month short", "Date week"], new_feature=1)
        

    def create_results(self, df1_new, df2_new, n_rows_1, n_rows_2, n_cols_1, n_cols_2, delta_df, delta_df_np, num_df, num_df_np):
        pass

