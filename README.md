# code-and-response-event-maker
Using the AirTable API and Python, format data from AirTable into arrays for the Code and Response site

This project uses the AirTable Python Wrapper - https://github.com/gtalarico/airtable-python-wrapper

# Usage
Add data to this AirTable - https://airtable.com/tblQehxM71jcC1HSk/viwmr7QGq39XvdLH0

# Sample Input

| Name | Link to DA Tool | Category | Description | City | Country | External Web Page | Start Date | End Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
IBM Developer Day @ DTEC - Dubai  UAE - 11/06/2019 - Dubai - 11/06/2019 |	https://w3.ibm.com/developer/events-dashboard/event/5c8f6c8963c61003f098f11b	| Conference	| IBM Developer Day is a Tech for Good event in Dubai  featuring over 6 sessions throughout the whole day  extensive networking sessions and a chance to pose questions to subject matter experts and technologists.</p><p>&nbsp;</p><p>This time  we&rsquo;re focusing on Data Science  AI and Machine Learning used to build sustainable solutions for social good with sessions for beginner  intermediate and advanced developers."	| Dubai	| United Arab Emirates | https://www.meetup.com/IBMCloud-Dubai/events/261446545/ |	2019-06-11T05:00:00.000Z	| 2019-06-11T12:00:00.000Z

# Sample Output
```
  array (
    'title' => 'Workshops and Call for Code Challenge | Lima  Peru',
    'description' => '<p>The Peruvian Red Cross  Techo Per&uacute;  UTEC Ventures and IBM del Per&uacute;  present a series of workshops meant to prepare developers willing to participate in the Call for Code 2019 and help create solutions for natural disasters. We will cover the six core technologies for the Call for Code in this workshops.&nbsp;We will present Blockchain  Data Science  Machine Learning  Internet of Things  Artificial Intelligence and Traffic and Weather by our technical experts in the Universidad de Ingenier&iacute;a y Tecnolog&iacute;a" UTEC. The developers that attend to workshop  will have the opportunity to participate in a Challenge the weekend after the workshop; they will get to know more about the Call for Code by IBM Maketing team  they will learn about Perus disasters by NGO Techo Per&uacute; and learn about how to help and be prepared in case of natural disasters by The Peruvian Red Cross; then they will explore ideas with design thinking and prototype them to be ready for the Call for Code.</p>"',
    'type' => 'Workshop',
    'city' => 'Lima',
    'city_slug' => 'lima',
    'country' => 'Peru',
    'start date' => '2019-06-11T00:00:00.000Z',
    'end date' => '2019-06-16T03:00:00.000Z',
    'url' => 'https://forms.gle/LcUZzzJsadRMKC1z9',
  ),
  ```
