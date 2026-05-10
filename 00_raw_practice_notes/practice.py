# DSA-PYTHON-PRACTICE

# import string
# n=int(input())
# a=reversed(string.ascii_lowercase)
# a=string.ascii_uppercase
# print(a)
# for i in range(n):
#     print()
# from lib2to3.pytree import Node
from asyncio import Queue
from ipaddress import collapse_addresses
from multiprocessing.managers import BaseManager
from operator import truediv

# n=int(input())
# c='*'
# for i in range(2,(n//2)+1):
#     a = (2 * i - 1)
#     print((c*a).center(n,'-'))


# a='abcdefg'
# print(a[2:2:-1])
# import string
#
# def print_rangoli(n):
#     alpha = string.ascii_lowercase
#     width = 4 * n - 3
#     rows = []
#
#     # Create upper half rows (including middle)
#     for i in range(n):
#         left = alpha[n-1 : n-i-1 : -1]   # decreasing letters
#         right = alpha[n-i : n]           # increasing letters
#         row = "-".join(left + right)
#         rows.append(row.center(width, '-'))
#
#     # Print top + bottom mirror (without repeating center line)
#     print("\n".join(rows[::-1] + rows[1:]))
# n=int(input())
# print_rangoli(n)

# a='abcdefgh'
# print(a[-2::-1])

# import string
#
# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#     width = size * 4 - 3
#     rows = []
#     for i in range(size):
#         left = alpha[size-1:size-i:-1]
#         right = alpha[size-i:size]
#         row = '-'.join(left + right)
#         rows.append(row.center(width, '-'))
#     print("\n".join(rows[::-1] + rows[1:]))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string
#
# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#     width = size * 4 - 3
#     rows = []
#     for i in range(size):
#         # descending from size-1 to size-i
#         left = alpha[size-1:size-i:-1]
#         # ascending from size-i to size
#         right = alpha[size-i:size]
#         row = '-'.join(left + right)
#         rows.append(row.center(width, '-'))
#     print("\n".join(rows[::-1] + rows[1:]))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

# import string
#
# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#     width = size * 4 - 3
#     rows = []
#     for i in range(size):
#         # indices descending from size-1 to size-1-i
#         desc = [alpha[j] for j in range(size - 1, size - 1 - i - 1, -1)]
#         # indices ascending from size-1-i+1 to size-1 (to avoid duplicating the center)
#         asc = [alpha[j] for j in range(size - 1 - i + 1, size)]
#         row = "-".join(desc + asc)
#
#         rows.append(row.center(width, "-"))
#
#     print("\n".join(rows[::-1] + rows[1:]))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)




# import string
# def Rangoli(size):
#     wedth=n*4-3
#     alpha=string.ascii_lowercase
#     new_list=[]
#     for i in range(n):
#         s=alpha[n-1:n-1-i:-1]+alpha[n-i-1:n]
#         row='-'.join(s)
#
#         new_list.append(row.center(wedth,'-'))
#     print("\n".join(new_list+new_list[-2::-1]))
# n=int(input())
# Rangoli(n)

# a='abcd'
# print("-".join(a))

# def result(s):
#
#     words=s.split(" ")
#     for i in words:
#         # print(i[0:1].upper()+i[1:],end=" ")
#         print(i.capitalize(),end=" ")
# s=str(input("Enter a string: "))
# result(s)
# def main(S):
#     a=''
#     for i in S:
#         a+=i
#         print(a)
#     return a
# S=(input())
# main(S)


# a=[1,2,3,2]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         # print(a[i],a[j])
#         if a[i]==a[j]:
#             print('false')
#             break
# else:
#     print('True')

# def minon_game(string):--
#     vowels='AEIOU'
#     dileep_score=0
#     sampoorna_score=0
#     n=len(string)
#     for i in range(n):
#         if string[i] in vowels:
#             dileep_score+=n-i
#         else:
#             sampoorna_score+=n-i
#     if dileep_score>sampoorna_score:
#         print("dileep",dileep_score)
#     elif sampoorna_score>dileep_score:
#         print("sampoorna",sampoorna_score)
#     else:
#         print("Draw")
# s=input()
# minon_game(s)


# s='abcdefghijklmnopqrstuvwxyz'
# width=0
# while True:
#     if len(s)>width:
#         print(s[width:width+4])
#         width+=4



# s={'A','B','C','D','E','F','G','H','I','J'}
# for i in sorted(s):
#     print(i)

# s=['ABB','BCB','DAD']
#
# result=''
# for i in sorted(s):
#     result+=''.join(dict.fromkeys(i))+ "\n"
# print(result)



# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# sum_of_arr=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(i,j)
    # sum_of_arr+=sum(i)

# print(sum_of_arr)

# print(arr[0][0])


# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # # for i in arr:
# # #     print(sum(i))
# #
# for idx,row in enumerate(arr, start=1):
#     print(f"Row {idx} sum = {sum(row)}")


# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(arr)):
#     result = 0
#     for j in range(len(arr[i])):
#         result+=arr[j][i]
#
#     print(f" Column {i+1} sum = {result} ")

# # (or)
# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for idx,col in enumerate(zip(*arr),start=1):
#     print(f" Column {idx} sum = {sum(col)}")

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i==j:
#             print(arr[i][j])

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#


# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# new_arr = []
# for i in range(len(arr)):
#     result=[]
#     for j in range(len(arr[i])):
#         result.append(arr[j][i])
#     new_arr.append(result)
# print(new_arr)

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose=list(map(list, zip(*arr)))
# print(transpose)



# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# target=int(input())
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]==target:
#             print([i],[j])
#             break


# s={'h','a','c','k','e','r','r','h'}
# print(set(enumerate(s)))




# A = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# B = [
#     [7, 8, 9],
#     [1, 2, 3]
# ]
# for i in range(len(A)):
#     result=[]
#     for j in range(len(A[0])):
#       result.append(A[i][j]+B[i][j])
#     print(result)

# C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
# print(C)




# A = [
#     [1, 2],
#     [4, 5]
# ]
#
# B = [
#     [7, 8],
#     [1, 2]
# ]
# result=[[0 for _ in range(len(B[0]))] for _ in range(len(A))]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j]+=A[i][k]*B[k][j]
# print(result)


# a=[1,2,3]
# b=[4,1,6]
# my_score=0
# score=0
# for i in range(len(a)):
#     if a[i]>b[i]:
#         my_score+=1
#     else:
#         score+=1
# print(score)
# for i in range(len(a)):
#     print(i)

# a=[1,2,3,1,4]
# b={1,2,1}
# count=0
# for i in a:
#     if i in b:
#         count+=1
# print(count)

# arr = [1, 2, 3, 4, 5]
# n=4
# for i in range(n):
#     removed=arr.pop(0)
#     arr.append(removed)
# print(arr
# )


