CREATE TABLE Artistas (
    artist_id SERIAL PRIMARY KEY ,
    name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE TABLE Albumes (
    album_id SERIAL PRIMARY KEY ,
    title VARCHAR(255),
    artist_id INT REFERENCES Artistas(artist_id)
);

CREATE TABLE Canciones (
    song_id SERIAL PRIMARY KEY ,
    title VARCHAR(255),
    album_id INT REFERENCES Albumes(album_id)
);

CREATE TABLE Usuarios (
    user_id SERIAL PRIMARY KEY ,
    name VARCHAR(255),
    subscription_type VARCHAR(50)
);