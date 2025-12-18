from file_handler import read_csv_file, read_dtype, write_file
from stats import get_stat, get_col_min, get_col_mean, get_col_mode, get_col_median, get_col_max
import file_handler

class Dataframe:
    def __init__(self, data:dict ,  dtype:dict):
        self.dtypes = dtype
        self.data = data
        self.nulls = {}
        self.stats = {}
    
    #TODO: define read_csv(data_path, dtype_path)
    def read_csv(self , file_path , dtype_path):
        self.dtypes = read_dtype(dtype_path)
        self.data = read_csv_file(file_path , self.dtypes)


    @classmethod
    def create_frame(cls , data_path , dtypes_path):
        d = read_dtype(dtypes_path)
        data = read_csv_file(data_path , d)
        dataframe = Dataframe(data = data , dtype = d)
        return dataframe

    #TODO: define count_nulls()
    def count_nulls(self):
        self.nulls = {}
        for key in self.dtypes.keys():
            count = 0
            for value in self.data[key]:
                if value is None:
                    count+=1
            self.nulls[key] = count
        return self.nulls




    
    #TODO: define describe()
    def describe(self):
        for key , dtype in self.dtypes.items():
            if dtype!='string':
                self.stats[key]={
                    'min':get_col_min(self.data[key]) ,
                    'max': get_col_max(self.data[key]),
                    'median': get_col_median(self.data[key]),
                    'mode': get_col_mode(self.data[key]),
                    'mean': get_col_mean(self.data[key])
                }
        return self.stats

        
    #TODO: define fillna()
    def fillna(self , method = 'mean'):
        for key , dtype in self.dtypes.items() :
            if dtype=='string' :
                missing = get_col_mode(self.data[key])
            else:
                if method == 'mean' :
                    missing = get_col_mean(self.data[key])
                elif method=='median' :
                    missing = get_col_median(self.data[key])
                else:
                    print('unknown metric')
                    return


            for index , value in enumerate(self.data[key]):
                if value is None :
                    self.data[key][index] = missing



        
    #TODO: define to_csv()
    def to_csv(self , file_path):
        write_file(file_path , self.data)

                       
    
    
    
    
