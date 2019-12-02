function productOfThree(numbers) {
  if (numbers.length < 3) {
    return "Cant create a product of three with less than three numbers";
  }

  let max_product_three = numbers[0] * numbers[1] * numbers[2];
  let max_product_two = Math.max(
    numbers[0] * numbers[1],
    numbers[0] * numbers[2],
    numbers[1] * numbers[2]
  );
  let min_product_two = Math.min(
    numbers[0] * numbers[1],
    numbers[0] * numbers[2],
    numbers[1] * numbers[2]
  );
  let minimum = Math.min(numbers[0], numbers[1], numbers[2]);
  let maximum = Math.max(numbers[0], numbers[1], numbers[2]);

  for (let i = 3; i < numbers.length; i++) {
    max_product_three = Math.max(
      max_product_two * numbers[i],
      min_product_two * numbers[i],
      max_product_three
    );
    max_product_two = Math.max(
      max_product_two,
      minimum * numbers[i],
      maximum * numbers[i]
    );
    min_product_two = Math.min(
      min_product_two,
      minimum * numbers[i],
      maximum * numbers[i]
    );
    minimum = Math.min(numbers[i], minimum);
    maximum = Math.max(numbers[i], maximum);
  }
  return max_product_three;
}

module.exports = productOfThree;
