## Decode String

Given an encoded string, return its decoded string:

The encoding rule is: k[encodedstring], where the encodedstring inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume the input string is always valid; no extra white spaces, square brackets are well-formed, etc.

Furtermore you may assume that the original data does not contain any digits and that digits are only for those repeate numbers, k. For example, wont be input like 3a or 2[4].

Example:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
