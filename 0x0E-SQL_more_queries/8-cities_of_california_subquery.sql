-- lists all the cities of California 
-- lists all the cities of California
SELECT * FROM cities, states WHERE states.name = "California" AND cities.state_id = states.id ORDER BY cities.id ASC;
