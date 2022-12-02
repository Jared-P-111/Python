/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: 'Zaphod', charm: 'high', morals: 'dicey' };

//const expected1 = { Zaphod: 'name', high: 'charm', dicey: 'morals' };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */

/*
  .1) Start loop and iterate over object
  .2) Store key in temp var
  .3) assign new name of value to key
  .4) return object
*/

function invertObj(obj) {
  let tempVar = '';
  let tempVar2 = '';

  let newObj = {};

  for (key in obj) {
    tempVar = obj[key];
    tempVar2 = key;

    newObj[key] = obj;

    // console.log(`value = ${tempVar} || key = ${tempVar2}`);
  }
}

invertObj(obj1);
