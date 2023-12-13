from typing import Annotated, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field, HttpUrl, UrlConstraints

HttpsUrl = Annotated[
    HttpUrl,
    UrlConstraints(allowed_schemes=["https"]),
]


class ManufacturerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        max_length=250,
        title="Name",
        description="The registered trade name of the battery manufacturer company",
        examples=["Sandvik"],
    )
    street_name: str = Field(
        ...,
        title="Street Name",
        max_length=40,
        description="The street address of the manufacturer's headquarters",
        examples=["Kungsbron 1"],
    )
    postal_code: str = Field(
        ...,
        title="Postal Code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters",
        examples=["111 22"],
    )
    city: str = Field(
        ...,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters",
        examples=["Stockholm"],
    )
    country: str = Field(
        ...,
        title="Country",
        max_length=3,
        description="The country code of the manufacturer's headquarters location in Alpha-3 format",
        examples=["SWE"],
    )
    website: Optional[HttpsUrl] = Field(
        None,
        title="Website",
        description="The website of the battery manufacturer",
        examples=["https://www.home.sandvik"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer",
        examples=["info@sandvik.com"],
    )


class ManufacturingDataSheetResponse(CamelCaseModel):
    product_name: str = Field(
        ...,
        max_length=150,
        title="Product Name",
        description="The official sales name of the product",
        examples=["BEV Longhole Drill"],
    )
    manufacturer_information: ManufacturerInformation = Field(
        ...,
        title="Manufacturer Information",
        description="The details of the drill manufacturer",
    )
    boom_coverage: float = Field(
        ...,
        title="Boom Coverage",
        description="The largest distance to which the drill boom can reach from the machine in meters (m)",
        examples=[3.0],
    )
    tramming_distance: float = Field(
        ...,
        title="Tramming Distance",
        description="The maximum tramming distance of the drill movement in kilometers (km)",
        examples=[3.0],
    )
    maximum_hole_length: float = Field(
        ...,
        title="Hole Length",
        description="The maximum length of the drilled hole in meters (m)",
        examples=[54.0],
    )
    minimum_hole_diameter: float = Field(
        ...,
        title="Minimum Hole Diameter",
        description="The minimum diameter measure of the drilling hole in millimeters (mm)",
        examples=[76.0],
    )
    maximum_hole_diameter: float = Field(
        ...,
        title="Maximum Hole Diameter",
        description="The maximum diameter measure of the drilling hole in millimeters (mm)",
        examples=[127.0],
    )
    drilling_power: float = Field(
        ...,
        title="Drilling Power",
        description="The maximum drilling power of the machine in kilowatts (kW)",
        examples=[160.0],
    )
    reference_data_sheet: HttpsUrl = Field(
        ...,
        title="Reference Material",
        description="The link to the detailed product specifications",
        examples=["https://company/products/dl422ie/productdocument"],
    )
    safety_data_sheet: HttpsUrl = Field(
        ...,
        title="Safety Data Sheet",
        description="The link to the safety control measures of the product",
        examples=["https://company/products/dl422ie/productdocument"],
    )


class ManufacturingDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["dl422ie"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Drill Manufacturing Data Sheet",
    description="Manufacturing data sheet of a Mobile Drill Machine",
    request=ManufacturingDataSheetRequest,
    response=ManufacturingDataSheetResponse,
)
