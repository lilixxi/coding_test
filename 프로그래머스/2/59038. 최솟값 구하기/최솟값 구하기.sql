-- 코드를 입력하세요
SELECT DATETIME 
FROM ANIMAL_INS
WHERE DATETIME = (
SELECT MIN(DATETIME)
FROM ANIMAL_INS
);