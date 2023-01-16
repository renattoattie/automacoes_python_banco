import subprocess
import os

host = "XX.XX.XXX.XX"
user = "postgres"
db = "postgres"
password = "XXXXXXX"
os.environ["PGPASSWORD"] = password  # password

# Get a list of all databases
databases = subprocess.run(f"psql.exe -h {host} -d {db} -U {user} -l -t", shell=True, capture_output=True, text=True).stdout.strip().split("\n")[3:]
databases = [db.split("|")[0].strip() for db in databases]

# Remove empty databases
filtered_databases = list(filter(lambda x: x != '', databases))

# Loop through each database and run VACUUM and REINDEX
for database in filtered_databases:
    print ("Executando VACCUM para: "+ database)
    subprocess.run(f"vacuumdb -h {host} -U {user} -d {database}", shell=True, capture_output=True, text=True)
    print ("Executando REINDEX para: "+ database)
    subprocess.run(f"reindexdb -h {host} -U {user} -d {database}", shell=True, capture_output=True, text=True)
