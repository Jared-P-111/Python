
def countdown(num):
  list = []
  for i in range(num, -1, -1):
    list.append(i)
  return list

print(countdown(5))

def print_and_return(list):
  print("first print -> ", list[0])
  return list[1]

list = [1, 2]
print(print_and_return(list))

def first_plus_length(list):
  print("first_plus_length -> ", list[0] + len(list) - 1)


first_plus_length(list)

def values_greater_than_second(list):
  new_list = []
  for i in range(len(list)):
    if(list[i] > list[1]):
      new_list.append(list[i])
  return new_list

print(values_greater_than_second([0, 3, 4, 7, 1, 2]))

def this_len_that_value(list):
  new_list = []
  for i in range(list[1]):
    new_list.append(list[0])

  return new_list

print(this_len_that_value([3, 5]))