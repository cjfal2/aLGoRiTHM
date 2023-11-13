-- 2022년 4월 13일 취소되지 않은
-- 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요.
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요.
-- 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.
WITH INFO AS (
    SELECT APNT_NO, PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
    FROM APPOINTMENT AS A
        INNER JOIN DOCTOR AS D
        ON D.DR_ID = A.MDDR_ID
    WHERE APNT_YMD LIKE "%04-13%" AND A.MCDP_CD = "CS" AND APNT_CNCL_YN = "N"
)

SELECT APNT_NO, PT_NAME, I.PT_NO, MCDP_CD, DR_NAME, APNT_YMD
FROM INFO AS I
    INNER JOIN PATIENT AS P
    ON I.PT_NO = P.PT_NO
ORDER BY APNT_YMD;