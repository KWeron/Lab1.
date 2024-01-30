import matplotlib.pyplot as plt
import numpy as np

ocena = [1, 3, 4, 6, 2, 4, 2, 1, 6, 4, 4, 5, 2, 5]
plt.hist(ocena, bins=np.arange(1, 7) , edgecolor='black', alpha=0.7)

plt.title('Rozkład ocen uczniów')
plt.xlabel('Ocena')
plt.ylabel('Liczba uczniów')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
