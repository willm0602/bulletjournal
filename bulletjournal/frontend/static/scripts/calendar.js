function newCalendarItem(date)
{
    let task = window.prompt("New Calendar Item?");
    $.ajax(
        {
            url: "/api/new-calendar-item",
            method: "POST",
            body: {
                
            }
        }
    )
}