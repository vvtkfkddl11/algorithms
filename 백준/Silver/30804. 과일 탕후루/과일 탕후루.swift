import Foundation

let n = Int(readLine()!)!
let fruits = readLine()!.split(separator: " ").map { Int($0)! }

var fruit_cnt = [Int: Int]()
var left = 0
var max_len = 0

for right in 0..<n {
    fruit_cnt[fruits[right], default: 0] += 1

    while fruit_cnt.keys.count > 2 {
        fruit_cnt[fruits[left]]! -= 1
        if fruit_cnt[fruits[left]]! == 0 {
            fruit_cnt.removeValue(forKey: fruits[left])
        }
        left += 1
    }

    max_len = max(max_len, right - left + 1)
}

print(max_len)