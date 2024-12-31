import requests
import json
from ClassSlot import ClassSlot

JSON_URL: str = 'https://www.fil.univ-lille.fr/~aubert/l3/agenda/2425-S6-All.json'
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
    slots: list[dict] = []
    if optionChoice not in OPTIONS:
        raise ValueError('Option not available')
    for slot in jsonResponse:
        formatted_slot = ClassSlot(slot)
        if formatted_slot.is_appropriate(courseGroups, optionChoice):
            slots.append(formatted_slot)
    return slots

def export_slots_to_ics(slots: list[ClassSlot], filename: str) -> None:
    with open(filename, 'w') as ics_file:
        ics_file.write("BEGIN:VCALENDAR\n")
        ics_file.write("VERSION:2.0\n")
        for slot in slots:
            ics_file.write("BEGIN:VEVENT\n")
            ics_file.write(f"SUMMARY:{slot.title}\n")
            if slot.allDay:
                # All-day events use date only
                ics_file.write(f"DTSTART;VALUE=DATE:{ClassSlot.format_date_ics(slot.startTime)[:8]}\n")
                if slot.endTime:
                    ics_file.write(f"DTEND;VALUE=DATE:{ClassSlot.format_date_ics(slot.endTime)[:8]}\n")
                else:
                    # If no endTime, assume same day
                    ics_file.write(f"DTEND;VALUE=DATE:{ClassSlot.format_date_ics(slot.startTime)[:8]}\n")
            else:
                ics_file.write(f"DTSTART:{ClassSlot.format_date_ics(slot.startTime)}\n")
                ics_file.write(f"DTEND:{ClassSlot.format_date_ics(slot.endTime or slot.startTime)}\n")
            ics_file.write("END:VEVENT\n")
        ics_file.write("END:VCALENDAR\n")

if __name__ == '__main__':
    jsonResponse: json = requests.get(JSON_URL).json()
    slots = extract_appropriate_slots(jsonResponse, courseGroup, optionChoice)
    export_slots_to_ics(slots, "export.ics")