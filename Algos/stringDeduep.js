/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str2 = 'helloo';
const expected2 = 'helo';

const str1 = 'abcABC';
const expected1 = 'abcABC';

const str3 = '';
const expected3 = '';

const str4 = 'aa';
const expected4 = 'a';

const str5 = 'abc1def1';
const expected5 = 'abc1def';

const expected5_bonus = 'abcdef1';

/**
 * De-dupes the given string.
 * - Time: O(?). 0n
 * - Space: O(?). 0n
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 *
 * .1) create variable for string ""
 * .2) create empty hash map (Object) ⬅ constant time
 * .3) initiate for loop to iterate over provided argument. ⬅ linear time
 * .4) use conditional to check if str[i] is in hash map
 *      a) if not in map put it in map
 * .5) return string
 */

function stringDedupe(str) {
  let string = '';
  let hashMap = {};

  for (let i = str.length - 1; i >= 0; i--) {
    if (!(str[i] in hashMap)) {
      string = str[i] + string;
      hashMap[str[i]] = 1;
    }
  }
  return string;
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));
/*****************************************************************************/
