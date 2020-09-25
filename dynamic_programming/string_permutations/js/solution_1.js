function permute(str) {
  if (str.length <= 1) {
    return new Set([str]);
  }

  const all_chars_but_last = str.slice(0, -1);
  const last_char = str[str.length - 1];
  console.log(last_char);

  const all_chars_but_last_permutations = permute(all_chars_but_last);

  const permutations = new Set();

  all_chars_but_last_permutations.forEach(permutation => {
    for (let i = 0; i < permutation.length + 1; i++) {
      const new_permutation =
        permutation.slice(0, i) + last_char + permutation.slice(i);
      permutations.add(new_permutation);
    }
  });

  return permutations;
}

module.exports = permute;
