import numpy as np


class Multiplication:

      def __init__(self):
           
            self.result = ""
           
            self.input_1 = [[1, 0], [0, 1]]
            self.input_2 = [[1, 2], [3, 4]]


      def operation(self):

            z = np.zeros(10)
            z[4] = 1
            np_rng = 10 + np.arange(99)
            self.result = f"""
                        Version:{np.__version__} <br>
                        np zeros: {np.zeros(10)} <br>
                        np zeros except one value: {z} <br>
                        values ranging from 10 to 99: <br>{np_rng} <br> <br>
                        Reuslt is multiplication: { np.dot(self.input_1, self.input_2)}
                        """
            return self.result

      def __str__(self):
            
            return str(self.result)


print(Multiplication().operation())