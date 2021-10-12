<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 공부한 내용 정리

* KLUE 대회 관련
    * 어제 돌려놓았던 모델이 성능이 별로 안 좋았다 ㅠㅠㅠㅠ
        * 모델 : klue/roberta-large
        * TAPT 적용
        * 5 - fold
        * early stopping 7 step
        * eval step : 100
        * loss function : cross entropy
        * learning rate : 5e5
        * 결과 : mirco_f1 70.214, auprc 75.677

<br>

## 2. 과제 정리

없음

<br>

## 3. 피어세션 정리

마지막까지 모델 돌리면서 회고? 비슷한 여러 이야기를 하였다.

<br>

## 4. 학습 회고

* 2주간의 KLUE 대회가 막을 내렸고 최종 등수는 12등이다. 3등정도가 더 올라서 기분이 매우 좋았다 ㅎㅎㅎㅎㅎ
* 아쉬웠던 점은 train dataset으로 적용했던 TAPT가 private 결과를 보니 성능 향상에 큰 기여를 하지 않았다는 것을 알게 되었고 public의 micro_f1 점수에 낚여 큰 기여를 했다고 착각해버렸다. 이 부분에서 시간을 아꼈으면 좋았을텐데.... ㅠㅠ 
* 아쉽기는 했지만 개인적인 성장부분에서는 큰 도움이 되었던 기간인 것 같다. 다음 MRC에서는 7등안에 들었으면 좋겠고 그때도 많은 것을 배울 것이다~!!! 화이팅~~~!!!😆

<br>