from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from enum import Enum

class TipoDePlanilha(str, Enum):
    CHANNELS = "channels.csv"
    DELIVERIES = "deliveries.csv"
    DRIVERS = "drivers.csv"
    HUBS = "hubs.csv"
    ORDERS = "orders.csv"
    PAYMENTS = "payments.csv"
    STORES = "stores.csv"
    
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
    delivery_id: int
    delivery_order_id: int
    driver_id: int
    delivery_distance_meters: float
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
    order_id: int
    store_id: int
    channel_id: int
    payment_order_id: int
    delivery_order_id: int
    order_status: str
    order_amount: float
    order_delivery_fee: float
    order_delivery_cost: float
    order_created_hour: int
    order_created_minute: int
    order_created_day: int
    order_created_month: int
    order_created_year: int 
    order_moment_created: int
    order_moment_accepted: str
    order_moment_ready: str
    order_moment_collected: str
    order_moment_in_expedition: str
    order_moment_delivering: str
    order_moment_delivered: str
    order_moment_finished: str
    order_metric_collected_time: float 
    order_metric_paused_time: float
    order_metric_production_time: float
    order_metric_walking_time: float
    order_metric_expediton_speed_time: float
    order_metric_transit_time: float
    order_metric_cycle_time: float

class Payments(BaseModel):
    payment_id: int
    payment_order_id: int
    payment_amount: float
    payment_fee: float
    payment_method: str
    payment_status: str

class Stores(BaseModel):
    store_id: int
    hub_id: int
    store_name: str
    store_segment: str
    store_plan_price: float
    store_latitude: float
    store_longitude: float