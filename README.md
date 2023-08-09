Assumptions:

1. The library management system will have basic functionalities such as adding a new book, issuing a book, returning a book, and searching for a book.
2. The system will be a console-based application.
3. The system will not have any user roles. Any user can perform any operation.
4. The system will not persist data. Once the application is closed, all data will be lost.
5. The system will not handle any concurrency issues. It is assumed that only one user will use the system at a time.
6. The system will not handle any exceptions. It is assumed that the user will always provide valid input.

Core classes, functions, and methods:

1. `Book`: This class will represent a book in the library. It will have fields such as `id`, `title`, `author`, and `isIssued`.
2. `Library`: This class will represent the library. It will have a list of books and methods to add a book, issue a book, return a book, and search for a book.
3. `Main`: This class will be the entry point of the application. It will have the `main` method which will interact with the user and perform operations based on the user's input.

Now, let's write the code for each class.

book.java
