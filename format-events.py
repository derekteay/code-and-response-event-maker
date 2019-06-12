from airtable import Airtable

# AirTable API setup - the base and table name is correct, just add your API key
airtable = Airtable('appaS7Pu6nvkdBNiW', 'Events', api_key='your-api-key')

# Get all records
records = airtable.get_all()

# Create defaultdict structure
records_list = []

# Process each record from AirTable
for record in records:

    # For ease of code writing
    record = record['fields']

    # Get records and format appropriately
    name = record['Name'].split("-")[0].strip().replace("'", "")
    category = record['Category']
    description = record['Description'].replace("'", "")
    country = record['Country']
    start_date = record['Start Date']

    # City might not be provided, catch this error
    try:
        city = record['City']
        city_slug = city.lower().strip().replace(" ", "-")
    except KeyError:
        city = ""
        city_slug = ""

    # URL might not be provided, catch this error
    try:
        url = record['External Web Page']
    except KeyError:
        url = ""

    # End Date might not be provided, catch this error
    try:
        end_date = record['End Date']
    except KeyError:
        end_date = ""

    # Print the PHP code for this array
    print("  array (")
    print("    'title' => '" + name + "',")
    print("    'description' => '" + description + "',")
    print("    'type' => '" + category + "',")
    print("    'city' => '" + city + "',")
    print("    'city_slug' => '" + city_slug + "',")
    print("    'country' => '" + country + "',")
    print("    'start date' => '" + start_date + "',")
    print("    'end date' => '" + end_date + "',")
    print("    'url' => '" + url + "',")
    print("  ),")
    print("")
