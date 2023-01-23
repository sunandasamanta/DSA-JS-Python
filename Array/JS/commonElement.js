function commonElement(array1, array2) {
    for (let i = 0; i < array1.length; i++) {
        for (let j = 0; j < array2.length; j++) {
            if (array1[i] == array2[j]) {
                return true;
            }            
        }        
    }
    return false
}

list = [1, 2, 3, 4, 5]
list2 = [8, 7, 5, 6]

console.log(commonElement(list, list2));