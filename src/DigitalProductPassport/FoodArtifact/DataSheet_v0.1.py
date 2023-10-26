from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class FatContentType(CamelCaseModel):
    fats: float = Field(
        ...,
        title="Fats",
        description="The amount of fat per 100g measured in grams",
        example=6,
    )
    saturated_fats: float = Field(
        ...,
        title="Saturated Fats",
        description="The amount of saturated fat per 100g measured in grams",
        example=0.4,
    )


class EnergyContentType(CamelCaseModel):
    energy: int = Field(
        ...,
        title="Energy",
        description="The amount of energy per 100g measured in kilojoules",
        example=750,
    )
    calories: int = Field(
        ...,
        title="Calories",
        description="The amount of calories per 100g measured in kilocalories",
        example=180,
    )


class FoodArtifactDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product code",
        description="The product code used for identifying the product type",
        example="french-fries-500g",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product",
        example="550e8400-e29b-41d4-a716-446655440000",
    )


class FoodArtifactDataSheetResponse(CamelCaseModel):
    energy_content: EnergyContentType = Field(
        ...,
        title="Energy Content",
        description="The details of the energy content of the food artifact",
    )
    fat_content: FatContentType = Field(
        ...,
        title="Fat Content",
        description="The details of the fat content of the food artifact",
    )
    carbon_hydrates: float = Field(
        ...,
        title="Carbon Hydrates",
        description="The amount of carbon hydrates per 100g measured in grams",
        example=28,
    )
    sugar: float = Field(
        ...,
        title="Sugar",
        description="The amount of sugar per 100g measured in grams",
        example=0.5,
    )
    protein: float = Field(
        ...,
        title="Protein",
        description="The amount of protein per 100g measured in grams",
        example=3,
    )
    salt: float = Field(
        ...,
        title="Salt",
        description="The amount of salt per 100g measured in grams",
        example=0.01,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Food Artifact Nutritional Values",
    description="Returns the nutritional values of a food product",
    request=FoodArtifactDataSheetRequest,
    response=FoodArtifactDataSheetResponse,
    requires_authorization=False,
    requires_consent=False,
)
