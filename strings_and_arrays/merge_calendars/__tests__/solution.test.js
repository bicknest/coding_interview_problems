const mergeTwoCalendars = require("../solution");

test("merges a two meeting calendar correctly", () => {
  const calendar = [{ startTime: 1, endTime: 4 }, { startTime: 3, endTime: 7 }];
  expect(mergeTwoCalendars(calendar)).toEqual([{ startTime: 1, endTime: 7 }]);
});

test("merges a large meeting set correctly", () => {
  const calendar = [
    { startTime: 1, endTime: 6 },
    { startTime: 7, endTime: 9 },
    { startTime: 3, endTime: 4 },
    { startTime: 2, endTime: 6 }
  ];
  expect(mergeTwoCalendars(calendar)).toEqual([
    { startTime: 1, endTime: 6 },
    { startTime: 7, endTime: 9 }
  ]);
});

test("returns an empty array if passed an empty array", () => {
  const calendar = [];
  expect(mergeTwoCalendars(calendar)).toEqual([]);
});

test("returns the meeting passed if only one meeting in array", () => {
  const calendar = [{ startTime: 1, endTime: 5 }];
  expect(mergeTwoCalendars(calendar)).toEqual(calendar);
});
