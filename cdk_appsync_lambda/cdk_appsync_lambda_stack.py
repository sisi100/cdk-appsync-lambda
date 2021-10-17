from aws_cdk import core as cdk
import aws_cdk.aws_appsync as appsync
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python import PythonFunction


class CdkAppsyncLambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_ = PythonFunction(self, f"HogeLambda", entry="src", runtime=Runtime.PYTHON_3_9)

        api = appsync.GraphqlApi(
            self, "HogeApi", name="HogeApi", schema=appsync.Schema.from_asset("./schema/schema.graphql"),
        )

        lambda_datasource = api.add_lambda_data_source("HogeLambdaSource", lambda_)
        lambda_datasource.create_resolver(type_name="Query", field_name="getUsers")
        lambda_datasource.create_resolver(
            type_name="Mutation", field_name="addUser",
        )
