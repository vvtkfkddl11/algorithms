-- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('김치', '과자', '국', '식용유')
AND (CATEGORY, PRICE) IN (
    SELECT CATEGORY, MAX(PRICE)
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
)
ORDER BY MAX_PRICE DESC