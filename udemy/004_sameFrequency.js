function sameFrequency(num1, num2) {
  const str_num1 = num1.toString();
  const str_num2 = num2.toString();
  if (str_num1.length !== str_num2.length) return false;
  let tempObj = {};
  for (let str of str_num1) {
    tempObj[str] = (tempObj[str] || 0) + 1;
  }
  for (let str of str_num2) {
    if (!tempObj[str]) return false;
    else tempObj[str] -= 1;
  }
  return true;
}

console.log(sameFrequency(182, 281)); // true
console.log(sameFrequency(34, 14)); // false
console.log(sameFrequency(3589578, 5879385)); // true
console.log(sameFrequency(22, 222)); // false
