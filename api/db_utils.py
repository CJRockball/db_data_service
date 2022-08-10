import sqlite3
import pathlib
import pandas as pd
import numpy as np

PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_PATH / "api/tips.db"

def get_db_data(choose_data):
    global DB_PATH
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        if choose_data == "train":
            cur.execute("SELECT total_bill, tip, sex, smoker, day, time,g_size FROM train_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'g_size'])
        elif choose_data == "test":
            cur.execute("SELECT total_bill, tip, sex, smoker, day, time,g_size FROM test_table;")
            result = cur.fetchall()
            df = pd.DataFrame(result, columns=['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'g_size'])
        else: df=""
        
        return df
    
def get_random_test_data():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM test_table ;")
        row_count = cur.fetchall()
    
    random_row = np.random.randint(0,row_count[0][0])
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT total_bill, tip, sex, smoker, day, time,g_size FROM test_table WHERE id = ?;", (random_row,))
        result = cur.fetchall()
        
        df = pd.DataFrame(result, columns=['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'g_size'])
    
    return df