# arr=[1,2,3,4,5]
# # target=6
# # for i in range(len(arr)):
# #     for j in range(i+1,len(arr)):
# #         if arr[i]+arr[j] == target:
# #             print(arr[i],arr[j])
# print(len(arr[0]))


# s=[1,2,3,4,5,6,7,8,9]
# left=0
# right=len(s)-1
# target=6
# while left<right:
#
#     d=s[left]+s[right]
#     if d==target:
#         print(s[left],s[right])
#         left+=1
#         right-=1
#     elif d<target:
#         left+=1
#     else:
#         right-=1


# a=[1,2,3,4,5,6]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         print(a[i],a[j])
#




# array=list(map(int,input().split()))
# target=int(input())
# for i in range(len(array)):
#
#         print(array[i],end=" ")


# word1='abcg'
# word2="ef"
# string=""
# if len(word1)<len(word2):
#     for i in range(0,len(word1)):
#         string+=word1[i]+word2[i]
#         if i==len(word1)-1:
#             string+=word2[i+1:]
# if len(word1)>len(word2):
#     for i in range(0,len(word2)):
#         string+=word1[i]+word2[i]
#         if i==len(word2)-1:
#             string+=word1[i+1:]
#
# print(string)
# for i in range(len(word2)):
#     string+=word1[i]+word2[i]
# print(string)

# s='pwwkew'
# list1=[]
# for i in range(0,len(s)):
#     for  j in range(i+1,len(s)):
#             if s[i]==s[j]:
#                 list1.append(s[i:j])
# print(list1)



# longest_string=max(list1,key=len)
# print(len(set(longest_string)))

# def main(s1,s2):
#
#     if s1.count(s2):
#         word=sorted(set(s2))
#         result="".join(word)
#         print(result)
#     else:
#         print('""')
# main("ababab","abab")

# import math
# list1=[3,3]
# min_num=min(list1)
# max_num=max(list1)
# result=math.gcd(min_num,max_num)
# print(result)

# string="dileep is a good boy"
# list1=string.split()
# word=list1[::-1]
# print(" ".join(word))


# list1=[1,12,-5,-6,50,3]
# k=4
# list=[]
# for i in range(0,len(list1)):
#     slised=list1[i:k+i]
#     if len(slised)==k:
#         list.append(sum(slised))
# print(max(list)/k)

# left=0
# right=k
# list2=[]
# while right<=len(list1):
#     sums=sum(list1[left:right])
#     list2.append(sums)
#     left+=1
#     right+=1
# print(max(list2)/k)
#
#

# s="abcaabii"
# k=3
# vowels=["a","e","i","o","u"]
# left=0
# right=k
# list1=[]
# while  right<=len(s):
#     list1.append(s[left:right])
#     left+=1
#     right+=1
# max_num=0
# for sub in list1:
#     count=sum(1 for ch in sub if ch in vowels)
#     max_num=max(max_num,count)
# print(max_num)



# s="beighj"
# k=3
# left=0
# right=k
# max_vowel=0
# while  right<=len(s):
#     sub_string=s[left:right]
#     current_sub_string=sub_string.count("a")+sub_string.count("e")+sub_string.count("i")+sub_string.count("o")+sub_string.count("u")
#     left+=1
#     right+=1
#     # if current_sub_string>max_vowel:
#     #     max_vowel=current_sub_string
#
#     max_vowel=max(max_vowel,current_sub_string)
# print(max_vowel)



# s="abciiidef"
# k=3
# vowels=set("aeiou")
# count=0
# max_count=count
# for i in range(k):
#     if s[i] in vowels:
#         count+=1
# for i in range(k,len(s)):
#     if s[i] in vowels:
#         count+=1
#     if s[i-k] in vowels:
#         count-=1
#     max_count=max(count,max_count)
# print(max_count)


# num1 = [1,3]
# num2 = [2]
# num1.extend(num2)
# sort=sorted(num1)
#
#
# if len(num1) % 2 == 0:
#     k = len(num1) // 2
#     print(sum(num1[k-1:k+1]) / 2)
# if len(num1) % 2 == 1:
#     k = len(num1) // 2
#     print(num1[k])


# num1 = [1,3]
# num2 = [2]
# num1.extend(num2)
# sort=sorted(num1)
# if len(sort) % 2 == 1:
#     k = len(sort) // 2
#     print(sort[k])


# n=-123
#
# string=str(n)
# length=len(string)
# if n>=0:
#     print(string[::-1])
# elif n<0:
#     print("-"+string[1:length][::-1])

# n="123"
# b=n[1:3][::-1]
# print(b)
# def main(x):
#     string = str(x)
#     length=len(string)
#     if x >= 0:
#         return string[::-1]
#     else:
#         return f'-{string[1:length][::-1]}'
# print(main(-123))

# import random
# n=int(input())
#
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# combined=numbers+lower_case+upper_case+special_characters
# result=random.sample(combined,n)
# result1="".join(result)
# print(result1)



# def passed_generator(n,password):
#     numbers = "0123456789"
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     special_characters = "!@#$%^&*()-+"
#     has_digit=any(ch in numbers for ch in password)
#     has_lower_case=any(ch in lower_case for ch in password)
#     has_upper_case=any(ch in upper_case for ch in password)
#     has_special_character=any(ch in special_characters for ch in password)
#     req_char=0
#     if not has_digit:
#         req_char+=1
#     if not has_lower_case:
#         req_char+=1
#     if not has_upper_case:
#         req_char+=1
#     if not has_special_character:
#         req_char+=1
#     return max(req_char,6-n)
#
# print(passed_generator(5,"abcS$"))


# def main(s):
#     start=0
#     list1=[]
#     for ch in s:
#         index=s.find(ch)
#         if ch.isupper():
#             list1.append(s[start:index])
#             start=index
#
#     return len(list1)+1
# print(main("saveChangesInTheEditor"))


# digits = [1,2,3]
# n="".join(map(str,digits))
# t=int(n)+1
# result=list(map(int,str(t)))
# print(result)
# def main(x):
#     n=str(x)
#     if int(n[::-1])==x:
#         print("YES")
#     else:
#         print("NO")
# x=int(input())
# main(x)

# n=-121
# t=str(n)
# reverse=t[::-1]
# if reverse==t:
#     print("y")
# else:
#     print("n")


# l1 = [2,4,3]
# l2 = [5,6,4]
# rev_l1="".join(map(str,l1[::-1]))
# rev_l2="".join(map(str,l2[::-1]))
# result=str(int(rev_l1)+int(rev_l2))
# two_sum=list(map(int,result[::-1]))
# print(two_sum)
# nums=[1,2,3,2,3,3]
# mp={}
# for num in nums:
#     if num in mp:
#         mp[num]+=1
#     else:
#         mp[num]=1
# print(mp)

