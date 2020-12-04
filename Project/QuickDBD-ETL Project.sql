-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/d1wKEG
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "author_info" (
    "author_no" INT   NOT NULL,
    "name" VARCHAR(30)   NOT NULL,
    "born" VARCHAR(300)   NOT NULL,
    "description" VARCHAR(500)   NOT NULL,
    CONSTRAINT "pk_author_info" PRIMARY KEY (
        "author_no"
     )
);

CREATE TABLE "quotes" (
    "quote_no" int   NOT NULL,
    "author_no" int   NOT NULL,
    "quote" VARCHAR(300)   NOT NULL,
    CONSTRAINT "pk_quotes" PRIMARY KEY (
        "quote_no","author_no"
     )
);

CREATE TABLE "tags" (
    "quote_no" int   NOT NULL,
    "tag" Varchar(300)   NOT NULL,
    CONSTRAINT "pk_tags" PRIMARY KEY (
        "quote_no"
     )
);

ALTER TABLE "quotes" ADD CONSTRAINT "fk_quotes_quote_no" FOREIGN KEY("quote_no")
REFERENCES "tags" ("quote_no");

ALTER TABLE "quotes" ADD CONSTRAINT "fk_quotes_author_no" FOREIGN KEY("author_no")
REFERENCES "author_info" ("author_no");

