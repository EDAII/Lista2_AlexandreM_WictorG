def shellSort(rand_tuples):
 size = len(rand_tuples)
 gap = int(size/2)
 while(gap >= 1):
  i = gap
  while(i < size):
   value = rand_tuples[i]
   j = i
   while(j-gap >= 0 and value < rand_tuples[j - gap]):
    rand_tuples[j] =  rand_tuples[j - gap]
    j -= gap
   rand_tuples[j] = value
   i+=1
  gap = int(gap/2)
 print("sorted sample=",rand_tuples)

sample1 = [37,22,18,50,2,3,1,29,69,5]
shellSort(sample1)
sample2 = [1,2,3,4,5,6,7,8,9]
shellSort(sample2)
sample3 = [9,8,7,6,5,4,3,2,1]
shellSort(sample3)
sample4 = [-100,-1000,200,1,500,3,-1459,-98700,3456,9]
shellSort(sample4)
