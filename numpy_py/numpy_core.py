import numpy as np


class NumpyOperation:
      def __init__(self, arr_data_1, arr_data_2):
           
            # Creating a rank 1 Array
            arr = np.array(arr_data_1)

            print("Array with Rank 1: \n",arr)

            # Creating a rank 2 Array
          

            arr = np.array(arr_data_2)

            print("Array with Rank 2: \n", arr)


            # Creating an array from tuple
            arr_tuple = (1, 2, 3) 
                  
            arr = np.array(arr_tuple)
            print("\nArray created using "   "passed tuple:\n", arr)

            # Creating an array from tuple
            arr_tuple = (
                  (1, 2, 3),
                  (4, 5, 6)
                  )
            arr = np.array(arr_tuple)
            print("\nArray created using "   "passed tuple:\n", arr)


NumpyOperation()