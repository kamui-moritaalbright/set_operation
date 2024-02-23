#setops
# Zachary P and Kamui M-A
#1/22 2:25 last edited

def lowercase(string, n, func): #func is going to be passed as a lambda function lamba x: chr(ord(x)+32))
    if n > 0:
        if 'A' <= string[n-1] <= 'Z':
            new_char = func(string[n-1])
            string = string[:n-1] + new_char + string[n:]
        return lowercase(string, n-1, func)
    return string

def binarysearch(array, value, start, end): #binary search function
    #this returns the index if the value is found and returns a -1 if not
    if start <= end:
        midpointIndex = (start + end) // 2
        midpointValue = array[midpointIndex]
        if midpointValue == value:
            return midpointIndex + 1
        elif midpointValue < value:
            return binarysearch(array, value, midpointIndex + 1, end)
        else:
            return binarysearch(array, value, start, midpointIndex - 1)
    else:
        return -1

def length(list): #length function that returns length of array
    return length2(list, 0)

def length2(list,n):
    if list == []:
        return n
    else:
        return length2(list[1:],n+1)

def Stringlength(string): #same function but for strings
    return Stringlength2(string, 0)

def Stringlength2(string, n):
    if string == "":
        return n
    else:
        return Stringlength2(string[1:], n + 1)

def lowerCaseArray(array, index): #this function lowercases an entire array recursively
    if index == length(array):
        return array
    array[index] = lowercase(array[index], Stringlength(array[index]), lambda x: chr(ord(x) + 32))
    return lowerCaseArray(array, index + 1)

def clearDuplicates(array, index=0,result=None): #clears duplicates from an array
    if result is None:
        result = []
    if index==length(array):
        return result
    if binarysearch((result),array[index],0,length(result)-1)==-1:
        result.append(array[index])
    return clearDuplicates(array,index+1,result)

def union (array1,array2): #this is the union function and it works
    # right now it only works on completely sorted arrays, if not
    #sorted it will not work
    #a mergesort needs to be added at the end of this because it prints
    #backwards (aka numbers then letters)
    lowerCaseArray(array1,0)
    lowerCaseArray(array2,0)
    combined_array=array1+array2;
    combined_array=clearDuplicates(combined_array)
    return combined_array

#def intersection (array1,array2):
    #lowerCaseArray(array1)
    #lowerCaseArray(array2)
    #result=[]
    #def inter (arr1,arr2,index,result):
        #if length(arr1)>length(arr2):
            #largerArray = arr1
        #else:
            #largerArray = arr2
        #if index==length(largerArray)-1:
            #return result
        #if binarysearch(arr2,arr1[index],0,length(arr2)-1)!=-1 and binarysearch(result,arr1[index],0,length(result)-1)==-1:
            #result.append(arr1[index])
        #if binarysearch(arr1,arr2[index],0,length(arr2)-1)!=-1and binarysearch(result,arr2[index],0,length(result)-1)==-1:
            #result.append(arr2[index])
        #return inter(arr1,arr2,index+1,result)
    #return result


#added
def isnum_let(ch): #return True if the character is a number/letter
  if (48<=ord(ch)<=57 or 65<=ord(ch)<=90 or 97<=ord(ch)<=122):
    return True
  else:
    return False

def isnum(ch): #return True if the character is a number
  if(48<=ord(ch)<=57):
    return True
  else:
    return False

#create an array from an input string, eliminating symbols
def process_content(content, index=0, current_string='', cu_isnum = False, cu_fraction = False, result=None):
  if result is None:
        result = []

  #base case
  if index == len(content):
      #add the last word if not empty
      if current_string:
        if(cu_isnum and current_string[-1]=='.'): #check if the period is already appended
          current_string = current_string[:-1]
        result.append(current_string)
      return result

  char = content[index]

  #check if character is a letter or digit
  if isnum_let(char):
    if(isnum(char)):
      if(cu_isnum):
        current_string += char #if it's number when a current string is a number
      else:
        if current_string:
          result.append(current_string)
        current_string = char
        cu_isnum = True;
    else:
      if(cu_isnum):
        if(current_string[-1]=='.'): #check if the period is already appended
          current_string = current_string[:-1]
        result.append(current_string)
        current_string = ''
        cu_isnum = False;
        cu_fraction = False;
      current_string += char
  else: #space/symbol encountered
    if (char == '.'): #check for fraction
      if(cu_isnum and not cu_fraction):
          current_string += char
          cu_fraction = True
          return process_content(content, index + 1, current_string, cu_isnum, cu_fraction, result)
    if current_string:
      result.append(current_string)
      current_string = ''
      cu_fraction = False
      cu_isnum = False

  return process_content(content, index + 1, current_string, cu_isnum, cu_fraction, result)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if is_number(left[left_index]) or is_number(right[right_index]):
            if is_number(left[left_index]) and is_number(right[right_index]):
                if float(left[left_index]) <= float(right[right_index]):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            elif is_number(left[left_index]):
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        else:
            if left[left_index].lower() <= right[right_index].lower():
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

    # Append any remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    #array = ["1","1","2","3","4","4","5","6","6","6","7","7","7","7","8","9"]
    #array2 = ["9","Cat","Dog","Fox","seagull","turtle","zebra"]
    input1 = "cold, 12.34 blue 5678 tree. 91011 rock 12.13 star, 91011 moon. 91.011"
    input2 = "tree, 12.34 Blue. 5678 hot. 91011 rock 12.13 star 91011 Moon. 91.012"
    array1 = process_content(input1)
    array2 = process_content(input2)
    sorted_arr1 = merge_sort(array1)
    sorted_arr2 = merge_sort(array2)
    print(merge_sort(union(sorted_arr1,sorted_arr2)))
    #print(intersection(array,array2))
if __name__ == '__main__':
    main()