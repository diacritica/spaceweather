# spaceweather
Space Weather online resource web

API examples

Protonflux

http://127.0.0.1:8000/api/protonflux/?date_min=2015-12-06&date_max=2015-12-07&ptype=1&bogus=False

will yield all protonflux valid values for 2015-12-06 of energy type 1 (P>10MeV)

```
{
    "count": 251,
    "next": "http://127.0.0.1:8000/api/protonflux/?bogus=False&date_max=2015-12-07&date_min=2015-12-06&page=2&ptype=1",
    "previous": null,
    "results": [
        {
            "id": 268,
            "date": "2015-12-06T00:00:00Z",
            "ptype": 1,
            "value": 0.138,
            "units": "Protons/cm2-s-sr",
            "bogus": false,
            "links": {
                "self": "http://127.0.0.1:8000/api/protonflux/268/"
            }
        },
        {
            "id": 269,
            "date": "2015-12-06T00:05:00Z",
            "ptype": 1,
            "value": 0.109,
            "units": "Protons/cm2-s-sr",
            "bogus": false,
            "links": {
                "self": "http://127.0.0.1:8000/api/protonflux/269/"
            }
        },
        ...
]
