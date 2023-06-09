from . import database
from . import database, responses
import bcrypt


async def email_finder(email):
    existing_user = database.user_collection.find_one({"email": email})
    if existing_user is not None:
        return False
    else:
        return True


# hashes passwords using utf8
def hash_password(password: str) -> str:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Return the hashed password as a string
    return hashed_password.decode("utf-8")


# verifies the credentials from mongodb
async def verify_credentials(username: str, password: str) -> bool:
    user = await full_user_data(username)
    if user is None:
        return False
    hashed_password = user["password"].encode("utf-8")
    is_valid_password = bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return is_valid_password


async def inserter(metadata: dict):
    database.user_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)


# gets full user data
async def full_user_data(email):
    user = database.user_collection.find_one({"email": email})
    if not user:
        return responses.response(False, "does not exist", email)
    return user


def single_hack_data(title):
    hack = database.hackathon_collection.find_one({"title": title})
    if not hack:
        return responses.response(False, "does not exist", title)
    return hack


# gets all the data in the collection
def get_all_data():
    response = database.user_collection.find({})
    return list(response)


# gets all the hacks in the collection
def get_all_hacks():
    response = database.hackathon_collection.find({})
    return list(response)


# updates hacks created by user
def user_hack_created_updater(WrongValue, CorrectValue):
    database.user_collection.update_one(
        {"email": WrongValue}, {"$set": {"hacks_created": CorrectValue}}, upsert=True
    )


# updates submissions by the user


def user_submissions_updater(WrongValue, CorrectValue):
    database.user_collection.update_one(
        {"email": WrongValue}, {"$set": {"submissions": CorrectValue}}, upsert=True
    )


# updates enlisted hacks by the user
def user_hack_enlisted_updater(WrongValue, CorrectValue):
    database.user_collection.update_one(
        {"email": WrongValue}, {"$set": {"hacks_enlisted": CorrectValue}}, upsert=True
    )


# inserts hackathons
def hack_inserter(metadata: dict):
    database.hackathon_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)


# inserters submissions into collection
def submission_inserter(metadata: dict):
    database.submission_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)


# verifies if the hack is valid or not
def hack_verifier(title):
    existing_hack = database.hackathon_collection.find_one({"title": title})
    if existing_hack is not None:
        return False
    else:
        return True
