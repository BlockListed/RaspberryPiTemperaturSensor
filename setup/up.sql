CREATE USER IF NOT EXISTS 'raspberrytemperature'@'%';
SET PASSWORD FOR 'raspberrytemperature'@'%' = PASSWORD('raspberrytemperature');

CREATE DATABASE IF NOT EXISTS raspberrytemperature
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

GRANT ALL ON raspberrytemperature.* TO 'raspberrytemperature'@'%';