#John Vincent Marata, Giselle Nodalo, JM Santiago ADVDISC S18 class
class Vector(object):
    #Create Vector
    def __init__(self, array, dimension = None):
        self.__dim = 0
        self.__vector = []
        if dimension == None:
        #Store dimension
            self.__dim = array
        # Create Zero Vector of x dim
            self.__vector = [0] * self.__dim                          
        elif dimension != None :
            self.__dim = dimension
            self.__vector = array

    #getters 
    def get_dim(self):
        return self.__dim

    def get_vector(self):
        return self.__vector
        
    #Scale a Vector
    def scale(self,scalar):
        for i in range(self.__dim):
            self.__vector[i] = self.__vector[i]* scalar
        print('Scaled Vector:\n')        
        self.display()

    #Check Addend Dimension
    def checkDimension(self,addend):
        match = False
        #if addend rows == matrix rows
        if addend.get_dim() == self.__dim:
            match = True
        else: match = False
        return match

    #Vector Addition
    def add(self, addend):
        if self.checkDimension(addend) is False:
            print('Addend Vector incompatible for Vector Addition')
        elif self.checkDimension(addend) is True:
            print('Before Vector Addition:\n')
            self.display()
            temp = addend.get_vector()
            for k in range(len(self.__vector)):
                self.__vector[k] = self.__vector[k]+ temp[k]
            print('After Vector Addition:\n')
            self.display()    
    
    #Display Matrix
    def display(self):
        print(str(self.__vector) + '\n')

    #Display dimension
    def printdim(self):
        print('Vector Dimension: ' + str(self.__dim))

    # Gauss Jordan Function
    @staticmethod
    def Gauss_Jordan(vecList, dim, c):
        if dim <= 0:
            return None
        # making Row echelon form
        # For loop is based on height
        for i in range(len(vecList)):
            # list of index that has been done
            # To find non-zero term
            # index, the non-zero term's index
            found = 0
            for y in range(len(vecList)):
                if vecList[y][i] != 0:
                    found = 1
                    index = y
                    if y in ListDone:
                        found = 0
                if found == 1:
                    break
            # make the non-zero term "1"
            # vecList[index][i] is the first number in the list
            if found == 1:
                Divide = vecList[index][i]
                for y in range(len(vecList[index])):
                    vecList[index][y] = vecList[index][y] / Divide
                c[index] = c[index] / Divide
                ListDone.append(index)
                # scale and reduce
                for y in range(len(vector)):
                    # skip the zero term and the one being used to minus
                    if vecList[y][i] != 0 and y not in ListDone:
                        Scale = vecList[y][i]
                        for z in range(len(vecList[y])):
                            vecList[y][z] = (vecList[index][z] * Scale) - vecList[y][z]
                        c[y] = (c[index] * Scale) - c[y]
        # End of row echelon form
        for i in range(len(vecList) - 1, 0, -1):
            print(i)
            found = 0
            for y in range(len(vecList) - 1, 0, -1):
                if vecList[y][i] == 1:
                    found = 1
                    index = y
                if found == 1:
                    break
            if found == 1:
                # scale and reduce
                for y in range(len(vecList)):
                    # skip the zero term and the one being used to minus
                    if vecList[y][i] != 0 and y != index:
                        Scale = vecList[y][i]
                        vecList[y][i] = 0
                        c[y] = Scale - c[y]
        # check if there is all zero value
        for y in range(len(vecList)):
            if 1 not in vecList[y]:
                return None
        print(c)
        return c

    @staticmethod
    def span(vecList, dim):
        c = [0] * dim
        Vector.Gauss_Jordan(vecList, dim, c)
        holder = len(vecList)
        for vec in vecList:
            if all(v == 0 for v in vec):
                holder = holder - 1
        return holder
