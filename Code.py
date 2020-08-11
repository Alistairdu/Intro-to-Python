def csv_sqr_csv(data):
    white = data.split()
    nums = []
    for e in white:
        nums.append(e.split(","))
    end = []
    for i in nums: 
        end.append(str(int(i) * int(i)))
    return ",".join(end)



    # new = []
    # for i in nums:
    #     new.append(int(i))
    # exp = []
    # for e in new:
    #     exp.append(e*e)
    # # return exp
    # return str(exp)[1:-1]
print(csv_sqr_csv("2,4,4,5,5"))