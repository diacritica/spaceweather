# spaceweather
Space Weather online resource web

API examples

Protonflux

http://127.0.0.1:8000/api/protonflux/?date_min=2015-12-07&date_max=2015-12-07&ptype=1&bogus=False

will yield all protonflux valid values for 2015-12-07 of energy type 1 (P>10MeV)

'''{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "date": "2015-12-07T00:00:00Z",
            "ptype": 1,
            "value": 2234234234.0,
            "units": "Protons/cm2-s-sr",
            "bogus": false,
            "links": {
                "self": "http://127.0.0.1:8000/api/protonflux/1/"
            }
        }
    ]
}
