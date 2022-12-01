/*
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome.
    - palindrome = string that is same forwards and backwards
  Do not ignore spaces, punctuation and capitalization
 */

const str1 = 'a x a';
const expected1 = true;

const str2 = 'racecar';
const expected2 = true;

const str3 = 'Dud';
const expected3 = false;

const str4 = 'oho!';
const expected4 = false;

const str5 = 'tacocat';
const expected5 = true;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */

/*
  1. Assign Variables.
      a) i, j for our pointers.
  2. Initialize a loop.
      b) loop is controlled by conditional of length / 2
  3. Compare i with j and see (if )they match if not matching return false
  4. return condition
*/

function isPalindrome(str) {
  for (let i = 0; i < str.length / 2; i++) {
    if (str[i] !== str[str.length - 1 - i]) {
      // str.length -1 - i <- this is to use same var i as end pointer
      return false;
    }
  }
  return true;
}

console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));
console.log(isPalindrome(str5));

/*****************************************************************************/
