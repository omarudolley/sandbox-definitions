# Data Product Definitions template

This repository contains a minimal set of resources that are necessary to get started with
defining your own Data Product Definitions.

# Repo structure

- [./src](./src) - Definition sources in python format
- [./DataProducts](./DataProducts) - Final Definitions as OpenAPI 3.0 specs
- [.github/workflows](.github/workflows) - Pre-configured CI workflows for validating and
  converting definitions from sources

# Getting started

Press `Use template` to create a new repo from this template.

Define your own data products as python files under `src/`. Technically, you can go
   ahead and create final specs under the `DataProducts` folder if it's easier for you.
   However, the recommended approach is using python sources and the automatic converter

You have 2 options to use the converter:
1) By running `pre-commit install` after cloning the repo. Then definitions will be converted automatically before each commit
2) By creating a PR to the `master` branch. CI workflow will run the automation and push updated/generated files if needed.


## Python sources

Each python file located in the `src` folder is treated as a Data Product definition.

For example, `src/AirQuality/Current.py` defines `AirQuality/Current` data product.

These files are then converted to OpenAPI 3.0 specs, which are final forms of definitions. To make the converter work correctly, each file must follow the same structure:

```python
from pydantic import Field

from converter import CamelCaseModel, DataProductDefinition


class Request(CamelCaseModel):
    ...


class Response(CamelCaseModel):
    ...


DEFINITION = DataProductDefinition(
    description="...",
    request=Request,
    response=Response,
    route_description="...",
    summary="...",
)

```

Considering `CamelCaseModel` is a subclass of `pydantic`'s `BaseModel`, it's better to understand how to use this library. Please read [pydantic](https://pydantic-docs.helpmanual.io/)'s documentation if you're not familiar with it yet.

### Example 
There's an example of Data Product Definition for current weather:

```python
from pydantic import Field

from converter import CamelCaseModel, DataProductDefinition


class CurrentWeatherMetricRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location",
        ge=-90.0,
        le=90.0,
        example=60.192059,
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location",
        ge=-180.0,
        le=180.0,
        example=24.945831,
    )


class CurrentWeatherMetricResponse(CamelCaseModel):
    humidity: float = Field(..., title="Current relative air humidity in %", example=72)
    pressure: float = Field(..., title="Current air pressure in hPa", example=1007)
    rain: bool = Field(
        ..., title="Rain status", description="If it's currently raining or not."
    )
    temp: float = Field(
        ..., title="Current temperature in Celsius", example=17.3, ge=-273.15
    )
    wind_speed: float = Field(..., title="Current wind speed in m/s", example=2.1, ge=0)
    wind_direction: float = Field(
        ...,
        title="Current wind direction in meteorological wind direction degrees",
        ge=0,
        le=360,
        example=220.0,
    )


DEFINITION = DataProductDefinition(
    description="Data Product for current weather with metric units",
    request=CurrentWeatherMetricRequest,
    response=CurrentWeatherMetricResponse,
    route_description="Current weather in metric units",
    summary="Current Weather (Metric)",
)
```
