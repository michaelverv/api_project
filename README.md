# API Project Michael Vervoort 1 CCS 01

## Gekozen thema
Voor het project heb ik als thema `muziek`. Mijn database bestaat uit 3 entiteiten: bands, albums en songs.
Een band kan meerdere albums hebben en een album kan meerdere songs bevatten. Een song kan ook gemaakt worden zonder een album.

## API
### Link API: https://api-project-michaelverv.cloud.okteto.net/
### Uitleg API:

## API werking met Postman
### POST /bands

Voor het aanmaken van een band en deze naar de database te sturen
![image](https://github.com/michaelverv/api_project/assets/113921262/8f89ce76-0361-48c5-bb60-d91e2c861dc4)

### GET /bands

Laat alle bands met hun albums en nummers zien
![image](https://github.com/michaelverv/api_project/assets/113921262/7e532885-9ffb-4734-9a11-8912b89a9b18)

### GET /bands/{band_id}

Laat een specifieke band zien en daarvan de albums en nummers
![image](https://github.com/michaelverv/api_project/assets/113921262/6040ee15-1545-4e04-b833-efe6d3a629f4)

### POST /bands/{band_id}/albums

Aanmaken van een album die bij een band behoort
![image](https://github.com/michaelverv/api_project/assets/113921262/16b08bff-850f-48e1-bd82-81af3f38bb28)

### GET /albums

Laat alle albums zien
![image](https://github.com/michaelverv/api_project/assets/113921262/4bfb6bc8-bd37-4e68-8431-9d9140c9c7e0)

### POST /songs

Aanmaken van een song, een album id kan gelinkt worden aan een song maar een song kan ook bestaan zonder album. Voor een POST request met een album id moet het pad: "/songs?album_id=n" zijn
![image](https://github.com/michaelverv/api_project/assets/113921262/72f7ef69-bc47-4d69-90d2-fdafb4864d85)

### GET /songs

Laat alle songs zien
![image](https://github.com/michaelverv/api_project/assets/113921262/b7dbaeb5-872e-4ae1-b01e-8dfa3647b337)

### DELETE /bands/{band_it}/delete

Het verwijderen van een specifieke band op basis van de band id

Bij een GET /bands is er te zien dat de band "Slipknot" een id van 2 heeft
![image](https://github.com/michaelverv/api_project/assets/113921262/21f930fb-68ee-4de2-90ec-6fa78e903c08)

Bij een DELETE /bands/2/delete is er een "null" te zien, dit geeft aan dat de band verwijderd is
![image](https://github.com/michaelverv/api_project/assets/113921262/a6265b46-3fd3-4558-8b51-a92a769396c7)

Als we dan opnieuw een GET /bands doen staat alleen de band met id 1 er nog
![image](https://github.com/michaelverv/api_project/assets/113921262/b4d2631b-0a0d-4c08-bbc5-150d240d8d8e)

### DELETE /delete
Verwijdert heel de database

We vertrekken weer vanuit een GET /bands. Er staat een band in met een album en een song
![image](https://github.com/michaelverv/api_project/assets/113921262/b4d2631b-0a0d-4c08-bbc5-150d240d8d8e)

Bij een DELETE /delete, geeft deze weer een "null" waarde
![image](https://github.com/michaelverv/api_project/assets/113921262/c8ff27a5-e752-4e5d-8972-8bc04f9ac077)

Bij een nieuwe GET /bands valt het op dat er niks meer in de database is opgeslagen
![image](https://github.com/michaelverv/api_project/assets/113921262/2bdff632-4f67-483e-9ad4-292f3a999926)

## OpenAPI docs
Alle endpoints van de API
![docs](https://github.com/michaelverv/api_project/assets/113921262/b2ca89c1-7d7f-48e4-a988-12f3e8a78f6d)
