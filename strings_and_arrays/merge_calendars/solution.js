?/* Merge Two Calendars */

function mergeTwoCalendars(calendar) {
    
    // Sort the array by startTime

    calendar.sort((a, b) => {
        return a.startTime - b.startTime;
    });

    // Initialize array that will return our merged calendar
    const mergedCalendar = [];


    // Iterate over calendar and merge
    for (let i = 0; i < calendar.length; i++) {
        if (calendar[i].endTime < calendar[i + 1].starTime) {
            mergedCalendar.push(calendar[i]);
        }
        else


    }
}