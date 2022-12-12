/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/
// -------- Conditions ------
// Counter never goes above six.
// If end of array and last place for 1 < 7 start loop over with new condition.
// The loops variable needs to change per conditional
//
//                                                 Counter = 2;  Index = 0;
//                                               i
//                                               ⬇
const queue1 = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {
  var count = 0;
  for (var i = 0; i < queue.length; i++) {
    if (count == 0 && queue[i] == 1) {
      count = 6;
    } else if (count > 0 && queue[i] == 1) {
      return false;
    } else if (count > 0 && queue[i] == 0) {
      count--;
    }
  }
  return true;
}

socialDistancingEnforcer(queue1);

/*****************************************************************************/
