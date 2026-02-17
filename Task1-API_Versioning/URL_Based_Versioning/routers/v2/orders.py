from fastapi import APIRouter

router = APIRouter()

# Get all orders (Version 2)
@router.get("/orders")
def get_orders():
    return {
        "version": "v2",
        "orders": [
            {
                "order_id": 101,
                "product": "Laptop",
                "quantity": 1,
                "price": 75000,
                "status": "shipped"
            },
            {
                "order_id": 102,
                "product": "Phone",
                "quantity": 2,
                "price": 30000,
                "status": "processing"
            }
        ]
    }


# Get single order (Version 2)
@router.get("/orders/{order_id}")
def get_order(order_id: int):
    return {
        "version": "v2",
        "order_id": order_id,
        "product": "Laptop",
        "quantity": 1,
        "price": 75000,
        "status": "delivered",
        "delivery_date": "2026-02-17"
    }


# Create order (Version 2)
@router.post("/orders")
def create_order():
    return {
        "version": "v2",
        "message": "Order created successfully",
        "order_id": 201,
        "status": "confirmed"
    }
