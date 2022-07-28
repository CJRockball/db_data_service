import sqlite3
import pandas as pd
import pathlib



def setup_db(path):
    # Connect to db
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    # Create a table
    cur.execute("""DROP TABLE IF EXISTS train_table""")
    cur.execute("""DROP TABLE IF EXISTS test_table""")
        
    cur.execute(
        """CREATE TABLE IF NOT EXISTS train_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total_bill REAL,
                    tip REAL,
                    sex TEXT,
                    smoker TEXT,
                    day TEXT,
                    time TEXT,
                    g_size INT);"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS test_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total_bill REAL,
                    tip REAL,
                    sex TEXT,
                    smoker TEXT,
                    day TEXT,
                    time TEXT,
                    g_size INT);"""
    )

    # Write changes
    conn.commit()
    conn.close()
    
    return


def data_insert(data_tuple, command_code):
    global DB_PATH
    # Create a table
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for entry in data_tuple:
            cur.execute(command_code,entry)

    return


def tuplefy(df):
    data_tuple = [tuple(x[1:]) for x in df.to_numpy()]
    return data_tuple

#if __name__ == "__main":
ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DB_PATH = ROOT_DIR / "app/tips.db"
print(DB_PATH)

print('>>>> setup_db start')
setup_db(DB_PATH)
print('>>>> setup_db complete')
print(">>>Load data")
if DATA_DIR.exists():
    try:
        df = pd.read_csv(DATA_DIR / "tips.csv")
    except Exception as error:        
        print("Couldn't load data", error)
else:
    print('No file found')

print(">>>> Split data")
data_size = df.shape[1]
train_size = int(0.8 * data_size)
df_train = df.iloc[:train_size,:]
df_test = df.iloc[train_size:,:]

print('>>>> tuplefy')
train_tuple = tuplefy(df_train)
test_tuple = tuplefy(df_test)
print('>>>> train_tuple complete')
print('>>>> db_insert start')
data_insert(train_tuple, "INSERT OR IGNORE INTO train_table (total_bill, tip, sex, smoker, day, time,g_size) VALUES (?,?,?,?,?,?,?);" "")
data_insert(test_tuple, "INSERT OR IGNORE INTO test_table (total_bill, tip, sex, smoker, day, time,g_size) VALUES (?,?,?,?,?,?,?);" "")
print('>>>> db_insert complete')