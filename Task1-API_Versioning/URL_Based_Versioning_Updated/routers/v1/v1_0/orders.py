from fastapi import APIRouter

router = APIRouter()

# Get all orders (Version 1)
@router.get("/orders")
def get_orders():
    return {
        "version": "v1.0",
        "orders": [
            {
                "order_id": 101,
                "product": "Laptop",
                "quantity": 1
            },
            {
                "order_id": 102,
                "product": "Phone",
                "quantity": 2
            }
        ]
    }


# Get single order by ID (Version 1)
@router.get("/orders/{order_id}")
def get_order(order_id: int):
    return {
        "version": "v1.0",
        "order_id": order_id,
        "product": "Laptop",
        "quantity": 1
    }


# Create order (Version 1)
@router.post("/orders")
def create_order():
    return {
        "version": "v1.0",
        "message": "Order created successfully"
    }
