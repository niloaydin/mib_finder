import json

def load_previous_mib_state():
    try:
        with open("previous_mib_state.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        return {"version": 1, "mibs": {}}


def load_mib_dictionary():
    try:
        with open("mib_dictionary.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:

        return {"version": 1, "mibs": {}}


def save_mib_dictionary():

    mib_dict = load_mib_dictionary()


    previous_mib_state = load_previous_mib_state()


    if mib_dict.get("mibs") != previous_mib_state.get("mibs"):

        existing_version = mib_dict.get("version", 1)
        new_version = existing_version + 1
        mib_dict["version"] = new_version


    with open("mib_dictionary.json", "w") as file:
        json.dump(mib_dict, file, indent=4)


    with open("previous_mib_state.json", "w") as file:
        json.dump(mib_dict, file, indent=4)

save_mib_dictionary()
