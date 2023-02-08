""""The filter() function returns an iterator were the items are filtered through a
function to test if the item is accepted or not."""

#Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x >= 18:
    return True
  else:
    return False

adults = filter(myFunc,ages)

print(list(adults))
# for x in adults:
#   print(x)