
import pyodbc
import pandas as pd
import pytest


def execute_sql_query(connection_string, query):

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    connection.close()
    return result

""""
import pytest

@pytest.fixture
def db_connection_string():
    return "DRIVER={SQL Server};SERVER=TSaqqadlg01;DATABASE=PlanIntegration_TSA_UAT;"
    """
def export_to_excel(results, excel_file_path):
    df = pd.DataFrame(results)
    df.to_excel(excel_file_path, index=False)

@pytest.fixture

def connection_string():
    return "DRIVER={SQL Server};SERVER=TSaqqadlg01;DATABASE=PlanIntegration_TSA_UAT;"

def test_sql_query(connection_string):
    query = "SELECT * FROM process"
    result = execute_sql_query(connection_string, query)

    for row in result:
        print(row)
    assert len(result) > 0

    excel_file_path = "sample_results.xlsx"
    export_to_excel(result, excel_file_path)



















