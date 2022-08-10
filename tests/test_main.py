from fastapi.testclient import TestClient
from api.main import tips
import pytest
from unittest import mock
from api.db_utils import get_random_test_data
import pandas as pd

client = TestClient(tips)

def test_main_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message':"hello world tips"}


@mock.patch('api.main.get_random_test_data')
def test_main_get_random_test_data_mock(random_test_data_mock, dummy_df, dummy_dict_list):
    
    random_test_data_mock.return_value = dummy_df
    actual = client.get('/get_random_test_data')
    expected = dummy_dict_list
    
    assert actual.status_code == 200
    assert actual.json() == expected


@mock.patch('api.main.get_db_data')
def test_main_test_data_mock(test_data_mock, dummy_df, dummy_dict_list):
    
    test_data_mock.return_value = dummy_df
    actual = client.get('/test_data')
    expected = dummy_dict_list
    
    assert actual.status_code == 200
    assert actual.json() == expected


@mock.patch('api.main.get_db_data')
def test_main_train_data_mock(train_data_mock, dummy_df, dummy_dict_list):
    
    train_data_mock.return_value = dummy_df
    actual = client.get('/train_data')
    expected = dummy_dict_list
    
    assert actual.status_code == 200
    assert actual.json() == expected



