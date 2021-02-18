CREATE TABLE languages (
    language_id SMALLSERIAL                 NOT NULL,
    name VARCHAR(32)                        NOT NULL,
    creation_date TIMESTAMP WITH TIME ZONE  NOT NULL DEFAULT current_timestamp,
    last_update TIMESTAMP WITH TIME ZONE    NOT NULL DEFAULT current_timestamp,

    PRIMARY KEY (language_id)
);


CREATE TABLE categories (
    category_id SMALLSERIAL                 NOT NULL,
    name VARCHAR(56)                        NOT NULL,
    creation_date TIMESTAMP WITH TIME ZONE  NOT NULL DEFAULT current_timestamp,
    last_update TIMESTAMP WITH TIME ZONE    NOT NULL DEFAULT current_timestamp,

    PRIMARY KEY (category_id)
);


CREATE TABLE languages_categories (
    id SERIAL               NOT NULL,
    language_id SMALLSERIAL NOT NULL,
    category_id SMALLSERIAL NOT NULL,

    FOREIGN KEY (language_id) REFERENCES languages (language_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories (category_id) ON DELETE RESTRICT ON UPDATE CASCADE
);


CREATE TABLE articles (
    article_id SERIAL                       NOT NULL,
    title VARCHAR(56)                       NOT NULL,
    image VARCHAR(32)                       DEFAULT NULL,
    content TSVECTOR                        DEFAULT NULL,
    code TEXT                               DEFAULT NULL,
    creation_date TIMESTAMP WITH TIME ZONE  NOT NULL DEFAULT current_timestamp,
    last_update TIMESTAMP WITH TIME ZONE    NOT NULL DEFAULT current_timestamp,
    category SMALLSERIAL                    NOT NULL,
    author SMALLSERIAL                      NOT NULL,

    PRIMARY KEY (article_id),
    FOREIGN KEY (category) REFERENCES languages_categories (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (author) REFERENCES author (author_id) ON DELETE RESTRICT 
);


CREATE TABLE author (
    author_id SMALLSERIAL       NOT NULL,
    description VARCHAR(132)    DEFAULT NULL,
    socials VARCHAR(132)[]      DEFAULT NULL,

    PRIMARY KEY (author_id),
    FOREIGN KEY (id) REFERENCES User (id)
);