# nums=[1,1,2,2]
# mp={}
# for x in nums:
#     mp[x]=mp.get(x,0)+1
# print(mp)
# list1=list(mp.values())
# if sorted(list1)==list(sorted(set(list1))):
#     print("true")
# else:
#     print("false")

# n=[1,2,3,1,2,3]
# from collections import defaultdict
# mp=defaultdict(int)
# for x in n:
#     mp[x]+=1
# print(mp)
# num="applel"
# from collections import defaultdict
# mp=defaultdict(int)
# for x in num:
#     mp[x]+=1
# print(mp)


# s="banana"
# mp={}
# for x in s:
#     if x in mp:
#         mp[x]+=1
#     else:
#         mp[x]=1
# print(mp)

# s="prakashpinnaya"
# mp={}
# for x in s:
#     mp[x]=mp.get(x,0)+1
# print(mp)

# s="apple"
# mp={}
# for x in s:
#     if x in mp:
#         print(True)
#     mp[x]=1

# nums1 = [1,2,3]
# nums2 = [2,4,6]
# st1=set(nums1)
# st2=set(nums2)
# print([list(st1-st2),list(st2-st1)])



# n=[0,1,0,3,4]
# for i in n:
#     if i == 0:
#         n.remove(i)
#         n.append(i)
# print(n)


# a=5
# b=4
# a,b=b,a
# print(a)
# print(b)


# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# s="apple"
# print(sorted(s))



# t ="ahbgdc"
# k=3
# left=0
# right=k
# while right<=len(t):
#     print(t[left:right])
#     right+=1
#     left+=1


# s="abcdef"
# b="cef"
# for i in range(0,len(s)+1):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])
#         if s[i:j]==b:
#             print("true")
#             break
    # else:
    #     print("false")

#
# t="bbaaaa"
# s="aaaaaa"
# s1=""
# for ch in s:
#     if ch in t:
#         s1+=ch
#         ind=t.index(ch)
#         t=t[ind+1:]
# print(s1)
# if s1==s:
#     print("true")
# else:
#     print("false")
#


# n=[1,2,2,2,23,3]
# mp={}
# for x in n:
#     mp[x]=mp.get(x,0)+1
# max_val=max(mp,key=mp.get)
# print(max_val)

# grid = [[3,2,1],
#         [2,7,6],
#         [1,7,7]]
# count=0
# for i in range(0,len(grid)):
#     for j in range(0,len(grid[i])):
#         if grid[i]==[row[j] for row in grid]:
#             count+=1
# print(count)
# from collections import Counter
# rows = Counter(tuple(row) for row in grid)
# cols=Counter(tuple(col)for col in zip(*grid))
# count=0
# for i in rows:
#     count+=rows[i]*cols.get(i,0)
# print(count)

# from collections import defaultdict
# nums=[2,1,1,2]
# target=3
# mp=defaultdict(int)
# prefix_sum=0
# count=0
# for num in nums:
#     prefix_sum+=num
#     if prefix_sum-target in mp:
#         count+=1
#     mp[prefix_sum]=mp.get(prefix_sum,0)+1
# print(count)
# print(mp)

# from collections import defaultdict
# def prefixsum(nums,k):
#     mp=defaultdict(int)
#     mp[0]=1
#     prefix_sum=0
#     count=0
#     for num in nums:
#         prefix_sum+=num
#         count+=mp[prefix_sum-k]
#         mp[prefix_sum]=mp.get(prefix_sum,0)+1
#     return count,mp
# print(prefixsum([2,2],4))



# def prefixsum(nums,k):
#     mp={0:1}
#     prefix_sum=0
#     count=0
#     for num in nums:
#         prefix_sum+=num
#         if prefix_sum-k in mp:
#             return True
#
#         mp[prefix_sum]=mp.get(prefix_sum,0)+1
# print(prefixsum([3, 1, 2, 5, 1],6))



# n=[9,2,3,45,6,7,5,7,8]
# for i ,num in enumerate(n):
#     print(i,"-->",num)
# nums=[3, 1, 2, 5, 1]
# k=6
# nums = [1, 2, 3, -2, 5]
# k = 3
# from collections import defaultdict
# mp=defaultdict(list)
# mp[0].append(-1)
# prefix_sum=0
# for i, num in enumerate(nums):
#     prefix_sum+=num
#     if prefix_sum-k in mp:
#         for start_index in mp[prefix_sum-k]:
#             print("the index from",{start_index+1},"to",{i})
#
#     mp[prefix_sum].append(i)
# print(mp)

# from collections import defaultdict
# nums = [1, 2, 3, -2, 5]
# k = 3
# mp=defaultdict(int)
# mp[0]=1
# prefix_sum=0
# count=0
# for num in nums:
#     prefix_sum+=num
#     count+=mp[prefix_sum-k]
#     mp[prefix_sum]=mp.get(prefix_sum,0)+1
# print(count)


#
#
# list1=[1,2,3,4]
# print(list1[::-1])
# list1=[1,2,3,45,67]
# emp_list=[]
# for i in list1:
#     emp_list.append(i)
# print(emp_list)

# nums=[-2,1,-3,4,-1,2,1,-5,4]
# max_sum=0
# for i in range(len(nums)):
#     for j in range(1,len(nums)):
#         curr_sum=sum(nums[i:j+1])
#         max_sum=max(curr_sum,max_sum)
#
# print(max_sum)
# def subarray(nums):
#     max_sum=0
#     for num in range(0,len(nums)):
#         left=num
#         right=num+1
#         while right<=len(nums):
#             curr_sum=sum(nums[left:right])
#             max_sum=max(curr_sum,max_sum)
#             right+=1
#     return max_sum
# nums=list(map(int,input().split()))
# print(subarray(nums))

# from collections import defaultdict
# def max_list(nums):
#     mp=defaultdict(int)
#     for num in nums:
#         mp[num]+=1
#     for i in mp:
#         if mp[i]>1:
#             print(i)
#
# nums=list(map(int,input().split()))
# max_list(nums)



# strs = ["flower","flow","flight"]
# print(set(strs))
# for str in strs:
# from collections import defaultdict
# nums = [-1,0,1,2,-1,-4]
# target=0
# mp=defaultdict(list)
# mp[0].append(-1)
# prefix_sum=0
# for i,num in enumerate(nums):
#     prefix_sum+=num
#     if prefix_sum - target in mp:
#         for start_index in mp[prefix_sum-target]:
#             print("from",start_index+1,"to",i)
#
#     mp[prefix_sum].append(i)
#
# print(mp)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# a=sorted(set(nums))
# under_score=["_"] * (len(nums)-len(a))
# a.extend(under_score)
# print("["+",".join(str(x) for x in a)+"]")


# def removeDuplicates(self, nums: List[int]) -> int:

# del_duplecates = sorted(set(nums))
# under_score = ["_"] * (len(nums) - len(del_duplecates))
# del_duplecates.extend(under_score)
# result="[" + ",".join(str(x) for x in del_duplecates) + "]"
# print(result)


