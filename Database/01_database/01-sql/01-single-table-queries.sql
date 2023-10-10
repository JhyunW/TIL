-- 01. Querying data
SELECT
 LastName 
FROM 
 employees;

SELECT
 LastName, FirstName
FROM
 employees;

SELECT
 *
FROM
employees;

SELECT
 FirstName AS '이름'
FROM
 employees;

SELECT
 Name,Milliseconds / 60000 AS '재생시간(분)'
FROM
tracks;

-- 02. Sorting data
SELECT
 FirstName
FROM
 employees
ORDER BY
 FirstName ASC;


 SELECT
 FirstName
FROM
 employees
ORDER BY
 FirstName DESC;


SELECT
  Country, City
FROM
  customers
ORDER BY -- 컨트리가 먼저 정렬
  Country DESC,  -- 그리고 그 정렬안에서 다시정렬
  City ASC;


SELECT
  Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data
SELECT DISTINCT  -- DISTINCT 로 중복 제거
  Country
FROM
 customers
ORDER BY
  Country;


SELECT -- DISTINCT 로 중복 제거
  LastName, FirstName, City
FROM
 customers
WHERE
  City = 'Prague';


SELECT -- DISTINCT 로 중복 제거
  LastName, FirstName, City
FROM
 customers
WHERE
  City != 'Prague';


SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';


SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';


SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- 100000 <= Bytes <= 500000;
  Bytes BETWEEN 100000 AND 500000;


SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
Bytes;


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
-- Country = 'Canada'
-- OR Country = 'Germany'
-- OR Country = 'France';


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE  -- % 는 앞에 몇개의 문자가 있던 상관이 없음
  LastName LIKE '%son';


SELECT
  LastName, FirstName
FROM
  customers
WHERE  -- 단일 문자와 일치하는지
  FirstName LIKE '___a';


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4; -- 3개를 상쇄시키고 최종 4개


-- 04. Grouping data
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;


SELECT
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;


SELECT
Composer,
AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
 avgOfminute < 10;


-- 에러


-- 에러 해결
