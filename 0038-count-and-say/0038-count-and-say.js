/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) {
        return '1'
    }
    
    const countAndSayHelper = (val) => {
        strVal = '' + val
        let builder = ''
        let currNum = strVal[0]
        let currCount = 0
        for (let i = 0; i < strVal.length; i++) {
            if (strVal[i] === currNum) {
                currCount++
            } else {
                builder += currCount + '' + currNum
                currNum = strVal[i]
                currCount = 1
            }
        }
        builder += currCount + '' + currNum
        return builder
    }
    
    return countAndSayHelper(countAndSay(n - 1))
};