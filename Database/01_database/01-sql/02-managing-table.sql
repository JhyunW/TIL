CREATE TABLE examples(
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
  );

PRAGMA table_info('examples');

ALTER TABLE
  examples
ADD COLUMN
  country VARCHAR(100) NOT NULL
DEFAULT
  '부산';

ALTER TABLE
  exaples
ADD COLUMN
  Age INTEGER NOT NULL;

ALTER TABLE
  examples
ADD COLUMN
  address VARCHAR(100) NOT NULL;




-- 컬럼 명 수정
-- Address -> PostCode
ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;


-- 컬럼 삭제
-- DROP COLUMN
ALTER TABLE
  examples
DROP COLUMN
  PostCode;


ALTER TABLE
  examples
RENAME  TO
  new_examples;

ALTER TABLE
  new_examples
RENAME TO
  examples;

DROP TABLE examples;

DROP TABLE examples;