# s='aabc'
# freq = [0] * 26
#
# for ch in s:
#     index = ord(ch) - ord('a')
#     freq[index] += 1
#
# print(freq)

# from collections import defaultdict
#
# s = "aAb!a"
#
# mp = defaultdict(int)
#
# for ch in s:
#     mp[ch] += 1
#
# print(mp)


# #for anagram
# s = "listen"
# t = "silent"
# if sorted(s)==sorted(t):
#     print("True")
# else:
#     print("False")
#
#
# # # first non_reperatating character:
# s = "leetcode"
# for ch in s:
#     if s.count(ch) <= 1:
#         print(ch)
#         break
#
# # check if string is palindrome or not
# s=str(input())
# reversed_string=s[::-1]
# if s==reversed_string:
#     print("string is palindrome")
#
#
# # vowels and consonents count
# s=str(input())
# vowels="aeiou"
# vowel_count=0
# consonant_count=0
# for c in s:
#     if c in vowels:
#         vowel_count+=1
#     else:
#         consonant_count+=1
# print("vowel_count:",vowel_count)
# print("consonant_count:",consonant_count)
#
# # find duplicate charecters
# from collections import defaultdict
# mp=defaultdict(list)
# s=str(input())
# for ch in s:
#     mp[ch]=mp.get(ch,0)+1
#     if mp[ch]>1:
#         print(ch)


# from collections import Counter
# s="dileep"
# t="lieepd"
# print(Counter(s)==Counter(t))


# from collections import Counter
# s="dileiepd"
# freq=Counter(s)
# for ch in s:
#     if freq[ch]==1:
#         print(ch)
#         break


# s=[0,1,2,3,3,4,2]
# s=list(filter(lambda x: x!=2,s))


# haystack = "sadpopsad"
# needle = "pop"
# # n=haystack.find(needle)
# # print(n)
# n=len(haystack)
# m=len(needle)
# for i in range(n-m+1):
#     if haystack[i:i+m]==needle:
#         print(i)
#         break
# else:
#     print("-1")


# n=[1,2,3,4,4]
# for i,num in enumerate(n):
#     print(i,num)

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# curr_sum=sum(arr[:k])
# max_sum=curr_sum
# for i in range(1,len(arr)-(k-1)):
#     curr_sum= sum(arr[i:i+k])
#     max_sum=max(max_sum,curr_sum)
# print(max_sum)



# SLIDINGS WINDOW TECHNIQUE

# arr = [2, 1, 5, 1, 3, 10]
# k = 3
# curr_sum=sum(arr[:k])
# max_sum=curr_sum
# for i in range(k,len(arr)):
#     curr_sum+=arr[i]
#     curr_sum-=arr[i-k]
#     max_sum=max(max_sum,curr_sum)
# print(max_sum)
#
#
#

# arr = [4, 1, 39, 1, 3, 10]
# k=3
# curr_sum=0
# max_sum=0
# left=0
# for right in range(0,len(arr)):
#     curr_sum+=arr[right]
#     if right-left+1==k:
#         max_sum = max(max_sum, curr_sum)
#         curr_sum-=arr[left]
#         left+=1
#
# print(max_sum)
# #
# def maxSumSubarray(arr, k):
#     window_sum = 0
#     max_sum = 0
#     left = 0

    # for right in range(len(arr)):
    #     window_sum += arr[right]
    #
    #     # window size reached
    #     if right - left + 1 == k:
    #         max_sum = max(max_sum, window_sum)
    #         window_sum -= arr[left]   # remove left element
    #         left += 1                 # slide window
    #
    # return max_sum

# print(maxSumSubarray([4, 1, 39, 1, 3, 10], 3))


# arr=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# print([[i] for i in zip(*arr)])
# transpose=
# print(transpose)
# print("     HELlo".strip())


# Longest subarray with sum ≤ K

# arr = [2, 5, 1, 7,1, 10]
# K = 14
# curr_sum=0
# max_len=0
# left=0
# for right in range(len(arr)):
#     curr_sum+=arr[right]
#     while curr_sum>K:
#         curr_sum-=arr[left]
#         left+=1
#     max_len=max(max_len,right-left+1)
# print(max_len)


# s = "abcbcbb"
# char_set=set()
# left=0
# max_len=0
# for right in range(len(s)):
#     while s[right] in char_set:
#         char_set.remove(s[right])
#         left+=1
#     char_set.add(s[right])
#     max_len=max(max_len,right-left+1)
# print(max_len)


# def sum_arr(arr,target):
#     left,right=0,len(arr)-1
#
#     result=[]
#     while left<right:
#          sum_arr=arr[left]+arr[right]
#          if sum_arr==target:
#              result.append([left,right])
#              left+=1
#              right-=1
#
#          elif sum_arr>target:
#             right-=1
#          else:
#             left+=1
#         print(result)
#
# sum_arr([1,3,5,7,8,9],10)

# s = "a"
# max_len=0
# arr=""
# for i in range(len(s)):
#     for j in range(1,len(s)+1):
#         a=s[i:j]
#         if a==a[::-1]:
#             if len(a)>max_len:
#                 max_len=len(a)
#                 arr=a
#
# print(arr)



# s=" -042"
# s=s.strip()
# st=""
# for i in range(len(s)):
#     if s[i].isdigit() or s[0]=="-" or s[0]=="+":
#         if s[i]=="0":
#             continue
#         st+=s[i]
#     else:
#         break
# if st=="":
#     st+="0"
# print(st)

# nums = [1, 1,1,2]
# k = 3
# mp={0:1}
# prefix_sum=0
# count=0
#
# for x in nums:
#     prefix_sum+=x
#     if prefix_sum-k in mp:
#         count+=mp[prefix_sum-k]
#     mp[prefix_sum]=mp.get(prefix_sum,0)+1
#
# print(mp)
# print(count)

# nums=[1,7,3,6,5,6]
# left = 0
# right = len(nums) - 1
# # print(nums[right])
# left_sum = 0
# right_sum = 0
# while left < right:
#     if left_sum <= right_sum:
#         left_sum += nums[left]
#         left += 1
#     else:
#         right_sum += nums[right]
#         right -= 1
#
#     if left_sum == right_sum:
#         print(left)
#
#
#
#   # index where sums match


# N, X = map(int,input().split())
# list1 = []
# for i in range(0, X):
#     stu_marks =list(map(float,input().split()))
#     list1.append(stu_marks)
# result=list(zip(*list1))
# for j in range(0,len(result)):
#     print(sum(result[j])/len(result[j]))

# dividend = -2147483648
# divisor = -1
# result=dividend/divisor
# print(result)

# a= "1010"
# b = "1011"
# result = int(a, 2) + int(b, 2)

# print(type(bin(result)[2:]))



# n=[1,2,3,4,5]
# n[:]=n[-3:]+n[:-3]
# print(n)



