# code-and-response-event-maker
Using the AirTable API and Python, format data from AirTable into arrays for the Code and Response site

This project uses the AirTable Python Wrapper - https://github.com/gtalarico/airtable-python-wrapper

# Usage
Add data to this AirTable - https://airtable.com/tblQehxM71jcC1HSk/viwmr7QGq39XvdLH0

Run `format-events.py`

# Sample Input

| Name | Link to DA Tool | Category | Description | City | Country | External Web Page | Start Date | End Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
IBM Developer Day @ DTEC - Dubai  UAE - 11/06/2019 - Dubai - 11/06/2019 |	https://w3.ibm.com/developer/events-dashboard/event/5c8f6c8963c61003f098f11b	| Conference	| IBM Developer Day is a Tech for Good event in Dubai  featuring over 6 sessions throughout the whole day  extensive networking sessions and a chance to pose questions to subject matter experts and technologists."	| Dubai	| United Arab Emirates | https://www.meetup.com/IBMCloud-Dubai/events/261446545/ |	2019-06-11T05:00:00.000Z	| 2019-06-11T12:00:00.000Z

# Sample Output
```
array (
    'title' => 'IBM Developer Day @ DTEC',
    'description' => 'IBM Developer Day is a Tech for Good event in Dubai featuring over 6 sessions throughout the whole day extensive networking sessions and a chance to pose questions to subject matter experts and technologists.
    'type' => 'Conference',
    'city' => 'Dubai',
    'city_slug' => 'dubai',
    'country' => 'United Arab Emirates',
    'start date' => '2019-06-11T05:00:00.000Z',
    'end date' => '2019-06-11T12:00:00.000Z',
    'url' => 'https://www.meetup.com/IBMCloud-Dubai/events/261446545/',
  ),
  ```
