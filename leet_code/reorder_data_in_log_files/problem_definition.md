## Reorder Data in Log Files

You have an array of `logs`. Each log is a space delimited string of words.

For each log the first word in each log is an alphanumeric identifier, Then, either:
- each wordd after the identifier will consist only of lowercase letters
- each word after the indentifier will consist only of digits

We will call these letter logs and digit logs. It is guaranteed that each log has at least one wrd after its identifier.

Reorder the logs such that all the letter logs come first and then are ordered based on lexicographic precedence. Leave the digit logs in the order they came.
The letter logs are ordered lexicographically after their identifier, digit logs are ordered as they came.
