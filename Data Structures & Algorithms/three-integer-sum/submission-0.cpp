class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int numInstances = 0;
        int sum;
        std::vector<std::vector<int>> myVector;
        std::sort(nums.begin(), nums.end());
        for(int i =0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    myVector.push_back({nums[i], nums[left], nums[right]});
                    right--;
                    left++;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                } else if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                }
            }
            
        }
        return myVector;
    }
};
