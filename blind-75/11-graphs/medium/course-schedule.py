class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = {i: [] for i in range(numCourses)}  
        for crs, req in prerequisites:
            reqMap[crs].append(req)
        visiting = set()
        
        def dfs(crs):
            if crs in visiting:  # cycle detected
                return False
            if reqMap[crs] == []: # this course has already been checked ok to be completed
                return True
            
            visiting.add(crs)
            for req in reqMap[crs]:
                if not dfs(req):
                    return False
            visiting.remove(crs)
            reqMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
# time: O(n + p)
# n: numCourses, p: prerequisites