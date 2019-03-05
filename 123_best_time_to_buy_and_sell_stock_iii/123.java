/*
	Author: Zac Cui
	Created Date: 2019-03-05 23:24:56
*/
	
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        int buy1 = prices[0], buy2 = prices[0];
        int sell1 = 0, sell2 = 0;
        for (int i = 1; i < prices.length; ++i) {
            buy1 = Math.min(buy1, prices[i]);
            sell1 = Math.max(sell1, prices[i] - buy1);
            buy2 = Math.min(buy2, prices[i] - sell1);
            sell2 = Math.max(sell2, prices[i] - buy2);
        }
        return sell2;
    }
}