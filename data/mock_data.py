ORDERS = {

    "ORD1025": {
        "customer": "Rahul",
        "product": "Dell Inspiron Laptop",
        "category": "Laptop",
        "price": 65000,
        "order_date": "2026-09-28",
        "expected_delivery": "2026-10-05",
        "status": "shipped",
        "tracking_id": "TRK784521",
        "payment_method": "UPI"
    },

    "ORD3001": {
        "customer": "Rahul",
        "product": "Apple iPhone 17",
        "category": "Smartphone",
        "price": 79999,
        "order_date": "2026-10-01",
        "expected_delivery": "2026-10-04",
        "status": "delivered",
        "tracking_id": "TRK300112",
        "payment_method": "UPI",
        "delivery_date": "2026-10-04",
        "condition": "damaged"
    }
}


PRODUCTS = {

    "Dell Inspiron Laptop": {
        "category": "Laptop",
        "brand": "Dell",
        "price": 65000,
        "description": "15-inch productivity laptop"
    },

    "Apple iPhone 17": {
        "category": "Smartphone",
        "brand": "Apple",
        "price": 79999,
        "description": "Latest Apple smartphone"
    }
}


INVENTORY = {

    "Dell Inspiron Laptop": {
        "stock": 5
    },

    "Apple iPhone 17": {
        "stock": 3
    }
}


SHIPMENTS = {

    "TRK784521": {
        "status": "delayed",
        "location": "Hyderabad Distribution Center",
        "reason": "Package has not been assigned to a delivery executive",
        "new_estimated_delivery": "2026-10-07"
    },

    "TRK300112": {
        "status": "delivered",
        "location": "Customer Address",
        "reason": "Successfully delivered",
        "new_estimated_delivery": None
    }
}


RETURNS = {}

REFUNDS = {}