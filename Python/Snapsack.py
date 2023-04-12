def Snapsack(capacidad, items):
    if capacidad == 0 or not items:
        return []
    elif items[0] > capacidad:
        return Snapsack(capacidad, items[1:])
    else:
        included = Snapsack(capacidad - items[0], items[1:])
        included.append(items[0])
        not_included = Snapsack(capacidad, items[1:])
        if sum(included) > sum(not_included):
            return included
        else:
            return not_included

capacidad = 20
items = [11, 8, 7, 6, 5]
solution = Snapsack(capacidad, items)
print("La solución es:", solution)