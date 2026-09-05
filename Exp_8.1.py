import numpy as np

img1=np.full((3,3,3),100,dtype=np.uint8)

img2=np.full((3,3,3),10,dtype=np.uint8)

print("---INITIAL DATA---")
print(f"Image 1 : \n{img1}")
print(f"Image 2 : \n{img2}")

#MATRIX ADDN
added = img1 + img2

#MATRIX SUB
subbed = img1 - img2

#MATRIX MUL
multiplied = img1 * 2

colour_filter = np.array([[1,0,0],
                          [0,1,0],
                          [0,0,1.5]])
matrix_mul=img1 @colour_filter

#MATRIX TRANSPOSE
transposed = img1.transpose(1,0,2)


print("~~~RESULTS~~~")
print(f"ADDITION :\n{added}")
print(f"SUBSTRACTION (100-10) :\n{subbed}")
print(f"MULTIPLICATION (100*2) :\n{multiplied}")
print(f"MATRIX MULTIPLICATION :\n{matrix_mul}")
print(f"ORIGINAL SHAPE :\n{img1.shape}")
print(f"TRANSPOSED SHAPE :\n{transposed.shape}")