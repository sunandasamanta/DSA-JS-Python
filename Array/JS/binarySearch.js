listOfNums = [1, 2, 3, 4, 54, 64, 76, 35, 25, 22, 98]
sortedList = listOfNums.sort(function(a, b){return a-b});

function binarySearch(arr, key) {
    start = 0
    end = arr.length
    while (start <= end) {
        mid = parseInt((start + end)/2)
        if (arr[mid] == key) {
            return `${key} found at index ${mid}`;            
        } else if (arr[mid]  > key) {
            end = mid-1;
        } else {
            start = mid+1;
        }
    }

    return `${key} not found`;
}

result = binarySearch(sortedList, 35);
console.log(result);