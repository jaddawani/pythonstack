def biggesiza (list):
	for i in range (0,len(list),1):
		if list[i] > 0 :
			list[i]= "big"
	print(list)
	return list
biggesiza([-1,2,-2,3])



def countt (list):
    count=0
    for i in range (0,len(list),1):
        if list[i] > 0 :
            count+=1
    list[-1]= count
    print(list)
    return list
countt([-1,1,1,1])


def sum (list):
    sum=0
    for i in range (0,len(list),1):
        sum=sum+ list[i]
    print(sum)
    return sum
sum ([1,2,3,4])


def avg (list):
    sum=0
    avg=0
    for i in range (0,len(list),1):
        sum=sum+ list[i]
        avg=sum/len(list)
    print(avg)
    return avg
avg ([1,7,3,4])


def length (list):
    for i in range (0,len(list),1):
    	print (len(list))
    	return len(list)
length([1,1,1,1])


def max (list):
    max=0
    for i in range (0,len(list),1):
        if list[i]> max:
            max = list[i]
    print (max)
    return max
max ([1,2,5,8])


def min (list):
    min=0
    for i in range (0,len(list),1):
        if list[i]< min:
            min = list[i]
    print (min)
    return min
min ([1,2,5,8])



# def thisdict (list):
#     max=0
#     min=0
#     avg=0
#     sum=0
#     for i in range (0,len(list),1):
#         sum=sum+ list[i]
#         avg=sum/len(list)
#          if list[i]< min:
#             min = list[i]
#             if list[i]> max:
#             max = list[i]


# def thisdict (list):
#     for i in range (0,len(list),1):
#         print (max)
#         print (min)
#         max(list)
#     return list
# thisdict([1,2,3,4])


def thisdict (list):
    for i in range (0,len(list),1):
        maxi = max(list)
        mini = min(list)
        avg = sum(list) / len(list)
    dictionary = {'sumTotal': sum(list), 'minimum': mini, 'average': avg , 'maximum': maxi,'length': len(list) }
    print(dictionary)
    return dictionary

thisdict([1,2,3,4])











def reverse (list):
    
    print (list[::-1])
    return list
reverse ([-1,3,4,5])