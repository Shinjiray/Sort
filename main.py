def Bubble_sort(A):
  for i in range (len(A)):
    for j in range (len(A)-i-1):
      if A[j]>A[j+1]:
        N=A[j]
        A[j]=A[j+1]
        A[j+1]=N
  print(A)
