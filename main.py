from toggl.TogglPy import Toggl

toggl = Toggl()

response = toggl.request("https://www.toggl.com/api/v8/clients")
myproject_id = 151778455
#toggl.startTimeEntry("test", myproject_id)
currentTimer = toggl.currentRunningTimeEntry()
toggl.stopTimeEntry(currentTimer['data']['id'])
