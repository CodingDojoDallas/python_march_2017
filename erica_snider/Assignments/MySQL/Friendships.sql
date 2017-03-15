SELECT users.first_name, users.last_name, friendships.users_id, friendships.friend_id, user2.first_name, user2.last_name
FROM users 
LEFT JOIN friendships 
ON friendships.users_id = users.id 
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
ORDER BY users.last_name ASC