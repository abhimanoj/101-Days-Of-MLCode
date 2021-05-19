import numpy as np


class Multiplication:

      def __init__(self):
           
            self.result = ""
           
            self.input_1 = [[1, 0], [0, 1]]
            self.input_2 = [[1, 2], [3, 4]]


      def operation(self):
            self.result = f"""
                        Reuslt is: { np.dot(self.input_1, self.input_2)}
                        """
            return self.result

      def __str__(self):
            
            return str(self.result)