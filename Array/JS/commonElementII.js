function commonElementII(array,array2) {
    //create an obj with first array
    obj = {}
    for (let i = 0; i < array.length; i++) {
        if (!obj[array[i]]) {
            obj[array[i]] = true
        }        
    }
    // console.log(obj);
    //check whether array2 elements exists in the obj properties    
    for (let j = 0; j < array2.length; j++) {
        if (obj[array2[j]]) {
            return true;
        }        
    }
    return false;
}
list = [1, 2, 3, 4, 5]
list2 = [8, 7, 5, 6]
console.log(commonElementII(list, list2));