import Foundation

func solution(_ my_string:String, _ is_suffix:String) -> Int {
    var temp = ""
    
    for i in my_string.reversed() {
        if temp == is_suffix {
            return 1
        }
        temp = String(i) + temp
    }
    if my_string == is_suffix {
        return 1
    } else {
        return 0
    }
}