function validAnagram(str1, str2) {
  // add whatever parameters you deem necessary - good luck!
  //   if (str1 === str2) {
  //     return true;
  //   }

  if (str1.length !== str2.length) {
    return false;
  }

  const tempStr1 = {};
  for (let str of str1) {
    if (!tempStr1[str]) {
      tempStr1[str] = 1;
    } else {
      tempStr1[str]++;
    }
  }

  for (let str of str2) {
    if (!tempStr1[str]) {
      return false;
    } else {
      tempStr1[str] -= 1;
    }
  }

  return true;
  //   const tempStr2 = {}
  //   for (let str of str2) {
  //     if (!tempStr2[str]) {
  //       tempStr2[str] = 1;
  //     } else {
  //       tempStr2[str]++;
  //     }
  //   }
  //   //   console.log(tempStr1, tempStr2);
  //   for (let key in tempStr1) {
  //     if (tempStr1[key] == tempStr2[key]) {
  //       return true;
  //     } else return false;
  //   }
}

console.log(validAnagram("", "")); // true
console.log(validAnagram("aaz", "zza")); // false
console.log(validAnagram("anagram", "nagaram")); // true
console.log(validAnagram("rat", "car")); // false
console.log(validAnagram("awesome", "awesom")); // false
console.log(validAnagram("amanaplanacanalpanama", "acanalmanplanpamana")); // false
console.log(validAnagram("qwerty", "qeywrt")); // true
console.log(validAnagram("texttwisttime", "timetwisttext")); // true
