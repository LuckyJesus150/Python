def delete():
    A = list(map(str, input('Enter a list: ').split()))

    print(A)

    value_to_delete = str(input('Enter value to delete: '))

    result = []

    for item in A:
        if item != value_to_delete:
            result.append(item)

    print(result)

    return result

delete()
