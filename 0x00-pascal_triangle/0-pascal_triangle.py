def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle

