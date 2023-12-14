/**
 * @param {string} path
 * @return {string}
 */

var simplifyPath = function(path) {
    let elems = path.split('/')
    
    const LinkedListElem = class {
        constructor(data, next) {
            this.data = data
            this.next = next
        }
    }

    let head = null
    
    for (elem of elems) {
        if (elem.length === 0) {
            continue
        }
        if (elem === '.') {
            continue
        }
        if (elem === '..') {
            if (head) {
                head = head.next
            }
            continue
        }
        let newElem = new LinkedListElem(elem, head)
        head = newElem
    }

    let canonicalPath = ''

    while (head !== null) {
        canonicalPath = '/' + head.data + canonicalPath
        head = head.next
    }

    if (canonicalPath.length === 0) {
        canonicalPath = "/"
    }

    return canonicalPath
};