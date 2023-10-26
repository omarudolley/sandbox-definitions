from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnStandardCertification(CamelCaseModel):
    en_standard_code: Optional[str] = Field(
        None,
        title="EN Standard Code",
        max_length=20,
        description="The identification code of the EN standard that the product is compliant with",
        example="EN 10002-1, EN 10002-5",
    )


class Measures(CamelCaseModel):
    width: Optional[int] = Field(
        None,
        title="Width",
        description="The width of the product measured in centimeters",
        example=1500,
    )
    length: Optional[int] = Field(
        None,
        title="Length",
        description="The length of the product measured in centimeters",
        example=4000,
    )
    height: Optional[int] = Field(
        None,
        title="Height",
        description="The height of the product measured in centimeters",
        example=0,
    )


class MetalArtifactDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product identifier",
        description="Technical product identifier used by the manufacturer",
        example="battery-100wh-s",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier for the product",
        example="177389-09633",
    )


class MetalArtifactDataSheetResponse(CamelCaseModel):
    product_name: str = Field(
        ...,
        title="Product Name",
        max_length=250,
        description="The commercial name of the metal product",
        example="HOT-DIP ZINC-COATED STEEL STRIP, HIGH STRENGTH STEEL FOR COLD FORMING",
    )
    product_type: str = Field(
        ...,
        title="Product Type",
        max_length=250,
        description="The type of the metal product",
        example="Steel roll",
    )
    measures: Optional[Measures] = Field(
        None,
        title="Measures",
        description="The dimensional measures of the metal product",
    )
    net_weight: float = Field(
        ...,
        title="Net Weight",
        description="Net weight of the steel roll in kilograms",
        example=11720.0,
    )
    en_standard_certification: List[EnStandardCertification] = Field(
        ...,
        title="EN Standard Certification",
        description="The list of EN standards",
    )
    treatment_type: Optional[str] = Field(
        None,
        title="Treatment Type",
        max_length=20,
        description="The type of re-treatment for the steel roll",
        example="Prelube oil",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Data Sheet For Metal Artifacts",
    description="Returns the basic product information of a metal product",
    request=MetalArtifactDataSheetRequest,
    response=MetalArtifactDataSheetResponse,
    requires_authorization=False,
    requires_consent=False,
)
