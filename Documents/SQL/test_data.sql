INSERT INTO languages
VALUES
    (default, 'C++', default, default),
    (default, 'Python', default, default);


INSERT INTO categories
VALUES
    (default, 'Data types', default, default),
    (default, 'OOP', default, default),
    (default, 'STL', default, default),
    (default, 'Operators', default, default);


INSERT INTO languages_categories
VALUES
    (1, 1),
    (1, 2),
    (1, 4),
    (2, 3),
    (2, 4);


INSERT INTO author
VALUES
    (1, 'Python deweloper', '{"some.com", "some_new.com", "facebook.com"}');