// Method 1: Heap
#include <unordered_map>
#include <queue>
#include <vector>
#include <algorithm>

class Solution
{
public:
    std::vector<int> topKFrequent(std::vector<int> &nums, int k)
    {
        std::vector<int> ret;
        std::unordered_map<int, int> map; // num -> freq
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;

        for (auto &n : nums)
        {
            map[n] += 1;
        }

        for (auto &i : map)
        {
            pq.push({i.second, i.first});
            if (pq.size() > k)
                pq.pop();
        }

        while (k--)
        {
            ret.push_back(pq.top().second);
            pq.pop();
        }

        return ret;
    }
};

// Method 2: Quick Select
#include <unordered_map>
#include <vector>

class Solution
{
public:
    void swap(int i, int j, std::vector<int> &nums)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    int partition(int l, int r, std::vector<int> &nums, std::unordered_map<int, int> &count)
    {
        int p1 = l;
        for (int p2 = l; p2 < r; p2++)
        {
            if (count[nums[p2]] >= count[nums[r]])
            {
                swap(p1, p2, nums);
                p1++;
            }
        }
        swap(p1, r, nums);
        return p1;
    }

    std::vector<int> quickSelect(int l, int r, std::vector<int> &nums, std::unordered_map<int, int> &count, int k)
    {

        std::vector<int> ret(k);
        int p = partition(l, r, nums, count);
        if (p < k - 1)
        {
            ret = quickSelect(p + 1, r, nums, count, k);
        }
        else if (p > k - 1)
        {
            ret = quickSelect(l, p - 1, nums, count, k);
        }
        else
        {
            copy(nums.begin(), nums.begin() + k, ret.begin());
        }
        return ret;
    }

    std::vector<int> topKFrequent(std::vector<int> &nums, int k)
    {
        std::unordered_map<int, int> count; // num -> freq
        for (auto &n : nums)
            count[n]++;

        std::vector<int> arr;
        for (auto i : count)
            arr.push_back(i.first);

        return quickSelect(0, arr.size() - 1, arr, count, k);
    }
};

// Method 3: Bucket Sort
#include <vector>
#include <unordered_map>

class Solution
{
public:
    std::vector<int> topKFrequent(std::vector<int> &nums, int k)
    {
        std::vector<int> ret;
        std::unordered_map<int, int> count;
        for (auto &n : nums)
        {
            count[n]++;
        }

        std::vector<std::vector<int>> freq_map(nums.size() + 1, std::vector<int>());
        for (auto i : count)
        {
            int num = i.first;
            int freq = i.second;
            freq_map[freq].push_back(num);
        }

        for (int i = freq_map.size() - 1; i > 0; i--)
        {
            for (auto num : freq_map[i])
            {
                ret.push_back(num);
                --k;
                if (k == 0)
                    goto end;
            }
        }

    end:
        return ret;
    }
};
