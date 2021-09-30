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

* 강의 내용은 3강까지 들었다.

* KLUE 대회 관련
    * 1번째 제출에서는 inference할 때 학습시킨 모델이 아닌 pre-trained만 된 모델을 가지고 사용했더니 점수가 처참했다. 사실 모델을 잘못 불러왔다는 것은 첫 제출후 4시간 뒤에 알게 되었다;;;
    * 어제 학습시킨 모델을 가지고 성능을 평가했는데 f1이 60정도 나왔다. 우리팀 best score랑 비교를 해보았을 submission.csv의 pred_label부분에서 가장 큰 차이점을 보였던 것이 class 0부분이었다. 팀 최고 점수 모델이 class 0을 선택했을때 나의 모델은 다른 것을 선택하는 하였고 그 부분에서 성능의 차이를 보인것 같다.
    * 3번제 제출에서는 original data를 사용였고 epoch을 2번째 제출보다 5를 더 추가해준 10으로 늘려주었다. 결과적으로 4%정도 성능이 올라갔다. 팀 최고 점수 모델이 epoch을 20정도 줬다고 해서 한 번 따라해볼려고 한다. 3번째 64%

<br>

## 2. 과제 정리

* 없음

<br>

## 3. 피어세션 정리

## 2021.09.28
### 참여자
김신곤, 김재영, 박세진, 손희락, 심우창, 이상준, 전상민

### 강의 review
https://drive.google.com/drive/folders/1MLI7SWBS-JM9_2zkSnySplb1YQt8fYaC  
[2장 정리](https://github.com/sangmandu/SangSangPlus/issues/84), 
[3장 정리](https://github.com/sangmandu/SangSangPlus/issues/83)

### Ground Rule
- 피어세션 이전의 질문 ) **공유 드라이브의 pdf와 git의 issue 양쪽에 질문 작성**하기
- 피어세션 진행 중의 질문 ) **zoom의 댓글로 기록**함으로써 모더레이터가 issue에 잘 정리할 수 있도록

- 질문 양식은 https://github.com/sangmandu/SangSangPlus/issues/85 참고

<br>

## 4. 학습 회고

* 오늘 피어세션에서 BERT에 대한 여러 질문들이 나왔고 어려웠지만 매우 재미있고 유익했다 ㅎㅎㅎㅎㅎ
* 덕분에 이전에 그냥 넘어갔던 부분에 대해서 잘 짚고 갈 수 있었던 것 같았고 해결하지 못한 부분은 좀 더 찾아보거나 내일 멘토링 시간때 해결할 수 있을 것 같다.
* 다들 BERT에 대해서 열정적으로 토론한 모습을 보니까 좋은 자극이 되었다!!!

* 요즘 학습 정리 및 회고를 하는데 게으러진 것 같은데.... 음....🤨 아무튼 화이팅~~~!😝
<br>