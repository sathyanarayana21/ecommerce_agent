from crewai.tools import tool

from data.mock_data import SHIPMENTS


@tool("Get Shipment Details")
def get_shipment_details(tracking_id: str) -> str:
    """Retrieve shipment and delivery information using a tracking ID."""

    shipment = SHIPMENTS.get(tracking_id)

    if not shipment:
        return f"Tracking ID {tracking_id} was not found."

    return f"""
Tracking ID: {tracking_id}
Shipment Status: {shipment['status']}
Current Location: {shipment['location']}
Reason: {shipment['reason']}
New Estimated Delivery: {shipment['new_estimated_delivery']}
"""