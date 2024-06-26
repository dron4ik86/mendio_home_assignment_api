Feature: BitBucket API Integration

  @repositories
  Scenario Outline: Manage repositories
    Given I create new repository <repository_name> for project <project_key> under workspace <workspace_id>
    When I send a request to get repository <repository_name> under workspace <workspace_id>
    And I delete repository <repository_name> that was created under workspace <workspace_id>
    Then I should not see the repository <repository_name> under workspace <workspace_id>

    Examples:
    | project_key | repository_name | workspace_id |
    | MEN         | just_test       | mendio1      |
