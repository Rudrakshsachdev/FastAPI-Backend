from pydantic import BaseModel, Field, Literal, AnyUrl ,field_validator, model_validator, computed_field
from typing import Annotated, List, Optional, Dict
from uuid import UUID

# Here, we are defining a schema for the products using pydantic
# This schema is used to validate the data that is sent to the API
class Products(BaseModel):
    id: UUID

    # here we are using Annotated to add metadata to the field
    # ... means that the field is required
    # description is used to describe the field
    # min_length and max_length are used to specify the minimum and maximum length of the field
    # example is used to specify the example of the field
    sku: Annotated[
        str,
        Field(
            ...,
            description="Product SKU",
            min_length=1,
            max_length=50,
            example="XIAO-359GB-001",
        )
    ]

    name: Annotated[
        str,
        Field(
            ...,
            title="Product Name",
            description="Product Name",
            min_length=1,
            max_length=50,
            example="Xiaomi Model Pro",
        )
    ]

    description:
    Annotated[
        str,
        Field(
            ...,
            title="Product Description",
            description="Product Description",
            min_length=1,
            max_length=50,
            example="Xiaomi Model Pro",
        )
    ]

    category: Annotated[
        str,
        Field(
            ...,
            title="Product Category",
            description="Product Category",
            min_length=1,
            max_length=50,
            example="Xiaomi Model Pro",
        )
    ]

    brand: Annotated[
        str,
        Field(
            ...,
            title="Product Brand",
            description="Product Brand",
            min_length=1,
            max_length=50,
            example="Xiaomi Model Pro",
        )
    ]

    price: Annotated[
        float,
        Field(
            ...,
            title="Product Price",
            description="Product Price",
            ge=0,
            example=100,
        )
    ]

    currency: Literal["INR"] = "INR"

    discount_percent: Annotated[
        float,
        Field(
            ...,
            title="Product Discount Percent",
            description="Product Discount Percent",
            ge=0,
            le=100,
            example=10,
        )
    ]

    stock: Annotated[
        int,
        Field(
            ...,
            title="Product Stock",
            description="Product Stock",
            ge=0,
            example=100,
        )
    ]

    is_active: Annotated[
        bool,
        Field(
            ...,
            title="Product Is Active",
            description="Product Is Active",
            example=True,
        )
    ]

    rating: Annotated[
        float,
        Field(
            ...,
            title="Product Rating",
            description="Product Rating",
            ge=0,
            le=5,
            example=4.5,
        )
    ]

    tags: Annotated[
        Optional[List[str]],
        Field(
            ...,
            title="Product Tags",
            description="Product Tags",
            example=["tag1", "tag2", "tag3"],
        )
    ]

    image_urls: Annotated[
        List[str],
        Field(
            ...,
            title="Product Image URLs",
            description="Product Image URLs",
            example=["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        )
    ]

    dimensions_cm: Annotated[
        Dict[str, float],
        Field(
            ...,
            title="Product Dimensions",
            description="Product Dimensions",
            example={"length": 10, "width": 10, "height": 10},
        )
    ]

    seller: Annotated[
        Dict[str, str],
        Field(
            ...,
            title="Product Seller",
            description="Product Seller",
            example={"seller_id": "1234567890", "name": "Seller Name"},
        )
    ]

    created_at: datetime

    # here we are using field_validator to validate the data that is sent to the API 
    @field_validator("sku", mode="after")
    @classmethod
    # here we are using field_validator to validate the data that is sent to the API and it is a class method which is taking cls and value as arguments
    # and it is returning the value if the validation is successful
    # and it is raising a ValueError if the validation is not successful
    def validate_sku(cls, value: str):
        if "-" not in value:
            raise ValueError("SKU must contain a hyphen")
        
        last = value.split("-")[-1]
        if not (len(last) == 3 and last.isdigit()):
            raise ValueError("Last part of SKU must be a 3-digit number")
        return value

    # here we are using model_validator to validate the data that is sent to the API and it is a class method which is taking cls and model as arguments
    # and it is returning the model if the validation is successful
    # and it is raising a ValueError if the validation is not successful
    @model_validator(mode="after")
    @classmethod
    def validate_business_rules(cls, model: "Product"):
        if model.stock == 0 and model.is_active is True:
            raise ValueError("Product cannot be active if stock is 0")
        

        if model.discount_percent > 0 and model.rating == 0:
            raise ValueError("Product cannot have discount if rating is 0")
        
        return model
    
    # here we are using computed_field to compute the final price of the product
    # and it is a property which is taking cls and model as arguments
    # and it is returning the final price if the computation is successful
    # and it is raising a ValueError if the computation is not successful
    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)
