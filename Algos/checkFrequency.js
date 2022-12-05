/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)

  1.) Create new dictionary/object.
  2.) check for < 1 if less than break from function.
  3.) Initiate loop for iteration. 
  4.) store first value and index 0 into dictionary.
  5.) Iterate over provided array/list. 
*/

const arr1 = ['a', 'a', 'a'];
const expected1 = {
  a: 3,
};
//                  i
//                  ⬇
const arr2 = ['a', 'b', 'a', 'c', 'B', 'c', 'c', 'd'];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?). On
 * - Space: O(?). On
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amount of times that item occurs.
 */
function makeFrequencyTable(arr) {
  let dictionary = {};

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] in dictionary) {
      dictionary[arr[i]] += 1;
    } else {
      dictionary[arr[i]] = 1;
    }
  }
  return dictionary;
}

console.log(makeFrequencyTable(arr1));
console.log(makeFrequencyTable(arr2));
console.log(makeFrequencyTable(arr3));
