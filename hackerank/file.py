
# def extractErrorLogs(logs):
#     # Write your code here
#     log = []
#     for l in logs:
#         if l[2] == 'ERROR' or l[2] == 'CRITICAL':
#             log.append(l)
#     logs = log    
#     for i in range(len(logs)):
#         for j in range(len(logs) - 1):
#             w1 = logs[j][0]
#             w2 = logs[j + 1][0]
#             if int(w1[6:10]) > int(w2[6:10]):
#                 switch = True
#             elif int(w1[6:10]) < int(w2[6:10]):
#                 switch = False
#             else:
#                 if int(w1[3:5]) > int(w2[3:5]):
#                     switch = True
#                 elif int(w1[3:5]) < int(w2[3:5]):
#                     switch = False
#                 else:
#                     if int(w1[0:2]) > int(w2[0:2]):
#                         switch = True
#                     elif int(w1[0:2]) < int(w2[0:2]):
#                         switch = False
#                     else:
#                         h1 = logs[j][1]
#                         h2 = logs[j + 1][1]
#                         if int(h1[0:2]) > int(h1[0:2]):
#                             print('masuk')
#                             switch = True
#                         elif int(h1[0:2]) < int(h1[0:2]):
#                             switch = False
#                         else:
#                             if int(h1[3:5]) > int(h1[3:5]):
#                                 switch = True
#                             else :
#                                 switch = False
#             if switch:
#                 logs[j], logs[j + 1] = logs[j + 1], logs[j]
#     return logs

# def custom_sort_key(log):
#     timestamp = log[0].split()[0]
#     date, time = timestamp.split('-'), log[1].split(':')
#     return (int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))

# def extractErrorLogs(logs):
#     error_logs = [log for log in logs if log[2] == 'ERROR' or log[2] == 'CRITICAL']
#     error_logs.sort(key=custom_sort_key)
#     return error_logs


# # log =  [["20-09-2000", "23:52", "ERROR", "failed"],["20-09-2000", "17:29", "CRITICAL", "failed"],["20-09-2000", "18:17", "CRITICAL", "failed"]]
# # print(extractErrorLogs(log))


# def getOneBits(n):
#     # Write your code here
#     string = ''
#     result = [0]
#     index = []
#     i_invers = 0
#     while n > 0:
#         if n%2:
#             result[0] += 1
#             index.append(i_invers)
#         string = str(n % 2) + string
#         n = n//2
#         i_invers += 1
#     for i in index[::-1]:
#         result.append(len(string)-i)
#     return result


# def kSub(k, nums):
#     # Write your code here
#     count = 0   
#     for start in range(len(nums)):
#         for end in range(start + 1, len(nums) + 1):
#             subarray = []
#             for i in range(start, end):
#                 subarray.append(nums[i])
#             if sum(subarray) % k == 0:
#                 count += 1
#     return count

# def kSub(k, nums):
#     # Write your code here
#     dividible_nums = 0
#     non_dividible_nums = []
#     for num in nums:
#         if num%2==0:
#             dividible_nums += 1
#         else:
#             non_dividible_nums.append(num)
#     count1 = 2**dividible_nums   
#     count2 = 0
#     for start in range(len(non_dividible_nums)):
#         for end in range(start + 1, len(non_dividible_nums) + 1):
#             subarray = []
#             for i in range(start, end):
#                 subarray.append(non_dividible_nums[i])
#             if sum(subarray) % k == 0:
#                 count2 += 1            
#     return count1-1 + count2 + count1*count2

# # data = [1, 2, 3, 4]

# # print(kSub(2, data))


# def minMoves(h,w,h1,w1):
#     hh = ww = hw = wh = 0
#     loop = True
#     while loop :
#         loop = False
#         if h > h1:
#             hh +=1
#             loop = True
#         if w > w1:
#             ww +=1
#             loop = True
#         if h > w1:
#             hw +=1
#             loop = True
#         if h > h1:
#             wh +=1
#             loop = True
#         h /= 2
#         w /= 2
#     if hh+ww < hw+wh:
#         return hh+ww
#     else: 
#         return hw+wh
        

# a = minMoves(4,3,10,2)
# print(a)



def kSub(k, nums):
    mods = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        modulus = current_sum % k
        if modulus < 0:
            modulus += k
        if modulus in mods:
            count += mods[modulus]
        if modulus in mods:
            mods[modulus] += 1
        else:
            mods[modulus] = 1

    return count

# def kSub(k, nums):
#     mods = {0: 1}
#     current_sum = 0
#     count = 0
#     for num in nums:
#         current_sum += num
#         modulus = current_sum % k  
#         if modulus in mods:
#             count += mods[modulus]
#             mods[modulus] += 1
#         else:
#             mods[modulus] = 1
#     return count

data = [1, 1, 1, 4]

print(kSub(3, data))

# def rearrange(arr):
#     # Write your code here
#     arr.sort()
#     arr.reverse()
#     first = [arr[0]]
#     arr = arr[1:]
#     half = len(arr) - (len(arr)//2)
#     insert =  arr[half:]
#     arr = arr[:half]
#     i = 1
#     for data in insert:
#         arr.insert(i, data)
#         i += 2
#     return first + arr

# print(rearrange([21,34,5,7,9]))

