CREATE INDEX article_category_id ON articles
USING BTREE (category);

CREATE INDEX article_title ON articles
USING BTREE (title);

CREATE INDEX article_content ON articles
USING GIST (content);
