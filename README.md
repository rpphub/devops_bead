# GDE Devops Beadandó
## Futtatás
Docker composeba van téve a 2 container így 1 parancs szükséges
`
docker compose up -d
`
Parancs kiadása után elindul a 2 container,
Böngészőben a http://localhost:8080/ -on megjeleníthető a frontend.

## Projekt leíárs
2 docker container:
- 1. Egy POST kéréseket fogadó REST API ami echozza az üzeneteket.
- 2. Egy streamlit frontend amivel üzneteket küldünk és megjelenítjük a kapott echo üzeneteket.
