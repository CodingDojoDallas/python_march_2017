# INSERT INTO users (id, users.first_name, users.last_name, created_at, updated_at)
# VALUES(1, 'Chris', 'Baker', NOW(), NOW());
# VALUES(2, 'Diana', 'Smith', NOW(), NOW());	# Insert users one by one
# VALUES(3, 'James', 'Johnson', NOW(), NOW());
# VALUES(4, 'Jessica', 'Davidson', NOW(), NOW());

# INSERT INTO friendships(id, user_id, friend_id, created_at, updated_at)
# VALUES(1, 1, 4, NOW(), NOW());
# VALUES(2, 1, 3, NOW(), NOW());				# Insert friendship relations one by one
# VALUES(3, 1, 2, NOW(), NOW());
# VALUES(4, 2, 1, NOW(), NOW());
# VALUES(5, 3, 1, NOW(), NOW());
# VALUES(6, 4, 1, NOW(), NOW());

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id
ORDER BY last_name ASC, friend_last_name ASC;	# Order by last name and then friend's last name