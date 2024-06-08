import aws_cdk as core
import aws_cdk.assertions as assertions

from sales_lambda_athena_project1.sales_lambda_athena_project1_stack import SalesLambdaAthenaProject1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in sales_lambda_athena_project1/sales_lambda_athena_project1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SalesLambdaAthenaProject1Stack(app, "sales-lambda-athena-project1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
