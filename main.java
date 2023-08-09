import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add book");
            System.out.println("2. Issue book");
            System.out.println("3. Return book");
            System.out.println("4. Search book");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter book id: ");
                    int id = scanner.nextInt();
                    System.out.print("Enter book title: ");
                    String title = scanner.next();
                    System.out.print("Enter book author: ");
                    String author = scanner.next();
                    library.addBook(new Book(id, title, author));
                    break;
                case 2:
                    System.out.print("Enter book id: ");
                    id = scanner.nextInt();
                    Book issuedBook = library.issueBook(id);
                    if (issuedBook != null) {
                        System.out.println("Book issued: " + issuedBook.getTitle());
                    } else {
                        System.out.println("Book not available");
                    }
                    break;
                case 3:
                    System.out.print("Enter book id: ");
                    id = scanner.nextInt();
                    library.returnBook(id);
                    break;
                case 4:
                    System.out.print("Enter book id: ");
                    id = scanner.nextInt();
                    Book searchedBook = library.searchBook(id);
                    if (searchedBook != null) {
                        System.out.println("Book found: " + searchedBook.getTitle());
                    } else {
                        System.out.println("Book not found");
                    }
                    break;
                case 5:
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
