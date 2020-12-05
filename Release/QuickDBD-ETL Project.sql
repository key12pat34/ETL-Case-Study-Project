-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/d1wKEG
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "author_info" (
    "_id" int   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "born" VARCHAR   NOT NULL,
    "description" VARCHAR   NOT NULL,
    CONSTRAINT "pk_author_info" PRIMARY KEY (
        "_id"
     )
);

CREATE TABLE "quotes" (
    "_id" int   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "text" VARCHAR   NOT NULL,
    CONSTRAINT "pk_quotes" PRIMARY KEY (
        "_id"
     )
);

CREATE TABLE "tags" (
    "_id" int   NOT NULL,
    "tags" Varchar(300)   NOT NULL,
    CONSTRAINT "pk_tags" PRIMARY KEY (
        "_id"
     )
);

ALTER TABLE "author_info" ADD CONSTRAINT "fk_author_info__id" FOREIGN KEY("_id")
REFERENCES "quotes" ("_id");

ALTER TABLE "tags" ADD CONSTRAINT "fk_tags__id" FOREIGN KEY("_id")
REFERENCES "quotes" ("_id");

