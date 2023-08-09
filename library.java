import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<Book> books;

    public Library() {
        this.books = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public Book issueBook(int id) {
        for (Book book : books) {
            if (book.getId() == id && !book.isIssued()) {
                book.issue();
                return book;
            }
        }
        return null;
    }

    public void returnBook(int id) {
        for (Book book : books) {
            if (book.getId() == id && book.isIssued()) {
                book.returnBook();
            }
        }
    }

    public Book searchBook(int id) {
        for (Book book : books) {
            if (book.getId() == id) {
                return book;
            }
        }
        return null;
    }
}
