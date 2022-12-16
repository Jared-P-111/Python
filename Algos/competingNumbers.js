/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

//             ⬇
//                        { }
const nums6 = [1, 4, 3, 2, 1, 1, 1, 5, 5, 5, 7, 8, 4, 8, 4, 4];
const expected6 = [1, 4];

const nums7 = [1, 2, 3, 1, 2, 3, 1, 2, 3];
const expected7 = [];

//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
  let hashMap = {};
  let highestCount = 0;
  let keyToHighest = [];

  if (nums.length < 1) {
    return nums;
  }

  for (let i = 0; i < nums.length; i++) {
    //🧈======= Counter and Assignment =========
    if (nums[i] in hashMap) {
      hashmap[nums[i]] += 1;
    } else {
      hashmap[nums[i]] = 1;
    }
  }
  for (key in hashMap) {
    //🧈======= Calculate Logic ============
    if (hashmap[nums[i]] > highestCount) {
      highestCount = hashMap[nums[i]];
      keyToHighest.push(key);
    }
  }
  return keyToHighest;
}

console.log(mode(nums1));
