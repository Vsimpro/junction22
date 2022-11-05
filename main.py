import sys, sqlite3

from modules.config import *
from modules.distance import *


class Database:
    # Initializing database connection 
    DB_FILE = "data/main.db"
    with open(DB_FILE, "w+") as file:
        file.close()

    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    # Creating necessary tables
    try:
        cur.execute("CREATE TABLE Distances(location_a, location_b, distance)")
        cur.execute("CREATE TABLE Nodes(location)")
    except Exception as e:
        print(e); sys.exit(1)

    def add_node(this, location):
        node = location.replace(" ", "_")

        try:
            this.cur.execute(f"INSERT INTO Nodes VALUES('{node}')")
        except Exception as e:
            print(e)

    def add_distances(this, location_a, location_b, distance):
        location_a = location_a.replace(" ", "")
        location_b = location_b.replace(" ", "")

        try:
            this.cur.execute(f"INSERT INTO Distances VALUES('{location_a}','{location_b}', '{distance}')")
        except Exception as e:
            print(e)


# Store locations
class Nodes:
    array = []


def create_node(this_node):
    if settings.verbose: print(f"[+] Creating node {this_node}")
    
    table_name = this_node.replace(" ", "_")

    Nodes.array.append(table_name)
    Database.add_node(Database, table_name)

    if len(Nodes.array) <= 1:
        if settings.verbose: print("[...] First node, skipping calculating distance.")

        if settings.verbose: return 0

    
    location_1 = this_node
    for node in Nodes.array:
        location_2 = node.replace("_", " ")

        if location_1 == location_2:
            continue

        print(f"\n  {location_1[:6]}.., {location_2[:6]}.. :\t", end=" ")
        distance = round(calculate_distance(location_1, location_2), 3)
        print(distance, "km")
        

    return 0

if __name__ == "__main__":
    Database()
    locations = [
        "Mannerheimintie 4",
        "Yrjönkatu 8",
        "Linnankatu 7"
    ]
    for location in locations:
        if create_node(location) == 0 and settings.verbose:
            print("[✔] Success.")

