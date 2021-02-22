


# def _sort_by_location(result_list):
#     new_result_list = sorted(
#         result_list,
#         key=lambda k: (
#             (k["location"][0] + k["location"][2]) // 2,
#             (k["location"][1] + k["location"][3]) // 2),
#         reverse=False)
#     return new_result_list

def _sort_by_location(result_list):
    new_result_list = sorted(
        result_list,
        key=lambda k: (
            (k["location"][1] + k["location"][3]) // 2,
            (k["location"][0] + k["location"][2]) // 2),
        reverse=False)
    return new_result_list

result_list =[{"location":[191,677,644,789],"content":"a^{3}-2018"},{"location":[191,677,644,890],"content":"又因为a≠2"},{"location":[230,950,635,1050],"content":"=-20.26"},{"location":[192,291,674,411],"content":"所以|a|=2"},{"location":[183,507,709,662],"content":"所设=a-2+2"},{"location":[152,51,829,206],"content":"∴根据题意得=y|a|-1="},{"location":[683,219,861,311],"content":"a=20"},{"location":[407,783,1192,926],"content":"(3)2018-(-2)^{3}-201"}]
aa = _sort_by_location(result_list)
print(result_list)
print(aa)


for k in aa:
    mid = (k["location"][0] + k["location"][2]) // 2, (k["location"][1] + k["location"][3]) // 2
    print(mid)