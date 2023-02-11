import Array
maxSize = 10 
arr = Array.Array(maxSize) 
arr.insert(77) 
arr.insert(99)
arr.insert(65)
arr.insert(81)
arr.insert(47)
arr.insert(21)
arr.insert(38)
arr.insert(8)
arr.insert(10)
arr.insert(27)

m=arr.getMaxNum()
arr.traverse()
print("El máximo es:", m)