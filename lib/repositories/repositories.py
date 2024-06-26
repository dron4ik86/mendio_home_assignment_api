from lib.utils import build_requests_headers, handle_response
import config as cfg
import requests
from logging_config import log


class Repositories:

    def __init__(self):
        self.repositories_url = "/repositories"

    def create_repositories(self, base_url, project_key, repo_name, workspace_id):
        log.info(f"Repositories: create_repositories")
        data = {
            "scm": "git",
            "project": {
                "key": f"{project_key}"
            },
            "is_private": True
        }

        request_headers = build_requests_headers(cfg.WORKSPACE_TOKEN)
        log.debug(request_headers)
        url = f"{base_url}{self.repositories_url}/{workspace_id}/{repo_name}"
        response = requests.post(url, headers=request_headers, json=data)
        handle_response(response)

        return response

    def get_repository(self, base_url, repository_name, workspace_id):
        log.info(f"Repositories: get_repository")
        url = f"{base_url}{self.repositories_url}/{workspace_id}/{repository_name}"
        request_headers = build_requests_headers(cfg.WORKSPACE_TOKEN)
        log.debug(request_headers)
        response = requests.get(url, headers=request_headers)

        return response

    def delete_repositories(self, base_url, repository_name, workspace_id):
        log.info(f"Repositories: delete_repositories")
        url = f"{base_url}{self.repositories_url}/{workspace_id}/{repository_name}"
        request_headers = build_requests_headers(cfg.WORKSPACE_TOKEN)
        log.debug(request_headers)
        response = requests.delete(url, headers=request_headers)

        return response

