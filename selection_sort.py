def selection_sort(x):
    for i in range(len(x)):
        min_ind = i
        for j in range(i+1, len(x)):
            if x[min_ind] > x[j]:
                min_ind = j

        x[i], x[min_ind] = x[min_ind], x[i]
    print(x)

selection_sort([32,42,1,3,45,6,4])

