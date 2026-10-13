import pytest


@pytest.fixture()
def my_operation_list():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture()
def filtered_executed():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]



@pytest.fixture()
def operation_list_without_executed():
    return [{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture()
def other_date_format():
    return [{"id": 41428829, "state": "EXECUTED", "date": "03.07.2019"},
            {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
            {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
            {"id": 615064591, "state": "CANCELED", "date": "14.10.2018"}]


@pytest.fixture()
def sorted_other_date_format():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T00:00:00.000000'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T00:00:00.000000'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T00:00:00.000000'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T00:00:00.000000'}]


@pytest.fixture()
def identical_date_list():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
     {"id": 939719570, "state": "EXECUTED", "date": "2018-09-12T22:14:25.241689"},
     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture()
def sorted_identical_date_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-09-12T22:14:25.241689'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]