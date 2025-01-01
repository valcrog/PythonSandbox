import json
import requests
from ClassSlot import ClassSlot

JSON_URL: str = 'https://www.fil.univ-lille.fr/\~aubert/l3/agenda/2425-S6-All.json'
OPTIONS: list[str] = ['all', 'none', 'BIOINFO', 'PP', 'II2D', 'META', 'MAL', 'PDM']

optionChoice: str = 'BIOINFO'
courseGroup: dict[str, int] = {'TEC': 6, 
                               'Projet': 6, 
                               'RSX2': 5, 
                               'GL': 4, 
                               'JSFS': 5, 
                               'Logique': 2, 
                               'LAAS': None, 
                               'ARCHI': 3, 
                               'PDS': None
                               }


def extract_appropriate_slots(jsonResponse: json, courseGroups: dict[str, int], optionChoice: str) -> list[dict]:
    """
    Extract all the appropriate slots based on option choice and course groups.
    Returns a list containing all the class slots matching the choices.
    """
    slots: list[dict] = []
    if optionChoice not in OPTIONS:
        raise ValueError('Option not available')
    for slot in jsonResponse:
        formatted_slot = ClassSlot(slot)
        if formatted_slot.is_appropriate(courseGroups, optionChoice):
            slots.append(formatted_slot)
    return slots

def export_slots_to_ics(slots: list[ClassSlot]) -> str:
    """
    Generates an ICS calendar string from the provided list of ClassSlot objects.
    Returns the ICS data as a string (no file operations).
    """
    ics_lines = []
    ics_lines.append("BEGIN:VCALENDAR")
    ics_lines.append("VERSION:2.0")

    for slot in slots:
        ics_lines.append("BEGIN:VEVENT")
        ics_lines.append(f"SUMMARY:{slot.title}")

        if slot.allDay:
            start_date = ClassSlot.format_date_ics(slot.startTime)[:8]
            ics_lines.append(f"DTSTART;VALUE=DATE:{start_date}")

            if slot.endTime:
                end_date = ClassSlot.format_date_ics(slot.endTime)[:8]
            else:
                end_date = start_date

            ics_lines.append(f"DTEND;VALUE=DATE:{end_date}")
        else:
            start_timestamp = ClassSlot.format_date_ics(slot.startTime)
            if slot.endTime:
                end_timestamp = ClassSlot.format_date_ics(slot.endTime)
            else:
                end_timestamp = start_timestamp

            ics_lines.append(f"DTSTART:{start_timestamp}")
            ics_lines.append(f"DTEND:{end_timestamp}")

        ics_lines.append("END:VEVENT")

    ics_lines.append("END:VCALENDAR")

    return "\n".join(ics_lines) + "\n"

def generate_ics(optionChoice, courseGroup) -> str:
    """
    Generate the ICS file corresponding to the given option and group for each course
    """
    jsonResponse = requests.get(JSON_URL).json()
    slots = extract_appropriate_slots(jsonResponse, courseGroup, optionChoice)
    return export_slots_to_ics(slots)

if __name__ == "__main__":
    ics_file = generate_ics('BIOINFO', {
                            'TEC': 6, 
                            'Projet': 6, 
                            'RSX2': 5, 
                            'GL': 4, 
                            'JSFS': 5, 
                            'Logique': 2, 
                            'LAAS': None, 
                            'ARCHI': 3, 
                            'PDS': None
                            })
    print(ics_file)