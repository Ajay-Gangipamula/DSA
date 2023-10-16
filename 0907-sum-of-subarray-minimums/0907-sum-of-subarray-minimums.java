class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        // Next smallest Element
        int NSE[] = new int[n];
        // Previous Smallest Or Equal
        int PSOE[] = new int[n];
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for (int i = 1; i < n; i++) {
            while (!stack.isEmpty() && arr[i] < arr[stack.peek()]) {
                NSE[stack.pop()] = i;
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            NSE[stack.pop()] = n;
        }
        // Now find PSOE
        stack.push(n - 1);
        for (int i = n - 2; i >= 0; i--) {
            while (!stack.isEmpty() && arr[i] <= arr[stack.peek()]) {
                PSOE[stack.pop()] = i;
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            PSOE[stack.pop()] = -1;
        }
        long sum = 0;
        int MOD = 1000000007;
        for (int i = 0; i < n; i++) {
            long a = (i - PSOE[i]);
            long b = (NSE[i] - i);
            long c = arr[i];
            long val = (a*b)%MOD;
            val = (val*c)%MOD;
            sum = (sum+val)%MOD;
        }
        return (int) sum;
    }
}
 