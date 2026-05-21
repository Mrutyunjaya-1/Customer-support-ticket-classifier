from pydantic import BaseModel, Field


class TicketClassification(BaseModel):
    category: str = Field(description="Category of the ticket")

    priority: str = Field(description="Priority level")

    routing_queue: str = Field(description="Support team queue")

    response_draft: str = Field(description="Draft response for the customer")