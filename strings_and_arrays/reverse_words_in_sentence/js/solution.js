/** Reverse words in a sentence */

// Because strings are immutable in javascript
// To acheive O(1) space complexity input has to be array
function reverseInPlace(word, startIndex = 0, endIndex = word.length - 1) {
    if (word.length < 2) {
        return word;
    }
    let i, j;
    for (i = startIndex, j = endIndex; i < j; i++, j--) {
        const temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }
    return word;
}

function reverseWordsAndSentence(sentence) {
    // Reverse the whole setence first
    reverseInPlace(sentence);
    let startOfWord = 0;
    // Iterate over each of the words to reverse it back
    // to an english word
    for (let i = 0; i < sentence.length; i++) {
        if (sentence[i] === ' ') {
            reverseInPlace(sentence, startOfWord, (i - 1));
            startOfWord = i + 1;
        }
    }
   reverseInPlace(sentence, startOfWord, sentence.length - 1);
   return sentence;
}

module.exports = reverseInPlace;

module.exports = reverseWordsAndSentence;