input = [4, 6, 2, 9, 1];

function selectionSort(array) {
  for (let i = 0; i < array.length - 1; i++) {
    let temp;
    let minIdx = i;
    for (let j = 0; j < array.length - i; j++) {
      if (array[i + j] < array[minIdx]) {
        minIdx = i + j;
      }
    }
    temp = array[i];
    array[i] = array[minIdx];
    array[minIdx] = temp;
  }
  return array;
}

selectionSort(input);
console.log(input);
