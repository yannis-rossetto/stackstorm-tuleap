import sys
import requests
from st2actions.runners.pythonrunner import Action

class GetProjects(Action):
    def run(self):
        requests.packages.urllib3.disable_warnings()

        url = 'https://' + str(self.config['tuleap_domain_name']) + '/api/v1/projects'
        request_get_projects = requests.get(url, verify=False)

        print(request_get_projects.text)