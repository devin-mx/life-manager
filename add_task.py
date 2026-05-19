from core.tasks import add_task
from datetime import datetime

for i in range(5):
    add_task(f"Title {i}", datetime.now())
