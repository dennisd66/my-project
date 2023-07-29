-- Database schema for concordance and text retrieval system
CREATE TABLE concordance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    document_id INTEGER,
    position INTEGER,
    FOREIGN KEY (document_id) REFERENCES documents (id)
);

CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
