

def sortArray(nums):

        # 如果子数组有序就不继续拆分，在基本有序的数组可以使得时间复杂度比n*logn还低
        def valid(arr_list):
            flag = True
            for i in range(len(arr_list)):
                if i < len(arr_list)-1 and arr_list[i] > arr_list[i+1]:
                    flag = False

            return flag


        # 归并排序
        def merge_sort(arr_list):
            if valid(arr_list):
                print(arr_list)
                return arr_list
            
            mid = len(arr_list)//2
            left = merge_sort(arr_list[:mid])
            right = merge_sort(arr_list[mid:])
            return merge(left,right)

        def merge(left,right):
            res =[]
            while len(left)>0 and len(right)>0:
                if left[0]<=right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            
            res += left
            res += right

            return res

        return merge_sort(nums)


nums=[1,-2,3,4,5,6,13,8,-9]
print(sortArray(nums))