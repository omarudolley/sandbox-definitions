from datetime import datetime
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class ManufacturerLocation(CamelCaseModel):
    country: Optional[str] = Field(
        None,
        title="Country",
        max_length=3,
        description="The country code of the battery manufacturing location in Alpha-3 format",
        examples=["CHE"],
    )
    city: str = Field(
        ...,
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
    website: Optional[str] = Field(
        None,
        title="Website",
        description="The website of the battery manufacturer",
        examples=["https://www.fzsonick.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer",
        examples=["info@fzsonick.com"],
    )


class BatteryCategory(str, Enum):
    STATIONARY_ENERGY_STORAGE = "stationary energy storage"
    INDUSTRIAL_BATTERY = "industrial battery"
    LMT_BATTERY = "lmt battery"
    ELECTRIC_VEHICLE_BATTERY = "electric vehicle battery"


class CellType(str, Enum):
    SODIUM_ION = "sodium-ion"


class RoundTripEfficiency(CamelCaseModel):
    initial_energy_efficiency: Optional[float] = Field(
        None,
        title="Initial Energy Efficiency",
        description="The initial round trip energy efficiency of an energy storage battery in percentage (%)",
        examples=[75.0],
    )
    degraded_energy_efficiency: Optional[float] = Field(
        None,
        title="Degraded Energy Efficiency",
        description="The round trip energy efficiency of an energy storage battery in percentage (%) at 50% of expected cycle life",
        examples=[60.0],
    )


class VoltageLevels(CamelCaseModel):
    nominal_voltage: float = Field(
        ...,
        title="Nominal Voltage",
        description="The average voltage the battery output when fully charged",
        examples=[550.0],
    )
    maximum_voltage: float = Field(
        ...,
        title="Maximum Voltage",
        description="The largest level the battery voltage can reach",
        examples=[620.0],
    )
    minimum_voltage: float = Field(
        ...,
        title="Minimum Voltage",
        description="The lowest level the battery voltage can reach",
        examples=[180.0],
    )


class TemperatureRange(CamelCaseModel):
    minimum_temperature: float = Field(
        ...,
        title="Minimum Temperature",
        description="The minimum temperature the battery can withstand",
        examples=[-40.0],
        le=100,
        ge=-100,
    )
    maximum_temperature: float = Field(
        ...,
        title="Maximum Temperature",
        description="The maximum temperature the battery can withstand",
        examples=[50.0],
        le=100,
        ge=-100,
    )


class ExpectedLifetime(CamelCaseModel):
    cycle_life: int = Field(
        ...,
        title="Cycle Life",
        description="Minimum number of cycles the battery can be recharged to at least 80% of initial capacity",
        examples=[5000],
    )
    reference_test: str = Field(
        ...,
        title="Reference Test",
        max_length=250,
        description="The details of the reference test used for defining the expected lifetime",
        examples=["Accelerated cycle life testing"],
    )
    cycle_rate: str = Field(
        ...,
        title="Cycle Rate",
        description="The C-rate used in the cycle life test",
        examples=["1C"],
    )


class MaterialComposition(CamelCaseModel):
    chemistry: List[str] = Field(
        ...,
        title="Chemistry",
        description="The chemical composition of the battery",
        examples=[["Sodium", "Cobalt"]],
    )
    hazardous_substances: List[str] = Field(
        ...,
        title="Hazardous Substances",
        description="The hazardous substances present in the battery",
        examples=[["Sulphuric acid"]],
    )
    critical_raw_materials: List[str] = Field(
        ...,
        title="Critical Raw Materials",
        description="The critical raw materials present in the battery in a concentration of more than 0.1% weight by weight",
        examples=[["Cobalt"]],
    )


class RecycledContent(CamelCaseModel):
    substance_name: str = Field(
        ...,
        title="Substance Name",
        max_length=40,
        description="The name of the substance that has recycled content",
        examples=["Cobalt"],
    )
    recycling_rate: float = Field(
        ...,
        title="Recycling Rate",
        description="The amount of recycled content in the substance",
        examples=[8.5],
    )


class ExtinguishingAgent(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=250,
        description="The registered trade name of the extinguishing agent",
        examples=["Extinguishing company"],
    )
    website: Optional[str] = Field(
        None,
        title="Website",
        description="The website of the battery manufacturer",
        examples=["https://www.extcompany.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer",
        examples=["info@fzsonick.com"],
    )


class LegalConformity(CamelCaseModel):
    battery_act_compliance: bool = Field(
        ...,
        title="Battery Act Compliance",
        description="The indicator if the battery complies with the requirements of the battery act or not",
        examples=[True],
    )
    requirement_conformity: List[str] = Field(
        ...,
        title="Requirement Conformity",
        description="The compliancy of the battery with other legal and standard requirements",
        examples=[["ROHS", "CE HSE", "IEC62619"]],
    )
    conformity_declaration: str = Field(
        ...,
        title="Conformity Declaration",
        description="The link to the EU declaration of conformity documentation",
        examples=["https://company/EUdeclaration/z37-310-76"],
    )


class ManufacturingDataSheetResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        title="Product Name",
        description="The official sales name of the product",
        examples=["Salt battery"],
    )
    battery_model: str = Field(
        ...,
        title="Battery Model",
        max_length=40,
        description="The model of the battery",
        examples=["Z37-310-76"],
    )
    battery_category: BatteryCategory = Field(
        ...,
        title="Battery Category",
        description="The category of the battery based on its intended use",
        examples=[BatteryCategory.INDUSTRIAL_BATTERY],
    )
    manufacturer_information: ManufacturerInformation = Field(
        ...,
        title="Manufacturer Information",
        description="The details of the battery manufacturer",
    )
    manufacturing_location: ManufacturerLocation = Field(
        ...,
        title="Manufacturing Location",
        description="The details of the location battery manufacturing plant",
    )
    manufacturing_date: str = Field(
        ...,
        title="Manufacturing Date",
        description="The date of manufacture using month and year",
        patterns=[r"^\d{4}-\d{2}$"],
        examples=["2023-07"],
    )
    weight: float = Field(
        ...,
        title="Weight",
        description="The total net weight of the product in kilograms (kg)",
        examples=[450.0],
    )
    capacity: float = Field(
        ...,
        title="Capacity",
        description="The total number of ampere-hours (Ah) that can be withdrawn from a fully charged battery",
        examples=[100.0],
    )
    power: float = Field(
        ...,
        title="Power",
        description="The original power capability of the battery in Watts",
        examples=[25000.0],
    )
    cell_type: CellType = Field(
        ...,
        title="Cell Type",
        description="The type of cells used in the battery pack",
        examples=[CellType.SODIUM_ION],
    )
    resistance: float = Field(
        ...,
        title="Resistance",
        description="The internal resistance of teh battery pack",
        examples=[0],
    )
    round_trip_efficiency: RoundTripEfficiency = Field(
        ...,
        title="Round Trip Efficiency",
        description="The details of the round trip energy efficiency in energy storages",
    )
    voltage_levels: VoltageLevels = Field(
        ...,
        title="Voltage Levels",
        description="The details of the voltage levels of the battery",
    )
    temperature_range: TemperatureRange = Field(
        ...,
        title="Temperature Range",
        description="The details of the acceptable temperature values of the battery",
    )
    expected_lifetime: ExpectedLifetime = Field(
        ...,
        title="Expected Lifetime",
        description="The details of the battery lifetime",
    )
    material_composition: MaterialComposition = Field(
        ...,
        title="Material Composition",
        description="The details of the material composition of the battery",
    )
    recycled_content: List[RecycledContent] = Field(
        ...,
        title="Recycled Content",
        description="The recycled content information present in the battery",
    )
    renewable_content: List[RecycledContent] = Field(
        ...,
        title="Renewable Content",
        description="The renewable content information present in the battery",
    )
    extinguishing_agent: ExtinguishingAgent = Field(
        ...,
        title="Extinguishing Agent",
        description="The details of an agent that can extinguish the battery",
    )
    legal_conformity: LegalConformity = Field(
        ...,
        title="Legal Conformity",
        description="The details of the conformity of the battery with the legal and harmonized standards",
    )
    warranty: str = Field(
        ...,
        title="Warranty",
        description="The date when the battery warranty expires",
        patterns=[r"^\d{4}-\d{2}$"],
        examples=["2028-07"],
    )


class ManufacturingDataSheetRequest(CamelCaseModel):
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
    title="Manufacturing Data Sheet",
    description="Manufacturing data sheet as required by Battery Passport specification of the European Commission's Battery Act (2023/1542)",
    request=ManufacturingDataSheetRequest,
    response=ManufacturingDataSheetResponse,
)
