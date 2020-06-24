import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        else:
            return (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        traceSum = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    traceSum += self[i][j]
        return traceSum
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        if self.h == self.w == 1:
            if(self[0][0] == 0):
                inverse.append([0])
            else:
                inverse.append([1/self.g[0][0]])
        else:
            if(self.determinant() == 0):
                raise ValueError('The denominator of a fraction cannot be zero')
            else:
                over = 1/self.determinant()
                inverse=[
                    [1* over*self[1][1], -1 *over * self[0][1]],
                    [-1* over *self[1][0], 1 * over* self[0][0]]
                    ]
        return Matrix(inverse)
    

    def T(self):
        matrix_transpose = zeroes(self.h,self.w)
        for i in range(self.w):
            for j in range(self.h):
                matrix_transpose[i][j] = self.g[j][i]        
    
        return matrix_transpose
      
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        addition = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                addition[i][j] = self[i][j] + other[i][j]
        return addition

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        negative = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                negative[i][j] = -1 * self.g[i][j]
        return negative

    def __sub__(self, other):
        
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        sub = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                sub[i][j] = self[i][j] - other[i][j]
        return sub
    

    def __mul__(self, other):
        
        def dot_product(vector_one, vector_two):
            result = 0
            for i in range(len(vector_one)):
                result = result + (vector_one[i] * vector_two[i])
            return result
            
        def get_row(matrix, row):
            return matrix[row]

        def get_column(matrix, column_number):
            column = []
            for i in range(matrix.h):
                column.append(matrix[i][column_number])
            return column
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        m_rows = self.h            
        p_columns = other.w

        product = zeroes(m_rows, p_columns)

        for i in range(m_rows):
            for j in range(p_columns):
                product[i][j] = dot_product(get_row(self,i), get_column(other,j))
        return product

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        resfinal = zeroes(self.h, self.w)
        if isinstance(other, numbers.Number):
            pass
            for i in range(self.h): 
                for j in range(self.w):
                    resfinal[i][j] = other * self.g[i][j]
            return resfinal
     
            
