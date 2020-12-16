INSERT INTO passengers(name,flight_id) VALUES ('alice',2);
INSERT INTO passengers(name,flight_id) VALUES ('bob',2);
INSERT INTO passengers(name,flight_id) VALUES ('borkot',3);
INSERT INTO passengers(name,flight_id) VALUES ('salam',2);
INSERT INTO passengers(name,flight_id) VALUES ('rofik',1);
INSERT INTO passengers(name,flight_id) VALUES ('jobbar',3);
INSERT INTO passengers(name,flight_id) VALUES ('shohidullla',1);

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;