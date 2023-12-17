
import pyodbc
import pandas as pd
def fetch_data_from_db(connection_string, query):

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


import pytest

@pytest.fixture
def db_connection_string():
    return "DRIVER={SQL Server};SERVER=TSaqqadlg01;DATABASE=PlanIntegration_TSA_UAT;"

def test_fetch_data_from_db(db_connection_string):
    query = "SELECT * FROM process"
    result = fetch_data_from_db(db_connection_string, query)

    for row in result:
        print(row)
    assert len(result) > 0







