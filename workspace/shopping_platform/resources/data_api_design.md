classDiagram
    class User{
        +str username
        +str password
        +str email
        +str first_name
        +str last_name
        +bool is_active
        +bool is_staff
        +bool is_superuser
        +datetime date_joined
        +str get_full_name()
        +str get_short_name()
        +bool has_perm(perm, obj=None)
        +bool has_module_perms(package_name)
    }
    class Product{
        +str title
        +str description
        +float price
        +int stock
        +str image
        +User vendor
    }
    class Order{
        +User user
        +Product product
        +int quantity
        +datetime date_ordered
        +str status
    }
    class Review{
        +User user
        +Product product
        +str comment
        +int rating
    }
    User "1" -- "*" Order: places
    User "1" -- "*" Product: sells
    User "1" -- "*" Review: writes
    Product "1" -- "*" Order: contains
    Product "1" -- "*" Review: has
