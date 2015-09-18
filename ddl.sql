CREATE TABLE alarm_severity
(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR
);
CREATE TABLE alarms
(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR,
    description VARCHAR,
    severity INT,
    date TIMESTAMP
);
ALTER TABLE alarms ADD FOREIGN KEY (severity) REFERENCES alarm_severity (id);
CREATE INDEX fki_alarms_fk1 ON alarms (severity);
