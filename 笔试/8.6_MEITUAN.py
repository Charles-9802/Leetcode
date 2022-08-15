nums1 = [5, 4, 4, 5, 10, 1]
nums2 = [4, 4, 7, 5, 5, 0]
if len(nums1) % 2 == 1:
    yiban = (len(nums1) // 2) + 1
else:
    yiban = len(nums1) // 2
dic1 = {}
dic2 = {}
for ch in nums1:
    dic1[ch] = dic1.get(ch, 0) + 1
_dic1 = dict(sorted(dic1.items(), key=lambda x: x[1], reverse=True))
for i in range(len(nums2)):
    if nums2[i] == nums1[i]:
        continue
    dic2[nums2[i]] = dic2.get(nums2[i], 0) + 1
_dic2 = dict(sorted(dic2.items(), key=lambda x: x[1], reverse=True))
print(_dic1)
print(_dic2)
result = []
for key, value in _dic1.items():
    if value >= yiban:
        result.append(0)
        break
    else:
        a = dic2.get(key, 0)
        if (a + value) >= yiban:
            result.append(yiban - value)
            break
        else:
            result.append(-1)
print(result)
print(max(result))