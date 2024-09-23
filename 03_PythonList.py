#Raymond Lin
#Death Row Coders
#SoftDev
#K03-Python Review
#2024-09-17
#2 hours
def sleep_in(weekday, vacation):
  if (weekday == False or vacation == True):
    return True
  else:
    return False
def monkey_trouble(a_smile, b_smile):
  if (a_smile != b_smile):
    return False
  else:
    return True
def sum_double(a, b):
  if (a == b):
    return a * 4
  else:
    return (a + b)
def diff21(n):
  if (n > 21):
    return (n - 21) * 2
  else: 
    return 21 - n
def parrot_trouble(talking, hour):
  if (talking == True and (hour < 7 or hour > 20)):
    return True
  return False
def makes10(a, b):
  if (a == 10 or b == 10):
    return True
  if (a + b == 10):
    return True
  return False
def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)
def not_string(str):
  if str.startswith('not'):
    return str
  else: 
    return 'not ' + str
def missing_char(str, n):
  return str[:n] + str[n+1:]
def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1] + str[1:-1] + str[0]
def front3(str):
  front = str[:3]
  return front * 3
def string_times(str, n):
  result = ""
  for i in range(n):
    result = result + str
  return result
def front_times(str, n):
  front = str[:3]
  return front * n
def string_bits(str):
  return str[::2]
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return result
def last2(str):
  if len(str) < 2:
    return 0
  last = str[-2:]
  count = 0
  for i in range(len(str) - 2):
    if str[i:i+2] == last:
      count += 1
  return count
def array_count9(nums):
  return nums.count(9)
def array_front9(nums):
  return 9 in nums[:4]
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i:i+3] == [1, 2, 3]:
      return True
  return False
def string_match(a, b):
  min_length = min(len(a), len(b)) - 1
  count = 0
  for i in range(min_length):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  return False
def same_first_last(nums):
  if nums[0] == nums[len(nums)-1]:
    return True
  return False
def make_pi():
  return [3,1,4]
def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False
def sum3(nums):
  sum = 0
  for num in nums:
    sum = sum + num
  return sum
def rotate_left3(nums):
  num = []
  num.append(nums[1])
  num.append(nums[2])
  num.append(nums[0])
  return num
def reverse3(nums):
  num = []
  count = len(nums)-1
  while count >= 0:
    num.append(nums[count])
    count = count -1
  return num
def max_end3(nums):
  count = 0
  while count < len(nums):
    nums[count] = max(nums[0],nums[-1])
    count = count +1
  return nums
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]
def middle_way(a, b):
  num = []
  num.append(a[(len(a)-1)/2])
  num.append(b[(len(b)-1)/2])
  return num
def make_ends(nums):
  num = []
  num.append(nums[0])
  num.append(nums[-1])
  return num
def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False
def count_evens(nums):
  return sum(1 for num in nums if num % 2 == 0)
def big_diff(nums):
  return max(nums) - min(nums)
def centered_average(nums):
  nums_sorted = sorted(nums)
  return sum(nums_sorted[1:-1]) //(len(nums_sorted) - 2)
def sum13(nums):
  total = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else: 
      total += nums[i]
      i += 1
  return total
def sum67(nums):
  total = 0
  skip_section = False
  for num in nums:
    if num == 6:
      skip_section = True
    elif skip_section:
      if num == 7:
        skip_section = False
    else: 
      total += num
  return total
def has22(nums):
  for i in range (len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False