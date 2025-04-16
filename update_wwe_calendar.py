from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Timezone de Lisboa
tz = pytz.timezone("Europe/Lisbon")

# Criar calendário
cal = Calendar()

# RAW - todas as terças às 01:00 (hora Lisboa)
start_raw = datetime(2025, 4, 22)
for i in range(52):
    event = Event()
    dt = tz.localize(start_raw + timedelta(weeks=i))
    event.name = "WWE RAW"
    event.begin = dt
    event.duration = timedelta(hours=3)
    event.description = "WWE Monday Night Raw (hora de Lisboa)"
    cal.events.add(event)

# SmackDown - todos os sábados às 01:00 (hora Lisboa)
start_smack = datetime(2025, 4, 26)
for i in range(52):
    event = Event()
    dt = tz.localize(start_smack + timedelta(weeks=i))
    event.name = "WWE SmackDown"
    event.begin = dt
    event.duration = timedelta(hours=2)
    event.description = "WWE Friday Night SmackDown (hora de Lisboa)"
    cal.events.add(event)

# PPVs confirmados (data e hora podem ser ajustados futuramente)
ppvs = [
    ("Backlash France", "2025-05-04 01:00"),
    ("King and Queen of the Ring", "2025-05-25 01:00"),
    ("Money in the Bank", "2025-07-05 01:00"),
    ("SummerSlam", "2025-08-02 01:00"),
    ("Payback", "2025-09-07 01:00"),
    ("Extreme Rules", "2025-10-06 01:00"),
    ("Crown Jewel", "2025-11-02 01:00"),
    ("Survivor Series", "2025-11-24 01:00"),
    ("TLC", "2025-12-15 01:00")
]

for name, date_str in ppvs:
    event = Event()
    dt = tz.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))
    event.name = f"WWE PPV: {name}"
    event.begin = dt
    event.duration = timedelta(hours=3)
    event.description = f"Evento especial WWE - {name}"
    cal.events.add(event)

# Guardar o calendário
with open("wwe_calendar.ics", "w") as f:
    f.writelines(cal)