# head=Node(10)
# second=Node(20)
# third=Node(30)
#
# head.next=second
# head.next=third
#
# temp=head
#
# while temp:
#     print(head.data,end=" -> ")
#     temp=temp.next
# print("NULL")

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next= None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
#
# temp=head
#
# while temp:
#     print(temp.data,end=" -> ")
#     temp=temp.next
# print('Null')

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
#
# def insert_end(head,data):
#     new_node=Node(data)
#
#
#     if new_node is None:
#         return new_node
#
#     temp=head
#     while temp.next:
#         temp=temp.next
#     temp.next=new_node
#     return head
# head=insert_end(head,3)
# temp=head
# while temp!=None:
#     print(temp.data,end="->")
#     temp=temp.next
# print("NULL")




# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next = None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
#
# head.next=second
# second.next=third
# third.next=fourth

# def insert_end(head,data):
#     new_node = Node(data)
#
#     if new_node is None:
#         return new_node
#
#     temp=head
#
#     while temp.next!=None:
#         temp=temp.next
#     temp.next=new_node
#     return head
# head=insert_end(head,3)
#
#
#
# temp=head
# while temp!=None:
#     print(temp.data,end="->")
#     temp=temp.next
# print("NULL")



# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next = None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
#
# head.next=second
# second.next=third
# third.next=fourth
#
#
# def insert_pos(head,data,pos):
#     new_node=Node(data)
#
#     if pos==1:
#         new_node.next=head
#         return new_node
#
#     temp=head
#     count=1
#
#     while temp is not None and count<pos-1:
#         temp=temp.next
#         count+=1
#
#     if temp is None:
#         return new_node
#
#
#     new_node.next=temp.next
#     temp.next=new_node
#
#     return head
#
# head=insert_pos(head,25,4)




# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
#
#
# def delete_pos(head,pos):
#     if head is None:
#         return None
#
#     if pos==1:
#         return head.next
#
#     temp=head
#     count=1
#     while temp.next!=None and count<pos-1:
#         temp=temp.next
#         count+=1
#     temp.next=temp.next.next
#     return head
#
# head=delete_pos(head,1)
#
# temp=head
# while temp:
#     print(temp.data,end='->')
#     temp=temp.next
# print('NULL')
#
#



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
#
# def rev_linked_list(head):
#
#     prev=None
#     curr=head
#
#     while curr:
#         next_node=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next_node
#
#     return prev
# head=rev_linked_list(head)
#
# temp=head
# while temp:
#     print(temp.data,end="->")
#     temp=temp.next
# print("NULL")


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next=None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
# fifth=Node(50)
#
# head.next=second
# second.next=third
# third.next=fourth
# fourth.next=fifth
#
#
# def rev_linked_list(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None
#
#     prev=None
#     curr=head
#     while curr:
#         next_node=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next_node
#     return prev
# head=rev_linked_list(head)
#
#
#
#
# temp=head
# while temp:
#     print(temp.data,end="->")
#     temp=temp.next
# print("NULL")


import math
# nums=[1,2,3,4]
# for i in range(len(nums)):
#     num=nums[:i]+nums[i+1:]
#     print(num)


# result = []
# for num in nums:
#     list1 = nums
#     nums.remove(num)
#     print(list1)

#     product = math.prod(list1)
#     result.append(product)
#
# print(result)


# n=[1,2,3,4]
# for i in range(len(n)):
#     num=n[:i]+n[i+1:]
#     print(num)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(50)
# fourth=Node(30)
#
# head.next=second
# second.next=third
# third.next=fourth
#
#
#
# target=20
# temp=head
# position=1
# while temp:
#     if temp.data==target:
#         print(True)
#         break
#     position+=1
#     temp=temp.next
#
#
# def del_pos(head,pos):
#
#     if head is None:
#         return None
#     if pos==1:
#         return head.next
#
#     temp=head
#     count=1
#     while temp is not None and count<pos-1:
#         temp=temp.next
#         count+=1
#     temp.next=temp.next.next
#     return head
#
# head=del_pos(head,position)
#
# temp=head
# while temp:
#     print(temp.data,end="->")
#     temp=temp.next
# print("NULL")


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth










# def rev_lin(head):
#     prev = None
#     curr=head
#
#     while curr:
#         next_node=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next_node
#     if prev==




# from itertools import product

# lists = [[1,2], [3,4], [5,6]]
# for combo in product(*lists):
#     # print(combo)

# result=[]
# n=[1,2,3,4,5]
# b=[6,7,8,9,10]
# result.append(n)
# result.append(b)
# for num in product(*result):
#     print(num)

# result=[5]
# left=1
# right=1
# result=result[:left-1]+result[left-1:right][::-1]+result[right:]
# print(result)



# n=[1,2,3,4,56,7,2,3]
#
# for i in n:
#     if i==2:
#         while i<5:
#             print(i)
#             i+=1


# DOUBLY LINKED LISTS(DLL):

# Traversal of DLL


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
#
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
#
# print("NUll")



# INSERT AT THE BEGINNING:

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
#
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# def insert_beg(head,data):
#     new_node = Node(data)
#
#     head.prev=new_node
#     new_node.next=head
#
#     return new_node
#
# head=insert_beg(head,5)
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
#
# print("NUll")




# Insert at the end of DLL:
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
#
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# def insert_end(head,data):
#
#     new_node=Node(data)
#
#     if head is None:
#         return new_node
#
#     temp=head
#     while temp.next:
#         temp=temp.next
#     temp.next=new_node
#     new_node.prev=temp
#     return head
# head=insert_end(head,35)
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
#
# print("NUll")


# Insert the pos in DLL:

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
#
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# def insert_pos(head,data,pos):
#     new_node=Node(data)
#
#     if head is None:
#         return new_node
#
#     if pos<=1:
#         head.prev=new_node
#         new_node.next=head
#         return new_node
#
#     temp=head
#     count=1
#     while temp.next and count<pos-1:
#         temp=temp.next
#         count+=1
#     next_node=temp.next
#     temp.next=new_node
#     new_node.prev=temp
#     new_node.next=next_node
#
#     if next_node:
#         next_node.prev=new_node
#
#     return head
#
# head=insert_pos(head,99,3)
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
# print('Null')
#

# DELETE AT THE HEAD

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# third.next=fourth
# fourth.prev=third
#
# def del_beg(head):
#
#     if head is None:
#         return None
#
#     return head.next
#
#     if head:
#         head.prev=None
#
# head=del_beg(head)
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
# print("Null")


# DELETE AT THE END
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
# fifth=Node(50)
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# third.next=fourth
# fourth.prev=third
#
# fourth.next=fifth
# fifth.prev=fourth
#
# def del_end(head):
#
#     if head is None and head.next is None:
#         return None
#
#
#     temp=head
#     while temp.next.next:
#         temp=temp.next
#
#     temp.next=temp.next.next
#
#
#     return head
#
# head=del_end(head)
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
# print("NUll")


