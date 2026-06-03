class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a res list the same size as our input num array
        res = [1] * len(nums)

        #initially set prefix = 1 since no number preceeds nums[0]
        prefix = 1

        for i in range(len(nums)):
            #prefix is always updated to reflects everything before nums[i] so we can 
            #just store the results on of multiplying in res
            res[i] = prefix
            #prefix always updates so index after nums[i] can just use
            #without multplying all over again
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            #res[i] = [ , , , ] is always multiplied  by postfix
            #from backwards, so nums[i] is always multipled by all values 
            #the input array except themselves
            res[i] = res[i] * postfix

             #postfix always updates so index after nums[i] can just use
            #without multplying all over again when coming walking through from backwards
            
            postfix = postfix * nums[i]
        return res    


        