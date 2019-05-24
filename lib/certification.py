class Certification:
    def load_json(self):
        import json
        f = open('./config.json', 'r')
        json_data = json.load(f)
        f.close()
        return json_data['api_token']

    def default_workspace(self):
        import json
        f = open('./config.json', 'r')
        json_data = json.load(f)
        f.close()
        return json_data['default_workspace']

