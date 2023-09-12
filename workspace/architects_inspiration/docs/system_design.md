## Implementation approach
The website will be built using the Django framework due to its robustness and scalability. Django has a user-friendly admin interface which can be used for managing the content of the website. For the front-end, we will use Bootstrap to achieve a responsive and user-friendly interface similar to Pinterest. 

To incorporate AIGC-generated images, we will use an open-source AI image generation library such as DeepArt or DeepDream. These images will be stored in a PostgreSQL database due to its excellent performance with large datasets. 

For user interactions such as saving images, commenting, and liking posts, we will use Django's built-in authentication and authorization modules. 

The search functionality will be implemented using Elasticsearch, an open-source search engine that provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

## Python package name
```python
"architects_inspiration"
```

## File list
```python
[
    "main.py",
    "settings.py",
    "urls.py",
    "models.py",
    "views.py",
    "forms.py",
    "templates/home.html",
    "templates/board.html",
    "templates/search.html",
    "templates/upload.html",
    "static/css/main.css",
    "static/js/main.js",
    "requirements.txt"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class User{
        +str username
        +str password
        +str email
        +list[Image] saved_images
        +list[Image] uploaded_images
        +list[Comment] comments
        +list[Like] likes
        +__init__(username: str, password: str, email: str)
        +save_image(image: Image)
        +upload_image(image: Image)
        +comment_on_image(image: Image, comment: str)
        +like_image(image: Image)
    }
    class Image{
        +str url
        +str title
        +str description
        +User uploader
        +list[Comment] comments
        +list[Like] likes
        +__init__(url: str, title: str, description: str, uploader: User)
        +add_comment(comment: Comment)
        +add_like(like: Like)
    }
    class Comment{
        +User author
        +str text
        +Image image
        +__init__(author: User, text: str, image: Image)
    }
    class Like{
        +User user
        +Image image
        +__init__(user: User, image: Image)
    }
    User "1" -- "*" Image: saves, uploads
    User "1" -- "*" Comment: writes
    User "1" -- "*" Like: makes
    Image "1" -- "*" Comment: has
    Image "1" -- "*" Like: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant U as User
    participant I as Image
    participant C as Comment
    participant L as Like
    U->>I: save_image(image)
    U->>I: upload_image(image)
    U->>C: comment_on_image(image, comment)
    U->>L: like_image(image)
    I->>C: add_comment(comment)
    I->>L: add_like(like)
```

## Anything UNCLEAR
The requirement is clear to me.