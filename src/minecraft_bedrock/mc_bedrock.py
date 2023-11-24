import json

class MinecraftBedrock():
    def __init__(self) -> None:
        pass

    def load_json_file(self, filepath):
        with open(filepath) as f:
            data = json.load(f)
            return data
        
    def write_json_file(self, filepath, data):
        json_data = json.dumps(data, indent=4)

        with open(filepath, "w") as outfile:
            outfile.write(json_data)

    def add_allowlist_user(self, allowlist_filepath, xuid, name):
        allowlist = self.load_json_file(allowlist_filepath)

        allowlist.append({"ignoresPlayerLimit":False,"name":name,"xuid":xuid})

        self.write_json_file(allowlist_filepath, allowlist)

    def remove_allowlist_user(self, allowlist_filepath, name):
        allowlist = self.load_json_file(allowlist_filepath)

        new_allowlist = [user for user in allowlist if user['name'].lower() != name.lower()]

        self.write_json_file(allowlist_filepath, new_allowlist)

    def get_allowlist(self, allowlist_filepath):
        allowlist = self.load_json_file(allowlist_filepath)
        return allowlist

