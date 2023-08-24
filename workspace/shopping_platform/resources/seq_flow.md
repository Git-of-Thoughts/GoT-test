sequenceDiagram
    participant U as User
    participant P as Product
    participant O as Order
    participant R as Review
    U->>P: search_product(title)
    P-->>U: return_search_results()
    U->>P: view_product_details(product_id)
    P-->>U: return_product_details()
    U->>O: place_order(product_id, quantity)
    O-->>U: confirm_order()
    U->>R: write_review(product_id, comment, rating)
    R-->>U: confirm_review()
