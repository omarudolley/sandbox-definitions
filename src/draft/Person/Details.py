from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PersonDetailsRequest(CamelCaseModel):
    pass


class PersonDetailsResponse(CamelCaseModel):
    name: str = Field(
        ...,
        title="Full name",
        description="Person's name and surname",
        examples=["Joshua Gray"],
    )
    address: str = Field(
        ...,
        title="Address",
        description="Person's home address",
        examples=["6 Raymond river\nRileybury\nCR3 6XA"],
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    deprecated=True,
    title="Person details",
    description="Details about a person such as home address",
    request=PersonDetailsRequest,
    response=PersonDetailsResponse,
    requires_authorization=True,
)
