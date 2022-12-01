/*
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears.


  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

const str1 = 'aaaabbcddd';
const expected1 = 'a4b2c1d3';

const str2 = '';
const expected2 = '';

const str3 = 'a';
const expected3 = 'a';

const str4 = 'bbcc';
const expected4 = 'bbcc';

const str5 = 'abcdeffffffffff';
const expected5 = 'a1b1c1d1e1f10';

const str6 = 'aaabbaaa';
const expected6 = 'a3b2a3';

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
//                     count = 4
//          tv        i
//           a       ⬇⬇
//                   aaaabbcddd

// .1) Start loop on first character of string.
//      a) Edge case check for non value.
// .2) Store temp variable at curr index
// .3) Increase count by 1
//      a)
// .4) Iterate to next char
// .5) Compare tempVar with currChar
// .6) If no match push tempVar and count to newStr
// .7) Loop to end of string.

function encodeStr(str) {
  let tempVar = '';
  let count = 0;
  let newStr = '';

  for (let i = 0; i < str.length; i++) {
    tempVar = str[i];

    if (str[i] === tempVar) {
      count += 1;
      console.log(count);
    }

    if (str[i] !== tempVar) {
      newStr += tempVar;
      newStr += count;
    }
  }
}

encodeStr(str4);
