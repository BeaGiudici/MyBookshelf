error_responses = {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"detail": "Genre ID not found. Check if the genre exists."}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "An unexpected error occurred"}}
        },
    },
}