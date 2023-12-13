from typing import Annotated, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field, HttpUrl, UrlConstraints

HttpsUrl = Annotated[
    HttpUrl,
    UrlConstraints(allowed_schemes=["https"]),
]


class ManufacturingLocation(CamelCaseModel):
    country: str = Field(
        ...,
        title="Country",
        max_length=3,
        description="The country code of the battery manufacturing location in Alpha-3 format",
        examples=["CHE"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the battery manufacturing location",
        examples=["Stabio"],
    )


class ManufacturerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        max_length=250,
        title="Name",
        description="The registered trade name of the battery manufacturer company",
        examples=["FZSonic"],
    )
    street_name: str = Field(
        ...,
        title="Street Name",
        max_length=40,
        description="The street address of the manufacturer's headquarters",
        examples=["Viale Europa 81"],
    )
    postal_code: str = Field(
        ...,
        title="Postal Code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters",
        examples=["VI 36075"],
    )
    city: str = Field(
        ...,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters",
        examples=["Montecchio Maggiore"],
    )
    country: str = Field(
        ...,
        title="Country",
        max_length=3,
        description="The country code of the manufacturer's headquarters location in Alpha-3 format",
        examples=["ITA"],
    )
    website: Optional[HttpsUrl] = Field(
        None,
        title="Website",
        description="The website of the battery manufacturer",
        examples=["https://www.fzsonick.com"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer",
        examples=["info@fzsonick.com"],
    )


class CarbonFootprint(CamelCaseModel):
    pre_production_footprint: float = Field(
        ...,
        title="Pre Production Footprint",
        description="The carbon footprint of the raw material acquisition and pre-processing phase of the battery calculated as kilograms (kg) of CO2e per one kilowatt-hour (kWh) using preferably PEF and PEFCR methods",
        examples=[2345.7],
    )
    main_production_footprint: float = Field(
        ...,
        title="Main Production Footprint",
        description="The carbon footprint of the battery main production phase calculated as kilograms (kg) of CO2e per one kilowatt-hour (kWh) using preferably PEF and PEFCR methods",
        examples=[3504.4],
    )
    reference_material: HttpsUrl = Field(
        ...,
        title="Reference Material",
        description="The web link giving access to a public version of the study supporting the carbon footprint values",
        examples=["https://company/carbonFootprintAnalysis/z37-310-76"],
    )


class CarbonFootprintResponse(CamelCaseModel):
    manufacturer_information: ManufacturerInformation = Field(
        ...,
        title="Manufacturer Information",
        description="The details of the battery manufacturer",
    )
    battery_model: str = Field(
        ...,
        max_length=40,
        title="Battery Model",
        description="The model of the battery",
        examples=["Z37-310-76"],
    )
    conformity_declaration: HttpsUrl = Field(
        ...,
        title="Conformity Declaration",
        description="The link to the EU declaration of conformity documentation",
        examples=["https://company/EUdeclaration/z37-310-76"],
    )
    manufacturing_location: ManufacturingLocation = Field(
        ...,
        title="Manufacturing Location",
        description="The details of the location of the battery manufacturing plant",
    )
    carbon_footprint: CarbonFootprint = Field(
        ...,
        title="Carbon Footprint",
        description="The details of the carbon footprint for the battery production phases",
    )


class CarbonFootprintRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["sodium-ion-75kWh"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["660e8400-e29b-41d4-a716-446655440000"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Battery Carbon Footprint",
    description="Carbon footprint of a battery as required by the European Commission's Battery Act (2023/1542)",
    request=CarbonFootprintRequest,
    response=CarbonFootprintResponse,
)
