# DonyayeSerial Scrapper
This script scraps DonyayeSerial datacenters and extracts all movies and series with all qualities. Then, saves them into a sqlite file.

To use this script, first install this packages (last one is recommended, not required)
```bash
sudo apt install python3 python3-jupyter* python3-requests python3-bs4 sqlitebrowser
```
Then get some ApiKeys from [OMDB](https://omdbapi.com/) and write them in `API_KEY` file next to `scrapping.ipynb` (each ApiKey in one line). For example:
```
kci23r22
sjjw32e
wekwix
l3i3i3
343423
...
```
> This is a random-typed text!

Now, open `scrapping.ipynb` and run all cells but the last one, now you have lots of files like this:
```
dls-movie.json
dls-series.json
dls2-movies.json
...
```
Now, run last cell to merge all of them and create `final.json`

After that, open `json-to-sqlite.ipynb` and run all cells to create a `data.db` file. It contains all of movies in a sqlite database.

You can open `data.db` by `sqlitebrowser`:
```bash
sqlitebrowser data.db
```

Enjoy!


<!-- > In this time, the repo is private. if you can see this repo and you are not me, it means that i made it public! -->
