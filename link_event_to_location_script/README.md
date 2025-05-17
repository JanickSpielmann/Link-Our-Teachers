# How this script works

This script is designed to process event data from a PostgreSQL database,
extract location names from event descriptions, and create a new table that links events to their respective locations.
After running the script, there will be a new table with the normalized data called processed_event.

## Requirements

For this to work you need the following setup:
- table containing the relevant locations that will be needed and the events. This table just needs in Integer 'location_id' and a String 'location_name'
- table containing the events that will be linked to the locations. The table layout can be recovered from the dump file.
