from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from enum import Enum

# class TipoDePlanilha():
#     channels
#     deliveries
#     drivers
#     hubs
#     orders
#     payments
#     stores
    
# class Vendas(BaseModel):
#     email: EmailStr
#     data: datetime
#     valor: PositiveFloat
#     produto: str
#     quantidade: PositiveInt
#     categoria: CategoriaEnum

#     @field_validator('categoria')
#     def categoria_deve_estar_no_enum(cls, error):
#         return error

class Channels(BaseModel):
    channel_id: PositiveInt
    channel_name: str
    channel_type: str

class Deliveries(BaseModel):
    delivery_id: PositiveInt
    delivery_order_id: PositiveInt
    driver_id: PositiveInt
    delivery_distance_meters: PositiveFloat
    delivery_status: str

class Drivers(BaseModel):
    driver_id: PositiveInt
    driver_modal: str
    driver_type: str

class Hubs(BaseModel):
    hub_id: PositiveInt
    hub_name: str
    hub_city: str
    hub_state: str
    hub_latitude: float
    hub_longitude: float

class Orders(BaseModel):
    order_id: PositiveInt
    store_id: PositiveInt
    channel_id: PositiveInt
    payment_order_id: PositiveInt
    delivery_order_id: PositiveInt
    order_status: str
    order_amount: PositiveInt
    order_delivery_fee: PositiveFloat 
    order_delivery_cost: PositiveFloat 
    order_created_hour: PositiveInt
    order_created_minute: PositiveInt
    order_created_day: PositiveInt 
    order_created_month: PositiveInt
    order_created_year: PositiveInt 
    order_moment_created: str
    order_moment_accepted: str
    order_moment_ready: str
    order_moment_collected: str
    order_moment_in_expedition: str
    order_moment_delivering: str
    order_moment_delivered: str
    order_moment_finished: str
    order_metric_collected_time: PositiveFloat 
    order_metric_paused_time: PositiveFloat
    order_metric_production_time: PositiveFloat
    order_metric_walking_time: PositiveFloat
    order_metric_expediton_speed_time: PositiveFloat
    order_metric_transit_time: PositiveFloat
    order_metric_cycle_time: PositiveFloat