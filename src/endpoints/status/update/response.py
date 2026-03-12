error_responses = {
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
        "content": {"application/json": {"example": {"detail": "Book not found. Check if the book exists."}}},
    },
    422: {
        "description": "Unprocessable Entity",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid book data: field required"}
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {"example": {"detail": "Error updating book in DB"}}
        },
    },
}