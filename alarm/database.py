__author__ = 'Adge'

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, create_engine
from sqlalchemy.sql import select, join


class DatabaseService(object):
    def __init__(self):
        self._metadata = MetaData()
        self._severity = Table('alarm_severity', self._metadata,
                               Column('id', Integer, primary_key=True),
                               Column('name', String))

        self._alarms = Table('alarms', self._metadata,
                             Column('id', Integer, primary_key=True),
                             Column('name', String),
                             Column('description', String),
                             Column('severity', Integer, ForeignKey('alarm_severity.id')),
                             Column('date', DateTime)
                             )
        self._engine = create_engine('postgresql://alarm_viewer:test@localhost/alarmviewer')

    def fetch_alarms(self):
        select_query = select([self._alarms.c.name, self._alarms.c.description, self._alarms.c.date,
                               self._severity.c.name.label('severity')]).where(
            self._alarms.c.severity == self._severity.c.id)
        result = self._engine.execute(select_query)
        return result.fetchall()
