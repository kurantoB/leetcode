/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) {
        return '1'
    }
    
    const countAndSayHelper = (val) => {
        const strVal = '' + val
        let builder = ''
        let currNum = strVal[0]
        let currCount = 0
        for (let i of strVal) {
            if (i === currNum) {
                currCount++
            } else {
                builder += currCount + '' + currNum
                currNum = i
                currCount = 1
            }
        }
        builder += currCount + '' + currNum
        return builder
    }
    
    return countAndSayHelper(countAndSay(n - 1))
};