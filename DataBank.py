import pandas as pd
import os

class DataBank:

    file_name = "blur_selection_data.csv"
    column_list = ['name','num_of_clusters','cluster_contours', 'blur_clusters','valid_image']

    def __init__(self):
        self.file_name=self.file_name
        self.index_count=None

        if os.path.isfile(self.file_name):
            # read csv
            self.df = pd.read_csv(self.file_name)
        else:
            # create a dataframe with column names
            self.df = pd.DataFrame(columns=self.column_list)
            # create the csv file
            self.df.to_csv(self.file_name, index=None)

    def insert_data(self, name, num_of_clusters, cluster_contours, blur_clusters, valid_image):
        data = [name, num_of_clusters, cluster_contours, blur_clusters, valid_image]
        self.insert_row(data)
    
    def insert_row(self,row):
        #this will insert the given row to the end of the dataframe
        self.index_count=len(self.df.index)
        self.df.loc[self.index_count] = row
        self.df.to_csv(self.file_name, index=None)

    def get_last_row(self):
        #this will return the last row as a df frame with column names
        self.index_count=len(self.df.index)
        if(self.index_count > 0):
            return self.df.loc[self.index_count - 1]
        else:
            return None

    def get_last_row_as_list(self):
        #this will return the last row as a list without the column names
        row = self.get_last_row()
        if not row is None:
            return row.tolist()
        else:
            return None



# csv_name = 'sample_csv.csv'
# X = CSV_Update(csv_name, ['a','b','c'])
# X.insert_row([5,6,7])
# last_row = X.get_last_row()
# print(last_row)
# print(last_row.tolist())




