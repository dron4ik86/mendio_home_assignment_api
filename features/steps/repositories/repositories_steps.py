import json
from behave import step
from lib.repositories.repositories import Repositories
import config as cfg
from logging_config import log


@step('I create new repository {repository_name} for project {project_key} under workspace {workspace_id}')
def create_repository(context, repository_name, project_key, workspace_id):
    log.info("create_repository")
    context.response = Repositories().create_repositories(cfg.BASE_URL, project_key, repository_name, workspace_id)
    context.response_json = context.response.json()
    log.debug(json.dumps(context.response_json, indent=4))
    assert context.response.status_code == 200, f"The response status code is {context.response.status_code}"


@step('I send a request to get repository {repository_name} under workspace {workspace_id}')
def is_repository_created(context, repository_name, workspace_id):
    log.info("is_repository_created")
    context.response = Repositories().get_repository(cfg.BASE_URL, repository_name, workspace_id)
    context.response_json = context.response.json()
    log.debug(json.dumps(context.response_json, indent=4))
    assert context.response.status_code == 200, f"The response status code is {context.response.status_code}"
    extracted_repository_name = context.response_json['full_name'].split('/')[-1]
    assert extracted_repository_name == repository_name, \
        f"The repository full name is {context.response_json['full_name']}, but expected {repository_name}"


@step('I delete repository {repository_name} that was created under workspace {workspace_id}')
def delete_repository(context, repository_name, workspace_id):
    log.info("delete_repository")
    context.response = Repositories().delete_repositories(cfg.BASE_URL, repository_name, workspace_id)
    log.debug(context.response.status_code)
    assert context.response.status_code == 204, f"The response status code is {context.response.status_code}"


@step('I should not see the repository {repository_name} under workspace {workspace_id}')
def is_repository_exists(context, repository_name, workspace_id):
    log.info("is_repository_exists")
    context.response = Repositories().get_repository(cfg.BASE_URL, repository_name, workspace_id)
    context.response_json = context.response.json()
    log.debug(json.dumps(context.response_json, indent=4))
    assert context.response.status_code == 404, f"The response status code is {context.response.status_code}"

