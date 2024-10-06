from your_app.models import Sacrament
from datetime import datetime

# Define the target timestamp
target_date = datetime(1753, 1, 1)

# Update the records
Sacrament.objects.filter(Date_of_Communion=target_date).update(Date_of_Communion=None)
