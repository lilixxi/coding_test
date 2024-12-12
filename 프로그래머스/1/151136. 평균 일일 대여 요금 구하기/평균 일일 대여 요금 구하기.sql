-- 코드를 입력하세요
# select * from CAR_RENTAL_COMPANY_CAR
# where CAR_TYPE = 'SUV';

SELECT round(avg(DAILY_FEE)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV';
# group by CAR_TYPE
# having round(avg(DAILY_FEE),1) ;