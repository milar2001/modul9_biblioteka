# modul9_biblioteka <br/>
Abu uruchomic aplikacje nalezy pobrac repozytorium, a nastepnie otworzyc je w naszym IDE < br/>
W razie problemow wyrownac wersje bibliotek <br/>
np. "pip install Flask==2.3.1" <br/>

GET http://[hostname]/library - wyswietlanie zawartosci biblioteki <br/>
PATCH http://[hostname]/library/<int:book_id>/borrow - wypozyczenie ksiazki <br/>
PATCH http://[hostname]/library/<int:book_id>/return - oddanie ksiazki <br/>
DELETE http://[hostname]/library/<int:book_id> - usuniecie ksiazki z biblioteki <br/>
POST http://[hostname]/library - dodanie nowej ksiazki do biblioteki <br/>