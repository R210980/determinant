import numpy as np
n_array=np.array([[50,29],[30,44]])
print("Matrix is:")
print(n_array)
det=np.linalg.det(n_array)
print("\nDetermination of given matrix:",int(det))
