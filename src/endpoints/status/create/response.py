error_responses = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {"example": {"detail": "Invalid status data"}}
        },
    },
    401: {
        "description": "Unauthorized",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid authentication credentials"}
            }
        },
    },
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"detail": "Status not found"}}},
    },
    422: {
        "description": "Unprocessable Entity",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid status data: field required"}
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "An unexpected error occurred"}}
        },
    },
}