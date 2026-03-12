error_responses = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {"example": {"detail": "Invalid status data"}}
        },
    },
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"detail": "Status not found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "An unexpected error occurred"}}
        },
    },
}