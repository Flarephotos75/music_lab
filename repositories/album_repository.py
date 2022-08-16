
from contextlib import nullcontext
from db.run_sql import run_sql

from models.album import Album
  
def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['album_name'], row['genre'], row['artist_name'], row['id'])
        albums.append(album)
    return albums


def save(album):
    sql = "INSERT INTO albums (album_name, genre, artist_name) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.genre, album.artist_name]
    results = run_sql(sql, values)
    print(results)
    inserted_album = results[0]
    album.id = inserted_album['id']
    return album
    
def select(id):
    album = nullcontext
    sql = "SELECT * FROM albums WHERE id = (%s)"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
    album = Album(row['album_name'], row['genre'], row['artist_name'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
def update(album):
    sql = "UPDATE albums SET (album_name, genre, artist_name) = (%s, %s, %s, %s) WHERE id = %s"
    values = [album.album_name, album.genre, album.artist_name, album.id]

def delete_one_album(id):
    sql = "DELETE FROM albums WHERE id = (%s)"
    values = [id]
    results = run_sql(sql, values)





