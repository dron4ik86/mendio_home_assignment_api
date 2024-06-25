from lib.auth.auth import auth


def before_all(context):
    context.workspace_token = auth()


def before_feature(context, feature):
    ...


def before_scenario(context, scenario):
    ...


def after_scenario(context, scenario):
    ...


def after_all(context):
    ...


def before_step(context, step):
    ...


def after_step(context, step):
    ...
