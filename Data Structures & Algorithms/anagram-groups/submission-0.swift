class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var result = [[String]]()
        var valDic = [String: [String]]()

        for i in 0..<strs.count {
            let sorted = strs[i].sorted()
            let key = String(sorted)
            
            if var val = valDic[key] {
                valDic[key] = val + [strs[i]]
            } else {
                valDic[key] = [strs[i]]
            }
            

        }
        
        for (_, val) in valDic {
            result.append(val)
        }

        return result
    }
}
