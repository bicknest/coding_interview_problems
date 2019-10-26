/* Merge Two Calendars */

function mergeTwoCalendars(calendar) {
  // Sort the array by startTime

  calendar.sort((a, b) => {
    return a.startTime - b.startTime;
  });

  let updateIndex = 0;

  // Iterate over calendar and merge
  for (let i = 1; i < calendar.length; i++) {
    if (calendar[updateIndex].end >= calendar[i]) {
      calendar[updateIndex].end = Math.max(
        calendar[updateIndex].end,
        calendar[i].end
      );
      calendar[updateIndex].start = Math.min(
        calendar[updateIndex].start,
        calendar[i].start
      );
    } else {
      calendar[updateIndex] = calendar[i];
      updateIndex++;
    }
  }
  return calendar;
}
