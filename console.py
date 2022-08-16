
import pdb 
from models.album import Album
import repositories.album_repository as album_repository

# album_repository.delete_all()

album_1 = Album("Back in Black", "Rock", "AC/DC")
album_1_with_id = album_repository.save(album_1)

print("id of album 1 ", album_1.id)


album_repository.update(album_1)

# print(task_repository.select(album_1.id).__dict__)

result = album_repository.select_all()

for album in result:
    print(album.__dict__)

result = album_repository.delete_one_album(id)

for album in result:
    print(album.__dict__)

pdb.set_trace()






