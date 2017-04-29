import sys
import requests
from st2actions.runners.pythonrunner import Action

class GetProjects(Action):
    def run(self):
        requests.packages.urllib3.disable_warnings()

        tuleap_domain_name = self.config['tuleap_domain_name']
        username = self.config['tuleap_username']
        password = self.config['tuleap_password']

        url = 'https://' + str(tuleap_domain_name) + '/api/v1/projects'
        request_get_projects = requests.get(url, auth=(username, password), verify=False)

        print(request_get_projects.text)