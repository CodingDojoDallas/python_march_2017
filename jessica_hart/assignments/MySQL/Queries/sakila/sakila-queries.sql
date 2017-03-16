USE sakila;

# What query would you run to get all the customers inside city_id = 312?
# Your query should return customer first name, last name, email, and address.
SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address FROM country
JOIN city ON country.country_id = city.country_id
JOIN address ON city.city_id = address.city_id
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;

# What query would you run to get all comedy films?
# Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM category JOIN film ON category.category_id = category.category_id
WHERE category.name = 'Comedy';

# What query would you run to get all the films joined by actor_id=5?
# Your query should return the actor id, actor name, film title, description, and release year.
SELECT film_actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) actor_name, film.film_id, film.title, film.description, film.release_year
FROM film JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film_actor.actor_id = 5;

# What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)?
# Your query should return customer first name, last name, email, and address.
SELECT customer.store_id, address.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM city JOIN address ON address.city_id = city.city_id
JOIN customer ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459);	# Must use () to group conditionals

# What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15?
# Your query should return the film title, description, release year, rating, and special feature. 
# Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT film.film_id, film.title, film.release_year, film.rating, film.special_features FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.rating = 'G' AND special_features LIKE '%Behind the Scenes%' AND film_actor.actor_id = 15;

# What query would you run to get all the actors that joined in the film_id = 369?
# Your query should return the film_id, title, actor_id, and actor_name.
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) actor_name FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

# What query would you run to get all drama films with a rental rate of 2.99?
# Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name genre, film.rental_rate 
FROM film JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id= film_category.category_id
WHERE category.name = "Drama" AND film.rental_rate='2.99';

# What query would you run to get all the action films which are joined by SANDRA KILMER?
# Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT actor.actor_id, CONCAT(actor.first_name,' ', actor.last_name) actor_name, film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id= film_category.category_id
WHERE CONCAT(actor.first_name, actor.last_name)= 'SANDRAKILMER' AND category.name = 'Action';