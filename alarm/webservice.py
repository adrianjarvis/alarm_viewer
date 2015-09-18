from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from alarm.database import DatabaseService


class WebService(object):
    def __init__(self, database_service):
        self._database_service = database_service

    def fetch_alarms(self, request):
        return alarms_to_model(self._database_service.fetch_alarms())

    def alarm_viewer(self, request):
        static_url = request.static_url('static/')
        return {'static_url': static_url}


def alarms_to_model(alarm_rows):
    return {'alarms': [
        {'name': row.name.encode('utf-8'), 'severity': row.severity.encode('utf-8'), 'description': row.description.encode('utf-8'),
         'date': row.date.strftime('%d/%m/%Y %H:%M:%S')} for row in alarm_rows]}


if __name__ == '__main__':
    dbservice = DatabaseService()
    webservice = WebService(dbservice)
    config = Configurator()
    config.add_route('alarms', '/alarms')
    config.add_route('viewer', '/')
    config.add_view(webservice.fetch_alarms, route_name='alarms', renderer='json')
    config.add_view(webservice.alarm_viewer, route_name='viewer', renderer='alarm_viewer.pt')
    config.add_static_view(name='static', path='static')
    config.include('pyramid_chameleon')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
