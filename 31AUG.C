class Solution {
public:
    vector<int> find3Numbers(vector<int> arr) {
        int n = arr.size();
        if (n < 3) return {}; 

        vector<int> smaller(n, -1);
        vector<int> greater(n, -1);

        int min = 0;
        for (int i = 1; i < n; ++i) {
            if (arr[i] <= arr[min]) {
                min = i;
            } else {
                smaller[i] = min;
            }
        }

        int max = n - 1;
        for (int i = n - 2; i >= 0; --i) {
            if (arr[i] >= arr[max]) {
                max = i;
            } else {
                greater[i] = max;
            }
        }

        for (int i = 0; i < n; ++i) {
            if (smaller[i] != -1 && greater[i] != -1) {
                return {arr[smaller[i]], arr[i], arr[greater[i]]};
            }
        }

        return {}; 
    }
};