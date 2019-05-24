#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from lib.certification import Certification
from toggl.TogglPy import Toggl
from lib.argument import Argument

class Main():
    

    def main(self):
        API_TOKEN = certification.load_json()
        if not API_TOKEN:
            print('[WARN]:Please set the API token in config.json')
        toggl = Toggl()
        toggl.setAPIKey(API_TOKEN)
        workspace_id = self.get_workspace_id(toggl)
        self.get_project(toggl, workspace_id)
        args = argument.get_argument()
        if args.function.lower() == 'start':
            self.start(toggl)
        elif args.function.lower() == 'stop':
            self.stop(toggl)

    def get_workspace_id(self, toggl):
        workspace = toggl.getWorkspace(name="yamachaaan's workspace")
        workspace_id = workspace['id']
        return workspace_id

    def get_project(self, toggl, workspace_id):
        end_point = "https://www.toggl.com/api/v8/workspaces/%s/projects" % (workspace_id)
        print(end_point)
        response = toggl.request(end_point)
        for project in response:
            print("id: %s name: %s" % (project['id'], project['name']))

    def start(self, toggl):
        myproject_id = input('Project_id?')
        entry_name = input('Entry_name?')
        if not myproject_id:
            myproject_id = 151778455
        if not entry_name:
            entry_name = 'test'
        toggl.startTimeEntry(entry_name, myproject_id)

    def stop(self, toggl):
        currentTimer = toggl.currentRunningTimeEntry()
        toggl.stopTimeEntry(currentTimer['data']['id'])

if __name__ == '__main__':
    certification = Certification()
    argument = Argument()
    main = Main()
    main.main()
