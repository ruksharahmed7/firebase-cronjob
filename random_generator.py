import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore 
from dotenv import load_dotenv
import os
import json
load_dotenv()
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def main():
    # Fetch the service account key JSON file contents
    json_key = json.loads(os.environ.get('FIREBASE_CONFIG'))
    cred = credentials.Certificate(json_key)
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://fir-gitaction-cron-default-rtdb.asia-southeast1.firebasedatabase.app"
    })

    # json_data = json.dumps(json_key)
    # print(json_data)

    #generate random data
    random_number = random.randint(1, 100)
    age = random_number

    random_string = generate_random_string(10)
    name = random_string

    #calculate index number
    # Get a reference to the database root
    ref = db.reference('/')

    # Retrieve all reference keys
    snapshot = ref.get(shallow=True)
    keys = list(snapshot.keys()) if snapshot else []
    index = len(keys)

    #insert data into firebase realtime databaes
    # Get a reference to the database root
    ref = db.reference('/'+str(index))

    # Push data to a specific location
    data = {'name': name, 'age': age}
    ref.set(data)

if __name__ == '__main__':
    main()