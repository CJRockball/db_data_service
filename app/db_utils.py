import sqlite3
import pathlib
import pandas as pd


PROJECT_PATH = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_PATH / "app/tips.db"

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