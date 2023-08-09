package com.example.librarymanagementsystem.repositories;

import com.example.librarymanagementsystem.models.Book;
import org.springframework.data.repository.CrudRepository;

public interface BookRepository extends CrudRepository<Book, Long> {
}