# DELETE AT THE POSITION
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
# fifth=Node(50)
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# third.next=fourth
# fourth.prev=third
#
# fourth.next=fifth
# fifth.prev=fourth
#
#
# def del_pos(head,pos):
#     if head is None and head.next is None:
#         return None
#
#     if pos==1:
#         return head.next
#
#     temp=head
#     count=1
#     while temp.next.next and count<pos-1:
#         temp=temp.next
#         count+=1
#     temp.next=temp.next.next
#
#     return head
#
# head=del_pos(head,2)
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
# print("NUll")


# nums = [1,1,0,1,1,1]
# count=1
# for i in range(0,len(nums)):
#     if nums[i]==nums[i+1]:
#         count+=1
#     else:
#         count=0
# print(count)


# n=[1,1]
# seen=set()
# duplicates=set()
#
# for num in n:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
#
# result=list(duplicates)
# list1=[]
# list1.extend(result)
# for num in result:
#     list1.append(num+1)
# print(list1)

# CIRCULAR LINKED LISTS AND INSERTION
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
# fourth.next=head
#
#
# def insert_beg(head,data):
#     new_node=Node(data)
#
#     if head is None:
#         new_node.next=new_node
#         return new_node
#
#     temp=head
#     while temp.next!=head:
#         temp=temp.next
#
#     temp.next=new_node
#     new_node.next=head
#
#     return new_node
# #   return head
# head=insert_beg(head,5)
#
# temp=head
# while True:
#     print(temp.data,end='->')
#     temp=temp.next
#     if temp==head:
#         break
# print('HEAD')




# CIRCULAR LINKED LISTS AND DELETION
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
# head.next=second
# second.next=third
# third.next=fourth
# fourth.next=head


# def del_beg(head):
#     if head is None or head.next is None:
#         return None
#     temp=head
#
#     while temp.next!=head:
#         temp=temp.next
#     temp.next=head.next
#
#     return head.next
# head=del_beg(head)

# def del_end(head):
#     if head is None or head.next==head:
#         return None
#
#     temp=head
#     while temp.next.next != head:
#         temp=temp.next
#     temp.next=head
#
#     return head
# head=del_end(head)
#
#
#
#
# temp=head
# while True:
#     print(temp.data,end='->')
#     temp=temp.next
#     if temp==head:
#         break
# print('HEAD')


# nums=[1,2,2,4]
# n=len(nums)
# duplicate=2
# expected=n*(n+1)//2
# actual=sum(nums)
# missing=expected-(actual-duplicate)
# print(expected,actual,missing)

# nums=[6,5,4,8]
# list1=[]
#
# left=0
# while left<len(nums):
#     count=0
#     right=left+1
#     while right<len(nums):
#         if nums[right]<nums[left]:
#             count+=1
#         right+=1
#     list1.append(count)
#     left+=1
# print(list1)
#


# s1={1,2,5}
# s2={1,2,3,4,5}
#
# s2.add(6)
# print(s2)

# print(list(s2-s1))
#
# n=[1,2,2,3,9]
# print(max(n))
# print(set(n))

# s='abcd'
# n=len(s)
# res=""
# stack=[0]*n
# pop=-1
# for i in range(n):
#     stack[i]=s[i]
#     pop=pop+1
# while pop!=-1:
#     res+=stack[pop]
#     pop=pop-1
# print(res)



# def is_balanced(s):
#     stack = []
#     pairs = {')':'(', '}':'{', ']':'['}
#
#     for ch in s:
#         if ch in '({[':
#             stack.append(ch)
#         else:
#             if not stack:
#                 return False
#             top = stack.pop()
#             if pairs[ch] != top:
#                 return False
#
#     return len(stack) == 0
#
#
#
#
#
# def balanced_par(s):
#     n=len(s)
#     stack=[0]*n
#     pairs={')':'(','}':'{',']':'['}
#     top=-1
#
#     for ch in s:
#         if ch in "([{":
#             top=top+1
#             stack[top]=ch
#
#         else:
#             if top==-1:
#                 return False
#             if pairs[ch] != stack[top]:
#                 return False
#             top=top-1
#     return top == -1
# print(balanced_par("({[]})"))
#

#
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#
# head=Node(10)
# second=Node(20)
# third=Node(30)
# fourth=Node(40)
#
#
# head.next=second
# second.prev=head
#
# second.next=third
# third.prev=second
#
# third.next=fourth
# fourth.prev=third
#
#
# def insert_pos(head,data,pos):
#     new_node = Node(data)
#
#     if head is None:
#         return new_node
#     if pos==1:
#         head.prev=new_node
#         new_node.next=head
#         return new_node
#
#     temp=head
#     count=1
#
#
#     while temp.next and count<pos-1:
#         temp=temp.next
#         count+=1
#
#     next_node=temp.next
#
#     temp.next=new_node
#     new_node.prev=temp
#
#     new_node.next=next_node
#
#     if next_node:
#         next_node.prev=new_node
#
#     return head
#
# head=insert_pos(head,6,4)
#
#
# temp=head
# while temp:
#     print(temp.data,end="<-->")
#     temp=temp.next
# print("Null")


# n=9
# for i in range(n-1, 0, -1):
#     print(i)
#

# s='qwe'
# f='nkn'
# u=sorted(s+f)
# print("".join(u))
#
# a=[1,2]
# b=[3,4]
# print(a+b)
# tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# stack=[]
# for ch in tokens:
#     if ch not in "+-*/":
#         stack.append(int(ch))
#     else:
#         a=stack.pop()
#         b=stack.pop()
#         if ch=="+":
#             stack.append(a+b)
#         elif ch=="-":
#             stack.append(b-a)
#         elif ch=="*":
#             stack.append(a*b)
#         elif ch=="/":
#             stack.append(b//a)
# print(stack)
#
# tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# stack = []
#
# for ch in tokens:
#     if ch not in "+-*/":
#         stack.append(int(ch))   # store as integers
#     else:
#         a = stack.pop()   # right operand
#         b = stack.pop()   # left operand
#
#         if ch == "/":
#             # integer division
#             answer = b // a
#             stack.append(answer)
#         elif ch == "+":
#             stack.append(b + a)
#         elif ch == "-":
#             stack.append(b - a)
#         elif ch == "*":
#             stack.append(b * a)
#
# print(stack)

# a+b*c/d
# INFIX TO POSTFIX

