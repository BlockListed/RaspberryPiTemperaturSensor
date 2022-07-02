CREATE TABLE IF NOT EXISTS raspberrytemperature (
    id BIGINT NOT NULL PRIMARY KEY UNIQUE,
    pi INT NOT NULL,
    timestamp BIGINT NOT NULL,
    temp DOUBLE NOT NULL,
    humidity DOUBLE NOT NULL
);