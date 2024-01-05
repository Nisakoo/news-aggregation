CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT, 
    source VARCHAR(128),
    post_hash VARCHAR(64) UNIQUE
);"""

INSERT_VALUES_SQL = """INSERT INTO posts(title, content, source, post_hash)
VALUES (?, ?, ?, ?);"""

IS_POSTED_SQL = """SELECT * FROM posts WHERE post_hash = ?"""