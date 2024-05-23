-- lists all the cities of California 
-- lists all the cities of California
SELECT * FROM cities, states where states.name = "California" AND cities.state_id = states.id;