# def paranathesis(sign):
#
#     if sign == '+' or sign == '-':
#         return 1
#     elif sign == '*' or sign == '/':
#         return 2
#     elif sign == '^':
#         return 3
#     return 0
#
# def infix_to_postfix(s):
#     n=len(s)
#     stack=[0]*n
#     top=-1
#     output=""
#
#     for ch in s:
#         if ch.isalnum():
#             output+=ch
#
#         elif ch=='(':
#             top+=1
#             stack[top]=ch
#         elif ch==')':
#             while(top!=-1 and stack[top]!='('):
#                 output+=stack[top]
#                 top-=1
#             top-=1
#
#         else:
#             while(top!=-1 and paranathesis(stack[top])>=paranathesis(ch)):
#                 output+=stack[top]
#                 top-=1
#             top+=1
#             stack[top]=ch
#
#     while top!=-1:
#         output+=stack[top]
#         top-=1
#     return output
#
# print(infix_to_postfix('A+B*C-D'))
#

# POSTFIX_TO_PREFIX
# def postfix_to_prefix(s):
#     stack=[]
#
#     for ch in s:
#         if ch.isalnum():
#             stack.append(ch)
#         else:
#             op2=stack.pop()
#             op1=stack.pop()
#
#             stack.append(ch+op1+op2)
#     return stack[-1]
# print(postfix_to_prefix("ABC*+"))



# def paranasis(sign):
#     if sign=='+' or sign=='-':
#         return 1
#     elif sign=='*' or sign=='/':
#         return 2
#     elif sign=='^':
#         return 3
#     return 0
#
# def infix_to_prefix(s):
#     stack=[0]*len(s)
#     top=-1
#     res=""
#     for ch in s:
#         if ch.isalnum():
#             res+=ch
#
#         elif ch=="(":
#             top+=1
#             stack[top]=ch
#
#         elif ch==")":
#             while top != -1 and stack[top]!="(":
#                 res+=stack[top]
#                 top-=1
#             top-=1
#
#         else:
#             while  top != - 1 and paranasis(ch)<=paranasis(stack[top]):
#                 res+=stack[top]
#                 top-=1
#             top+=1
#             stack[top]=ch
#     while top!=-1:
#         res+=stack[top]
#         top-=1
#
#     return res
#
# print(infix_to_prefix("1*2+3*4-(7+8)"))
#



#
# s="123432"
# set_=set()
# for ch in s:
#     if ch in set_:
#         print("duplicate characters",ch)
#
#     set_.add(ch)

# s="123432"
# if len(s)==len(set(s)):
#     print("False")
# else:
#     print("True")

# s="aabbcddee"
# for i in range(0,len(s)):
#     if s.count(s[i])==1:
#         print(s[i])
#         break
# else:
#     print(f"{-1}")


# list_=[4,5,2,25]
# n=len(list_)
# stack=[]
# res=[-1]*n
#
# for i in range(n-1,-1,-1):
#     if stack and stack[-1]<=list_[i]:
#         stack.pop()
#
#     if stack:
#         res[i]=stack[-1]
#
#     stack.append(list_[i])
# print(res)


# n = int(input("enter the number: "))
# if n%2 != 0:
#     print("wired")
# elif 2<=n<=5:
#     print(" not wired")
# elif 6<=n<=20:
#     print(" wired")
# else:
#     print(" not wired")

# a="(3*4)+4-5+2*9"
# print(eval(a))


# n = "1234567"
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end="")

# sym="*"
# # print((sym*10).rjust(10))
# print((sym*2).center(3))

# #find the lenght of the list without using len() keyword
# s='radhika'
# count = 0
# for i in s:
#     count+=1
# print(count)
# # finding the number of vowels and consonents in a string
# n = "dileep"
# vow =['a','e','i','o','u']
# vowel = 0
# con =0
# for i in n:
#
#     if i in vow:
#         vowel = vowel + 1
#     else:
#         con = con + 1
# print(vowel)
# print(con)
#
# # clubing the all charecters in string
# list1=['a','b','c','d','e','f']
# new_list =""
# for i in range(0,len(list1)):
#     new_list+=list1[i]
# print(new_list)
#                     # (OR)
#
# list1=['1','2','3','4','5','6','7','8','9']
# print("".join(list1))
#
#
#
# # REMOVING PUNCTUATIONS IN A STRING
# import string
# s="hi, how are you!"
# res=""
# for ch in s:
#     if  ch not in string.punctuation:
#         res+=ch
# print(res)
#
# # FINDING THE FIRST NON REAPETED CHARACTER IN STRING
# s="gnanasree"
# res=""
# dup=""
# for ch in s:
#     if ch not in res:
#         res+=ch
#     else:
#         dup+=ch
# for i in s:
#     if i not in dup:
#         print(i)
#         break
#
#
# # count occureance of a substing
# s="dileepdileepdileepdileepdileepdileepdile"
# sub="dileep"
# print(s.count(sub))
#
#                     # (OR)
# import re
# s="dileepdileepdileepdileepdileepdileepdile"
# sub="dileep"
# result=re.findall(sub,s)
# print(len(result))
#
#

# def parameter(sign):
#     if sign=='+' or sign=='-':
#         return 1
#     elif sign=='*' or sign=='/':
#         return 2
#     elif sign=='^':
#         return 3
#     return 0
#
# def infix_to_postfix(s):
#     string=""
#     stack=[0]*len(s)
#     top=-1
#     for ch in s:
#         if ch.isalnum():
#             string+=ch
#         elif ch=='(':
#             top+=1
#             stack[top]=ch
#
#         elif ch==')':
#             while top!=-1 and stack[top]!='(':
#                 string+=stack[top]
#                 top-=1
#             top-=1
#         else:
#             while top!=-1 and parameter(stack[top])>=parameter(ch):
#                 string+=stack[top]
#                 top-=1
#             top+=1
#             stack[top]=ch
#     while top!=-1:
#         string+=stack[top]
#         top-=1
#
#
#     stack2= [0] * len(string)
#     top = -1
#     for ch in string:
#         if ch.isdigit():
#             top += 1
#             stack2[top] = int(ch)
#         else:
#             b = stack2[top]
#             top -= 1
#             a = stack2[top]
#             top -= 1
#
#             if ch == '+':
#                 result=a+b
#             elif ch == '-':
#                 result=a-b
#             elif ch == '*':
#                 result=a*b
#             elif ch == '/':
#                 result=a/b
#
#             top+=1
#             stack2[top]=result
#
#     print(stack2[0])
#
#
# res=infix_to_postfix('1+(2*3+4)*5')
#

# n=5
# queue=[0]*n
# front=-1
# rear=-1
# val=10
# for i in range(n):
#     if rear==n:
#         print("overflow")
#     else:
#         rear+=1
#         queue[rear]=val
#         val+=1
# print(queue)


# enqueue(5)
# enqueue(10)
# enqueue(15)
# dequeue()
# enqueue(20)
# enqueue(25)
# display()


