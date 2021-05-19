import numpy as np


class NumpyOperation:

      def __init__(self, arr_data_1, arr_data_2):
           
            self.result = ""
            # Creating a rank 1 Array
            self.arr = np.array(arr_data_1)

            self.result = f"""
                              Array with Rank 1: {self.arr}
                           """


      def operation(self):
            pass

      def __str__(self):
            return str(self.result)