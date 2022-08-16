DROP table albums;

create table albums (
    id SERIAL PRIMARY KEY,
    album_name VARCHAR(255),
    genre VARCHAR(255),
    artist_name VARCHAR(255)
);

INSERT INTO albums (album_name, genre, artist_name)
    VALUES ('Night At The Opera', 'Rock', 'Queen');

INSERT INTO albums (album_name, genre, artist_name)
    VALUES ('Happy', 'Pop', 'Pharrell Williams');


