# 1. Verify
    # Could height be zero? => yes
    # What is the min number of the lines? => 2
    
# 2. Test cases
    # [0, 0] -> 0
    # [1, 0] -> 0
    # [1, 1] -> 1
    # [1, 8, 2, 7, 3] -> 14
    
# 3. Algorithm
    # two pointers: a, b at both ends
    # area = witdth * height
    # area = (b - a) * min( height a, height b )
    # compare the heights and move the smaller one inward
    # recaculate the area to see it's bigger or not

# 4. Code
class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        area = (b - a) * min(height[a], height[b])
        
        while a < b:
            if height[a] < height[b]:
                a += 1
            else: 
                b -= 1
            tempArea = (b - a) * min(height[a], height[b])
            area = max(area, tempArea)
            
        return area
    
# 5. Check typo
# 6. Run test cases
    # [0, 0]: 
        # a = 0, b = 0, area = 1 * 0 = 0 (pass)
    # [1, 0]: 
        # a = 1, b = 1, area = 1 * 0 = 0 (pass)
    # [1, 1]:
        # a = 0, b = 1, area = 1 * 1 = 1 (pass)
    # [1, 8, 2, 7, 3]:
        # a = 1, b = 1, area = 14 (pass)
        # height[a] = 8, height[b] = 8
        # tempArea = 0

# 7. Analyze complexity
    # time: O(n)
    # space: O(1)

# 8. Think improved methods