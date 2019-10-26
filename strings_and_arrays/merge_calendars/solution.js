/* Merge Two Calendars */

function mergeTwoCalendars(calendar) {
  //Deals with case of empty or one event calendar
  if (calendar.length < 2) {
    return calendar;
  }

  // Sorts the array by start times ascending (O(nlgn))
  calendar.sort((a, b) => {
    return a.startTime - b.startTime;
  });

  let updateIndex = 0;

  // Traverse the array and merge calendar events in place (O(n) time)
  for (let i = 1; i < calendar.length; i++) {
    if (calendar[updateIndex].endTime >= calendar[i].startTime) {
      calendar[updateIndex].endTime = Math.max(
        calendar[updateIndex].endTime,
        calendar[i].endTime
      );
      calendar[updateIndex].startTime = Math.min(
        calendar[updateIndex].startTime,
        calendar[i].startTime
      );
    } else {
      calendar[updateIndex + 1] = calendar[i];
      updateIndex++;
    }
  }
  // pop off the rest of the array we don't need (O(n) worst case time)
  const lengthDiff = calendar.length - updateIndex;
  for (let i = 1; i < lengthDiff; i++) {
    calendar.pop();
  }
  return calendar;
}

module.exports = mergeTwoCalendars;
