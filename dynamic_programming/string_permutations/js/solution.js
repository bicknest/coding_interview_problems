function getPermutations(string) {
  if (string.length < 2) {
    return new Set([string]);
  }

  // split the string into last char and all others
  const charChopped = string.slice(0, -1);
  const lastChar = string[string.length - 1];

  // make the recursive call and get the returned Set of previous perms
  const choppedPermutations = getPermutations(charChopped);

  // loop over the chopped permutations and insert missing char in all spots
  // using Set to make sure we don't add dupes
  const permutations = new Set();

  choppedPermutations.forEach(perm => {
    for (let position = 0; position < perm.length; position++) {
      const permutation =
        perm.slice(0, position) + lastChar + perm.slice(position);
      permutations.add(permutation);
      console.log(permutation);
    }
  });
  return permutations;
}

module.exports = getPermutations;
