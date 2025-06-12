-- 코드를 입력하세요
# USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요.

SELECT b.USER_ID, b.NICKNAME, CONCAT(b.CITY, ' ', b.STREET_ADDRESS1, ' ', b.STREET_ADDRESS2) AS 전체주소, CONCAT(SUBSTR(b.TLNO, 1, 3), '-', SUBSTR(b.TLNO, 4, 4), '-', SUBSTR(b.TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_BOARD AS a
JOIN USED_GOODS_USER AS b
ON a.WRITER_ID = b.USER_ID
GROUP BY a.WRITER_ID
HAVING count(*) >= 3
ORDER BY b.USER_ID DESC
