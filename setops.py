#!/usr/bin/env python3
#setops
# Zachary P and Kamui M-A
#1/22 3:14 last edited
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def lowercase(string, n, func): #func is going to be passed as a lambda function lamba x: chr(ord(x)+32))
    if n > 0:
        if 'A' <= string[n-1] <= 'Z':
            new_char = func(string[n-1])
            string = string[:n-1] + new_char + string[n:]
        return lowercase(string, n-1, func)
    return string

def binarysearch(array, value, start, end, equals,lessthan): #binary search function
    #this returns the index if the value is found and returns a -1 if not
    if start <= end:
        midpointIndex = (start + end) // 2
        midpointValue = array[midpointIndex]
        if equals(midpointValue,value):
            return midpointIndex + 1
        elif lessthan(midpointValue,value):
            return binarysearch(array, value, midpointIndex + 1, end,lambda x,y:x==y,lambda x,y:x<y)
        else:
            return binarysearch(array, value, start, midpointIndex - 1,lambda x,y:x==y,lambda x,y:x<y)
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
    if binarysearch((result),array[index],0,length(result)-1,lambda x,y:x==y,lambda x,y:x<y)==-1:
        result.append(array[index])
    return clearDuplicates(array,index+1,result)

def union (array1,array2): #this is the union function and it works
    array1 =process_content(array1)
    array2= process_content(array2)
    array1= merge_sort(array1)
    array2= merge_sort(array2)
    lowerCaseArray(array1,0)
    lowerCaseArray(array2,0)
    combined_array=array1+array2;
    combined_array=clearDuplicates(combined_array)
    combined_array=merge_sort(combined_array)
    return combined_array

def intersection (array1,array2):
    def inter(array1,array2,result=[],index=0):
        if length(array1)<length(array2):
            boundaryIndex=length(array1)-1
            nonboundaryArray=array2;
        else:
            boundaryIndex = length(array2) - 1
            nonboundaryArray=array1
        if index==length(nonboundaryArray):
            return result
        if boundaryIndex==length(array2) - 1:
            if binarysearch(array2,array1[index],0,length(array2)-1,lambda x,y:x==y,lambda x,y:x<y)!=-1 and binarysearch(result,array1[index],0,length(result)-1,lambda x,y:x==y,lambda x,y:x<y)==-1:
                result.append(array1[index])
        else:
            if binarysearch(array1,array2[index],0,length(array1)-1,lambda x,y:x==y,lambda x,y:x<y)!=-1 and binarysearch(result,array2[index],0,length(result)-1,lambda x,y:x==y,lambda x,y:x<y)==-1:
                result.append(array2[index])
        return inter(array1,array2,result,index+1)
    array1 = process_content(array1)
    array2 = process_content(array2)
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    lowerCaseArray(array1, 0)
    lowerCaseArray(array2, 0)
    combined_array= inter(array1,array2)
    combined_array=clearDuplicates(combined_array)
    combined_array=merge_sort(combined_array)
    return combined_array

def difference (arr1, arr2):
    def diff(array1, array2, result=[], index=0):
        if index == length(array1)-1:
            return result
        if binarysearch(array2, array1[index], 0, length(array2) - 1, lambda x, y: x == y,lambda x, y: x < y) == -1 and binarysearch(result, array1[index], 0, length(result) - 1,lambda x, y: x == y, lambda x, y: x < y) == -1:
                result.append(array1[index])
        return diff(arr1, arr2, result, index + 1)
    arr1 = process_content(arr1)
    arr2 = process_content(arr2)
    arr1 = lowerCaseArray(arr1,0)
    arr2 = lowerCaseArray(arr2,0)
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    arr1 = clearDuplicates(arr1)
    arr2 = clearDuplicates(arr2)
    lowerCaseArray(arr1,0)
    lowerCaseArray(arr2,0)
    combined_arr = diff(arr1, arr2)
    combined_arr = clearDuplicates(combined_arr)
    combined_arr = merge_sort(combined_arr)
    return combined_arr

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

    return merge(left_half, right_half, 0, 0)

def merge(left, right, left_index, right_index):
    result = []

    if left_index < length(left) and right_index < length(right):
        if is_number(left[left_index]) or is_number(right[right_index]):
            if is_number(left[left_index]) and is_number(right[right_index]):
                if float(left[left_index]) <= float(right[right_index]):
                    result.append(left[left_index])
                    return result + merge(left, right, left_index + 1, right_index)
                else:
                    result.append(right[right_index])
                    return result + merge(left, right, left_index, right_index + 1)
            elif is_number(left[left_index]):
                result.append(left[left_index])
                return result + merge(left, right, left_index + 1, right_index)
            else:
                result.append(right[right_index])
                return result + merge(left, right, left_index, right_index + 1)
        else:
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                return result + merge(left, right, left_index + 1, right_index)
            else:
                result.append(right[right_index])
                return result + merge(left, right, left_index, right_index + 1)

    # If one of the arrays is exhausted, append the remaining elements of the other
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
    import sys
    args = sys.argv[1].split(';')
    set1_filename = args[0].split('=')[1]
    set2_filename = args[1].split('=')[1]
    operation = args[2].split('=')[1]
    set1_content = read_file(set1_filename)
    set2_content = read_file(set2_filename)
    if operation == 'difference':
        result = difference(set1_content, set2_content)
    elif operation == 'union':
        result = union(set1_content, set2_content)
    elif operation == 'intersection':
        result = intersection(set1_content, set2_content)
    else:
        print("Invalid operation. Supported operations are: difference, union, intersection")
    with open("result.txt", 'w') as result_file:
        result_file.write('\n'.join(result))
if __name__ == '__main__':
    main()