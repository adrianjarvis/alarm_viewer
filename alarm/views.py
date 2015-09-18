class WebService(object):
    def __init__(self, database_service):
        self._database_service = database_service

    def fetch_alarms(self, request):
        return alarms_to_model(self._database_service.fetch_alarms())

    def alarm_viewer(self, request):
        return {}


def alarms_to_model(alarm_rows):
    return {'alarms': [
        {'name': row.name.encode('utf-8'), 'severity': row.severity, 'description': row.description.encode('utf-8'),
         } for row in alarm_rows]}

