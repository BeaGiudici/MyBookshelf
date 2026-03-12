error_responses = {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"detail": "Book ID not found. Check if the book exists."}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "An unexpected error occurred"}}
        },
    },
}