# work_day =["周一","周二","周三","周四","周五",]
#
# count = 0
#
# while count <= 3:
    # day = input("今天周几：")
    # if day in work_day:
    #     print("上班吧，骚年")
    # count += 1
    #
    # if day =="周四":
    #     break#放在循环条件里面---直接退出
#1-100
# sum = 0
# count = 1
#
# while count <= 100 :
#     sum = sum + count
#     count += 1
#
# print(sum)

# zidian={
#     "mingzi":"yanyang",
#     "nixai":"kjhkj",
#     "xingbei":"nan",
#     "zhiye":"ceshi"
# }
# # print(ziadin.items())
# for key,value in zidian.items():
#     print(key,value)
# 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,j*i),end=' ')
#     print()
# 冒泡排序
k=[2,13,5,468,216,63,654,657,6,52,35,732]
n=len(k)
for i in range(n-1):
    for j in range(i+1,n):
        if k[i]>k[j]:
            k[i],k[j]=k[j],k[i]
print(k)















