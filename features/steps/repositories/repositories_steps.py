from behave import step
from lib.repositories.repositories import Repositories
import config as cfg


@step('I create new repository {repository_name} for project {project_key} under workspace {workspace_id}')
def create_repository(context, repository_name, project_key, workspace_id):
    context.response = Repositories().create_repositories(cfg.BASE_URL, project_key, repository_name, workspace_id)
    context.response_json = context.response.json()
    assert context.response.status_code == 200, f"The response status code is {context.response.status_code}"


@step('I send a request to get repository {repository_name} under workspace {workspace_id}')
def is_repository_created(context, repository_name, workspace_id):
    context.response = Repositories().get_repository(cfg.BASE_URL, repository_name, workspace_id)
    context.response_json = context.response.json()
    assert context.response.status_code == 200, f"The response status code is {context.response.status_code}"
    extracted_repository_name = context.response_json['full_name'].split('/')[-1]
    assert extracted_repository_name == repository_name, \
        f"The repository full name is {context.response_json['full_name']}, but expected {repository_name}"


@step('I delete repository {repository_name} that was created under workspace {workspace_id}')
def delete_repository(context, repository_name, workspace_id):
    context.response = Repositories().delete_repositories(cfg.BASE_URL, repository_name, workspace_id)
    assert context.response.status_code == 204, f"The response status code is {context.response.status_code}"


@step('I should not see the repository {repository_name} under workspace {workspace_id}')
def is_repository_exists(context, repository_name, workspace_id):
    context.response = Repositories().get_repository(cfg.BASE_URL, repository_name, workspace_id)
    context.response_json = context.response.json()
    assert context.response.status_code == 404, f"The response status code is {context.response.status_code}"

