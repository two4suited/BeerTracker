from aws_cdk import (
    core as core,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamo
)


class InfrastructureStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        core.Tag("Project","BeerTracker")

        beerdb = _dynamo.Table(
            self, 'beers',
            table_name="Beers",
            billing_mode=_dynamo.BillingMode.PAY_PER_REQUEST,
            partition_key=_dynamo.Attribute(
                name="LocationName",
                type=_dynamo.AttributeType.STRING
            ),
            sort_key=_dynamo.Attribute(
                name="BeerName",
                type=_dynamo.AttributeType.STRING
            ),
            removal_policy=core.RemovalPolicy.DESTROY
        )

        locationdb = _dynamo.Table(
            self, 'locations',
            table_name="Locations",
            billing_mode=_dynamo.BillingMode.PAY_PER_REQUEST,
            partition_key=_dynamo.Attribute(
                name="LocationName",
                type=_dynamo.AttributeType.STRING
            ),
            removal_policy=core.RemovalPolicy.DESTROY
        )
