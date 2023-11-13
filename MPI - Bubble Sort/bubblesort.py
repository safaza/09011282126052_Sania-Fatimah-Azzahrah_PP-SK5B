from mpi4py import MPI
import random
import time

start = time.time()

def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

if __name__== '__main__':
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    n = 20  # Jumlah elemen dalam array
    max_number = 100  # Rentang angka acak
    local_data = []

    # Setiap proses mendapatkan data yang berbeda
    for i in range(n):
        local_data.append(random.randint(1, max_number))

    local_data = comm.gather(local_data, root=0)

    if rank == 0:
        sorted_data = [item for sublist in local_data for item in sublist]
        print("Unsorted array is :",sorted_data)
        bubbleSort(sorted_data)
        print("Sorted array is:",sorted_data)

end = time.time()
print("Waktu dikerjakan",end-start)
