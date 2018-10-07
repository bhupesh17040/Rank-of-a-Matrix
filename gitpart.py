# HOMEWORK ASSIGNMENT 4 - FINDING THE RANK OF A MATRIX


def Displaymatrix(A,rownum,colnum):
        for i in range(rownum):
                for j in range(colnum):
                        print(A)
                        break
                        
def swapRows(A,row1,row2):                        #FUNCTION TO SWAP TWO ROWS OF A MATRIX A
	A[row2],A[row1]=A[row1],A[row2]
	return A

def Row_Transformation(A,x,row1,row2):            #FUNCTION TO PERFORM ROW TRANSFORMATION ON ROWS OF A MATRIX
	k=len(A[row2])
	for m in range(k):
		A[row2][m]=A[row2][m] + A[row1][m]*x
	return A