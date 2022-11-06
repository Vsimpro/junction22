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
        location_a = location_a.replace(" ", "_")
        location_b = location_b.replace(" ", "_")

        try:
            this.cur.execute(f"INSERT INTO Distances VALUES('{location_a}','{location_b}', '{distance}')")
        except Exception as e:
            print(e)

    def get_distances(this, location):
        try:
            res = this.cur.execute(f"SELECT location_a, location_b, distance FROM Distances WHERE location_a = '{location}' or location_b = '{location}'")
            return res.fetchall()
        except Exception as e:
            print(e)

# Store locations
class Nodes:
    array = []
    delivery_list = []

class Count:
    count = 0


def Group(location_1, location_2, distance):
    
    duplicate = False
    if distance < settings.distance:
        newlist = []
        newlist.append(location_1)
        newlist.append(location_2)

        for item in Nodes.delivery_list:
            if item[0] == newlist[1] and item[1] == newlist[0]:
                print("Duplicate!")
                duplicate = True
            

        if not duplicate:
            Nodes.delivery_list.append(newlist)


        print(f"\n{location_1[:6]}..{location_1[-2:]}, {location_2[:6]}..{location_2[-2:]}\t", end=" ")
        print(distance, "km")
        Count.count += 1

    def find_pairs(location):
        distances = []
        res = Database.get_distances(Database, location.replace(" ", "_"))
        if res not in distances:
            distances.append(res)
            for node in res:
                node = tuple(node)

                dest = node[1].replace("_", " ")
                dist = node[2]

                if  dest == location:
                    dest = node[0].replace("_", " ")
                    Group(location, dest, float(dist))

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

        if settings.verbose: print(f"\n  {location_1[:6]}..{location_1[-2:]}, {location_2[:6]}..{location_2[-2:]} :\t", end=" ")
        distance = round(calculate_distance(location_1, location_2), 3)
        Database.add_distances(Database, location_1, location_2, distance)   
        if settings.verbose: print(distance)

          

    return 0

def main():
    Database()
    locations = [
        "Mannerheimintie 4",
        "Yrjönkatu 8",
        "Linnankatu 7",
        "Rälssintie 4",
        "Rälssintie 6"
    ]
    for location in locations:
        if create_node(location) == 0 and settings.verbose:
            print("[✔] Success.")

    for location in locations:
        distances = []

        print(location)
        res = Database.get_distances(Database, location.replace(" ", "_"))
        if res not in distances:
            distances.append(res)
            for node in res:
                node = tuple(node)

                dest = node[1].replace("_", " ")
                dist = node[2]

                if  dest == location:
                    dest = node[0].replace("_", " ")

                Group(location, dest, float(dist))
    print(Count.count)
    print(Nodes.delivery_list)   
