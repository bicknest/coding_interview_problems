const makeChange = require('../solution');

test('tests that makeChange returns 1 if passed in a denomination', () => {
    expect(makeChange(25)).toEqual(1);
    expect(makeChange(10)).toEqual(1);
    expect(makeChange(5)).toEqual(1);
    expect(makeChange(1)).toEqual(1);
});

test('tests that makeChange returns 4 if passed in 4', () => {
    expect(makeChange(4)).toEqual(4);
});

test('tests that makeChange returns 3 if passed in 31', () => {
    expect(makeChange(31)).toEqual(3);
});