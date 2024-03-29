-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, (P.PRICE * SUM(OFF.SALES_AMOUNT)) AS SALES
FROM PRODUCT AS P JOIN OFFLINE_SALE AS OFF
ON P.PRODUCT_ID = OFF.PRODUCT_ID 
GROUP BY P.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE ASC