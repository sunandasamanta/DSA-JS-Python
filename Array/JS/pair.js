list = [1, 2, 3, 4, 5, "F"]

function pair(arr) {
    for (let i = 0; i < arr.length; i++) {
        arr.forEach(element => {
            console.log(list[i], element);
        });
    }
}

pair(list)