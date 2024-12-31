from datetime import datetime

class ClassSlot:
    def __init__(self, info):
        self.startTime = info['start']
        self.endTime = info.get('end', None)
        self.allDay = info.get('allDay', False)
        self.isSpecial = True
        self.title, self.slotType, self.course, self.group = self.extract_infos(info['title'])

    def extract_infos(self, title: str):
        slotType = None
        course = None
        group = None
        title = title.split("/")
        if len(title) == 2:
            infos = title[0].split()
            if infos[0] in ('TP', 'TD', 'CM'):
                self.isSpecial = False
                slotType = infos[0]
                course = infos[1]
                details = title[1].split()
                if details[-1].startswith('('):
                    group = int(details[-1][2])
            else:
                slotType = " ".join(infos)

        return "/".join(title), slotType, course, group
    
    def is_appropriate(self, courseGroup, optionChoice):
        return (((not self.group) and courseGroup.get(self.course, None)) or
                (self.course == optionChoice) or
                ((self.course in courseGroup.keys()) and self.group and (self.group == courseGroup[self.course]))
                )
    
    @staticmethod
    def format_date(dateStr: str) -> str:
        dateObj = datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
        return dateObj.strftime('%d/%m/%Y, %H:%M')
    
    @staticmethod
    def format_date_ics(dateStr: str) -> str:
        dateObj = datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
        return dateObj.strftime('%Y%m%dT%H%M%SZ')
    
    def __str__(self) -> str:
        startTimeFormatted = ClassSlot.format_date(self.startTime)
        endTimeFormatted = ClassSlot.format_date(self.endTime) if self.endTime else 'N/A'
        return f'({self.slotType}) - {self.course} [G. {self.group}] from {startTimeFormatted} to {endTimeFormatted}'
