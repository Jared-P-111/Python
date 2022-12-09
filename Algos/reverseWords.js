/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = 'hello';
const expected1 = 'olleh';

const str2 = 'hello world';
const expected2 = 'olleh dlrow';

const str3 = 'abc def ghi';
const expected3 = 'cba fed ihg';

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 *
 * .1) push string into array
 * .2) reverse our index's
 * .3) join strings back together.
 */
function reverseWords(str) {
  let string = str.split(' ');

  for (let i = 0; i < string[i]; i++) {
    let tempStr = '';
    for (let i = 0; i < string[i].length; i++) {
      /*  */
    }
  }
  console.log(string);
}

reverseWords(str2);
reverseWords(str3);
/*****************************************************************************/
