# def check(arr):
#     dic = {}
#     for num in arr:
#         dic[num] = dic.get(num, 0) + 1
#     return max(dic, key=lambda x: dic[x])
#     # return max(dic, key=dic.get)
#
#
# print(check([1, 1, 1, 2, 2]))

# out = []
# def swy(seq):
#     for item in seq:
#         if isinstance(item, list):
#             swy(item)
#         else:
#             out.append(item)
#     return out
#
#
# print(swy([1, [2, 3], [[4, 5], [6]]]))

# sentence = "the cattle was rattled by the battery"
# sentence = sentence.split(" ")
# print(sentence)


# a = "abc"
# print(a[:1])

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 10
