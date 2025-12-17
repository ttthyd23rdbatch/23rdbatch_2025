<<<<<<< HEAD
CREATE DATABASE INSTAGRAM_DB;

CREATE TABLE USERS (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INT,
    caption TEXT,
    hashtags TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE likes (
    like_id SERIAL PRIMARY KEY,
    post_id INT,
    user_id INT,
    liked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--INSERTING DATA INTO TABLES

INSERT INTO users (username, email, bio) VALUES
('srividya', 'sri@gmail.com', 'Python Developer'),
('kiran', 'kiran@gmail.com', 'Traveller'),
('arun', 'arun@gmail.com', 'Food lover');

INSERT INTO posts (user_id, caption, hashtags) VALUES
(1, 'Learning PostgreSQL', ARRAY['#sql', '#postgres']),
(2, 'Vacation time', ARRAY['#travel', '#fun']),
(1, 'Indexing explained', ARRAY['#database', '#index']);

INSERT INTO likes (post_id, user_id) VALUES
(1, 2),
(1, 3),
(2, 1);


SELECT * FROM USERS;
SELECT * FROM POSTS;
SELECT * FROM LIKES;


--1.B-TREE INDEX

CREATE INDEX IDX_USERS_USERNAME
ON USERS(USERNAME);

--QUERYING B-TREE
SELECT * FROM USERS WHERE USERNAME = 'srividya';


-- 2. hash index

CREATE INDEX IDX_LIKES_POSTS_HASH
ON LIKES USING HASH(POST_ID);

--QUERYING HASH INDEX

SELECT * FROM LIKES WHERE POST_ID = 1;


--QUERYING THE BITMAP INDEX
EXPLAIN ANALYZE
SELECT * 
FROM POSTS
WHERE USER_ID = 1
AND CREATED_AT >= CURRENT_DATE - INTERVAL '7 DAYS';

CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_created_at ON posts(created_at);


SET enable_seqscan = OFF;

SET enable_indexscan = OFF;
SET enable_seqscan = OFF;


--UNIQUE INDEX

CREATE UNIQUE INDEX IDX_UNIQUE_USERNAME
ON USERS(USERNAME);

--COMPOSITE UNIQUE INDEX

CREATE UNIQUE INDEX IDX_UNIQUE_LIKE
ON LIKES(POST_ID, USER_ID);

--UNIQUE INDES DOES NOT ALLOW DUPLICATE ROWS
INSERT INTO USERS (username,email)values
('srividya','sri@gmail.com');


--- GIN INDEX

CREATE INDEX IDX_POSTS_HASHTAGS
ON POSTS USING GIN(HASHTAGS);

--QUERYING THE GIN INDEX

SELECT * FROM POSTS
WHERE HASHTAGS @> ARRAY['#sql'];

SELECT * FROM POSTS
WHERE HASHTAGS && ARRAY['#travel'];

SELECT * FROM POSTS
WHERE TO_TSVECTOR('english',CAPTION) @@ TO_TSQUERY('indexing');


---composite index
CREATE INDEX IDX_LIKES_POSTS_USER
ON LIKES(POST_ID,USER_ID);

--QUERYING THE COMPOSITE INDEX
SELECT * FROM LIKES
WHERE POST_ID = 1 AND USER_ID = 2;

SELECT * FROM LIKES
WHERE POST_ID = 1;

--PARTIAL INDEX

ALTER TABLE USERS ADD COLUMN IS_ACTIVE BOOLEAN;
UPDATE USERS

SET IS_ACTIVE = CREATED_AT >= CURRENT_DATE - INTERVAL '30 DAYS';

CREATE INDEX idx_active_users
ON users(created_at)
WHERE is_active = true;

SELECT indexname, indexdef
from pg_indexes
where tablename = 'users';

SELECT COUNT(*) 
FROM users
WHERE is_active = true;

SELECT COUNT(*) FROM users;


EXPLAIN ANALYZE
SELECT *
FROM users
WHERE is_active = true
AND created_at >= DATE '2025-01-01';


=======
-- PL/SQL practice for 14-12-2025
>>>>>>> 2c8f74ff4a28405b418a89748e0928791107a2b0
