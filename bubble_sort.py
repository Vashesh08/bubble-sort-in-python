def bubble_sort(data: list) -> None:
    """ Sorts a list in place."""
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        # n -= 1
        print(f"data: {data}")
        if not swapped:
            break
    print(f"comparison_count: {comparison_count}")


# a = [1, 2, 5, 6, 7, 3, 4]
# a = [3, 2, 4, 1, 5, 7, 6]
# a = list(range(70, 0, -1))
# a = [1, 2, 3, 4, 6, 5, 7]
a = [1, 2, 3, 4, 5, 6, 7]
print(len(a))

bubble_sort(a)
print(a)
