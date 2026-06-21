class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var l = 0
        var r = l + 1
        var profit = 0
        while (r < prices.count) {
            if prices[l] < prices[r] {
                let p = prices[r] - prices[l]
                profit = max(p, profit)
                r += 1
            } else {
                l = r
                r += 1
            }

        }
        return profit
    }
}