# size=5
# queue=[0]*size
# front=-1
# rear=-1
# def enqueue(x):
#     global front,rear
#     if (rear+1)%size == front:
#         print("overflow")
#     elif front==-1:
#         front=0
#         rear=0
#         queue[rear]=x
#     else:
#         rear=(rear+1)%size
#         queue[rear]=x
#
#
# def dequeue():
#     global front,rear
#     if front==-1:
#         print("underflow")
#     elif front==rear:
#         print("deleted:",queue[front])
#         front=1
#         rear=1
#     else:
#         print("deleted:",queue[front])
#         front=(front+1)%size
#
#
# def display():
#     global front,rear
#     if front==-1:
#         print("underflow")
#     else:
#         i=front
#         while(i==rear):
#             print(queue[i],end="")
#             i=(i+1)%size
#         print()
#


# queue- enqueue and dequeue

size=5
queue=[None]*size
front=-1
rear=-1
#
# def enqueue(x):
#     global front,rear
#     if rear==size-1:
#         print("overflow")
#     else:
#         if front==-1:
#             front=0
#         rear+=1
#         queue[rear]=x
#
# def dequeue():
#     global front,rear
#     if front==-1:
#         print("Underflow")
#     elif front==rear:
#         front=-1
#         rear=-1
#
#     else:
#         queue[front]=0
#         front+=1
#
#
# enqueue(10)
# enqueue(20)
# enqueue(30)
# dequeue()
# print(front,rear)
#
# print(queue)

#
# # ENQUEUE,DEQUEUE USING CIRCULAR Queue
#
# size=5
# queue=[None]*size
# front=-1
# rear=-1
#
# def enqueue(x):
#     global front,rear
#     if (rear+1)%size==front:
#         print("overflow")
#
#     elif front==-1:
#         front=0
#         rear=0
#         queue[rear]=x
#
#     else:
#         rear=(rear+1)%size
#         queue[rear]=x
#
#
# def dequeue():
#     global front,rear
#     if front==-1:
#         print("underflow")
#     elif front==rear:
#         front=-1
#         rear=-1
#
#     else:
#         queue[front]=None
#         front=(front+1)%size
#
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue()
# dequeue()
# enqueue(4)
# enqueue(5)
# enqueue(6)
# dequeue()
# enqueue(7)
# print(queue)
# print(front)
# print(rear)
#
# def display():
#     global front,rear
#     if front==-1:
#         print("underflow")
#     else:
#         i=front
#         while True:
#             print(queue[i])
#             if i==rear:
#                 break
#             i=(i+1)%size
#
#
# display()
#


# queue-using two stacks

#
# stack1=[]
# stack2=[]
#
# def enqueue(x):
#     stack1.append(x)
#
# def dequeue():
#     if not stack2:
#         while stack1:
#             stack2.append(stack1.pop())
#
#     if not stack2:
#         print("stack2 empty")
#     else:
#         print("deleted:",stack2.pop())
#
#
# enqueue(1)
# enqueue(2)
# enqueue(3)
# enqueue(4)
# enqueue(5)
#
# dequeue()
# dequeue()




# improments

# class queue():
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
#
#     def enqueue(self,x):
#         self.stack1.append(x)
#
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#
#         if not self.stack2:
#             return None
#         return self.stack2.pop()
#
# q=queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
#
# print(q.dequeue())
# print(q.dequeue())
#


# a="cold"
# b="cloed"
#
# print(sorted(a)==sorted(b))

# QUEUE - Linkedlist

# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Queue():
#     def __init__(self):
#         self.rear=None
#         self.front=None
#
#     def enqueue(self,data):
#         new_node=Node(data)
#
#         if self.rear is None:
#             self.rear=self.front=new_node
#             return
#         self.rear.next=new_node
#         self.rear=new_node
#
#     def dequeue(self):
#         if self.front is None:
#             print("Queue is underflow")
#             return
#         temp=self.front
#         print("Deleted:",temp.data)
#         self.front=self.front.next
#
#         if self.front is None:
#             self.rear=None
#
#     def display(self):
#         if self.front is None:
#             print("Queue is underflow")
#             return
#
#         temp=self.front
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print(None)
#
#
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(20)
# q.enqueue(10)
# q.display()
# q.dequeue()
# q.display()
# q.dequeue()
# q.display()


# from collections import deque
#
#
# dq=deque()
#
#
# dq.append(10)
# dq.append(20)
# dq.appendleft(5)
# print(dq)
#
# dq.pop()
# dq.append(30)
# dq.popleft()
# print(dq)


# nums = [4, 2, 12, 3, 8, 7, 9]
# k = 3

# from collections import deque
#
# dq=deque()
#
# dq.append(10)
# dq.append(20)
# dq.append(30)
#
# dq.appendleft(5)
# print(dq)
#
# dq.pop()
# dq.popleft()
# print(dq)



# def bobble_sort(arr):
#
#     n=len(arr)
#
#     for i in range(n):
#
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 swapped = True
#
#         if swapped==False:
#             break
#
# arr=[5,2,1,3,4,10,9]
# bobble_sort(arr)
# print(arr)

# def selection_sort(arr):
#     n=len(arr)
#
#     for i in range(n):
#         min_index=i
#
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#
# arr=[64, 25, 12, 22, 11]
# selection_sort(arr)
# print(arr)




# TWO POINTER TECHNIEQUE

# def two_pointer(arr):
#     n=len(arr)
#     L=0
#     R=n-1
#     target=18
#     while L<R:
#         res=arr[L]+arr[R]
#         if target>res:
#             L+=1
#         elif target<res:
#             R-=1
#         elif target==res:
#             return L,R
# arr=[6,7,8,9,10]
# print(two_pointer(arr))


# def two_pointer(arr):
#     slow=0
#
#     for fast in range(1,len(arr)):
#         if arr[fast]!=arr[slow]:
#             slow+=1
#             arr[slow]=arr[fast]
#
#     return arr[:slow+1]
#
# arr=[1,1,2,2,3,3,4,5]
# print(two_pointer(arr))


# SLIDING WINDOW TECHNIQUE

# def sliding_window(arr):
#     l=0
#     sum_=0
#     max_sum=0
#     n=len(arr)
#     k=3
#     for r in range(n):
#         sum_+=arr[r]
#
#         if r-l+1==k:
#             max_sum=max(sum_,max_sum)
#
#             sum_-=arr[l]
#             l+=1
#
#     return max_sum
# arr=[2,1,5,1,3,9]
# print(sliding_window(arr))



# def sliding_window(arr):
#     l=0
#     sum_=0
#     min_len=float('inf')
#     n=len(arr)
#     target=15
#     for r in range(n):
#         sum_+=arr[r]
#
#         while target<=sum_:
#             len_=r-l+1
#             min_len=min(len_,min_len)
#
#             sum_-=arr[l]
#             l+=1
#
#     return 0 if min_len==float('inf') else min_len
#
# print(sliding_window([2,3,1,2,4,3]))


# arr=[1,2,3,4,2,1]
# freq={}
# for x in arr:
#     if x in freq:
#         freq[x]+=1
#     else:
#         freq[x]=1
#
# print(freq)






