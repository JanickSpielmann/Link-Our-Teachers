import psycopg2
import re
from typing import List, Tuple

# Database connection parameters - update these with your credentials
DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def get_location_patterns(cursor) -> List[str]:
    """
    Fetch all location names from the database and create regex patterns for them.
    Handles special characters and creates case-insensitive patterns.
    """
    cursor.execute("SELECT location_name FROM public.location")
    locations = [row[0] for row in cursor.fetchall()]

    patterns = []
    for loc in locations:
        # Escape special regex characters in the location name
        escaped_loc = re.escape(loc)
        # Create a word-boundary pattern that handles special characters
        pattern = rf'\b{escaped_loc}\b'
        patterns.append(pattern)

    return patterns


def extract_locations(description: str, location_patterns: List[str]) -> Tuple[str, List[str]]:
    """
    Extract locations from description using patterns from database.
    Returns cleaned description and locations list.
    """
    found_locations = []
    cleaned_desc = description

    # Check for locations in description
    for pattern in location_patterns:
        matches = re.finditer(pattern, description, re.IGNORECASE)
        for match in matches:
            loc = match.group(0)
            # Standardize case (use the version from database if we can)
            # For now just capitalize first letter as a simple approach
            loc = loc.capitalize()
            found_locations.append(loc)
            # Remove location from description
            cleaned_desc = re.sub(pattern, '', cleaned_desc, flags=re.IGNORECASE)

    # Clean up description (remove extra spaces, commas)
    cleaned_desc = re.sub(r'\s+', ' ', cleaned_desc).strip()
    cleaned_desc = re.sub(r'(\s,|,\s)', ',', cleaned_desc)

    return cleaned_desc, found_locations


def process_events():
    """
    Main function to process event data and create location relationships.
    """
    conn = None
    try:
        # Connect to database
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()

        # First get all location patterns from the database
        location_patterns = get_location_patterns(cur)
        print(f"Loaded {len(location_patterns)} location patterns from database")

        # Create a temporary table to store processed events
        cur.execute("""
                    CREATE
                    TEMPORARY TABLE temp_processed_events (
                prosop_id text,
                typ text,
                cleaned_beschreibung text,
                location_name text,
                von text,
                bis text
            )
                    """)

        # Fetch all events from the original table
        cur.execute("SELECT \"ProsopID\", \"Typ\", \"Beschreibung\", \"Von\", \"Bis\" FROM public.event")
        events = cur.fetchall()

        for event in events:
            prosop_id, typ, beschreibung, von, bis = event

            # Handle special case where type contains 'unibe' - implies Bern
            if 'unibe' in typ.lower():
                cleaned_desc, locations = extract_locations(beschreibung, location_patterns)
                # If no locations found in description, default to Bern
                if not locations:
                    # Check if Bern exists in locations table
                    cur.execute("SELECT location_name FROM public.location WHERE location_name ILIKE 'Bern'")
                    if cur.fetchone():
                        locations = ['Bern']

                # Insert each location as separate record
                for loc in locations:
                    cur.execute("""
                                INSERT INTO temp_processed_events
                                    (prosop_id, typ, cleaned_beschreibung, location_name, von, bis)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                """, (prosop_id, typ, cleaned_desc, loc, von, bis))
            else:
                # Normal processing - extract locations from description
                cleaned_desc, locations = extract_locations(beschreibung, location_patterns)

                if not locations:
                    # If no locations found, insert as-is with NULL location
                    cur.execute("""
                                INSERT INTO temp_processed_events
                                    (prosop_id, typ, cleaned_beschreibung, location_name, von, bis)
                                VALUES (%s, %s, %s, NULL, %s, %s)
                                """, (prosop_id, typ, cleaned_desc, von, bis))
                else:
                    # Insert each location as separate record
                    for loc in locations:
                        cur.execute("""
                                    INSERT INTO temp_processed_events
                                        (prosop_id, typ, cleaned_beschreibung, location_name, von, bis)
                                    VALUES (%s, %s, %s, %s, %s, %s)
                                    """, (prosop_id, typ, cleaned_desc, loc, von, bis))

        # Create a new table for the processed events with location relationships
        # First, drop if exists (for testing)
        cur.execute("DROP TABLE IF EXISTS public.processed_event")

        # Create the new table with foreign key to locations
        cur.execute("""
                    CREATE TABLE public.processed_event
                    (
                        id           SERIAL PRIMARY KEY,
                        prosop_id    text,
                        typ          text,
                        beschreibung text,
                        von          text,
                        bis          text,
                        location_id  integer,
                        FOREIGN KEY (location_id) REFERENCES public.location (location_id)
                    )
                    """)

        # Insert processed data with location references
        cur.execute("""
                    INSERT INTO public.processed_event
                        (prosop_id, typ, beschreibung, von, bis, location_id)
                    SELECT t.prosop_id,
                           t.typ,
                           t.cleaned_beschreibung,
                           t.von,
                           t.bis,
                           l.location_id
                    FROM temp_processed_events t
                             LEFT JOIN public.location l ON t.location_name ILIKE l.location_name
                    """)

        # Commit changes
        conn.commit()
        print("Processing completed successfully.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error processing events: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    process_events()
