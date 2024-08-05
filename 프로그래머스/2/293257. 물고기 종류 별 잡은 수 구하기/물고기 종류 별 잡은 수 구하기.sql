-- 물고기의 종류 별 물고기의 이름과 잡은 수를 출력하는 SQL문을 작성해주세요.
-- 결과는 잡은 수 기준으로 내림차순 정렬해주세요.
SELECT COUNT(*) AS FISH_COUNT, N.FISH_NAME
FROM FISH_INFO AS I
    INNER JOIN FISH_NAME_INFO AS N
    ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY N.FISH_NAME
ORDER BY COUNT(*) DESC