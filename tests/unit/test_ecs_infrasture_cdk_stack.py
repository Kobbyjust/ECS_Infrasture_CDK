import aws_cdk as core
import aws_cdk.assertions as assertions

from ecs_infrasture_cdk.ecs_infrasture_cdk_stack import EcsInfrastureCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ecs_infrasture_cdk/ecs_infrasture_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EcsInfrastureCdkStack(app, "ecs-infrasture-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
