import numpy as np


class NumpyTutorial:

      def __init__(self):
           
            self.result = ""
           
            self.input_1 = [[1, 0], [0, 1]]
            self.input_2 = [[1, 2], [3, 4]]


      def operation(self):

            z = np.zeros(10)
            z[4] = 1
            np_rng = 10 + np.arange(99)

            #Create a 3x3 matrix with values ranging from 0 to 8

            np_3X3_data = np.arange(9).reshape(3,3)

            # Find indices of non-zero elements
            non_zero_ele = np.nonzero([0,1,2,3,4,0,0,0,])

            #Declare a 3x3 identity matrix
            _3x3_identity_matrix = np.eye(3)

            #Declare a 5x5 matrix with values 1,2,3,4,5 just below the diagonal

            _5x5_mat_with_count = np.diag(1+np.arange(5), k=0)

            # Declare a 10x10x10 array with random values
            _10x10x10_with_random = np.random.random((10,10,10))

            # Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
            _op_on_mat = np.dot(np.ones((5,3)), np.ones((3,2)))

            

            self.result = f"""
                        Version:{np.__version__} <br>
                        np zeros: {np.zeros(10)} <br>
                        np zeros except one value: {z} <br>
                        values ranging from 10 to 99: <br>{np_rng} <br> <br>
                        Create a 3x3 matrix : <br>
                        {np_3X3_data[0]} <br> 
                        {np_3X3_data[1]} <br> 
                        {np_3X3_data[2]} <br> <br>
                        Find indices of non-zero : <br>{non_zero_ele} <br> <br>
                        Declare a 3x3 identity matrix: <br>
                        {_3x3_identity_matrix[0]} <br> 
                        {_3x3_identity_matrix[1]} <br> 
                        {_3x3_identity_matrix[2]} <br> <br>
                        eclare a 5x5 matrix with values1-5: <br>
                        {_5x5_mat_with_count[0]} <br>
                        {_5x5_mat_with_count[1]} <br> 
                        {_5x5_mat_with_count[2]} <br>  
                        {_5x5_mat_with_count[3]} <br> 
                        {_5x5_mat_with_count[4]} <br> <br>

                        Declare a 10x10x10 array with random values:<br>
                        {_10x10x10_with_random}<br><br>

                        Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
                        {_op_on_mat}<br><br>

                        Reuslt is multiplication: { np.dot(self.input_1, self.input_2)}
                        """
            return self.result

      def __str__(self):
            
            return str(self.result)


print(NumpyTutorial().operation())