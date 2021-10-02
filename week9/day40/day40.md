<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 40

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 공부한 내용 정리

* 강의 듣기
    * 4~6강까기 들었다. <- 주말에 내용정리 할 예정

* 오피스 아워 
    * 오피스 아워를 통해서 text augmentation방법에 대해서 알게 되었고 또 이번 대회에서 성능을 올리기 위한 여러 접근법 또한 얻어가는 좋은 시간이 되었다.
        * text augmentation<br>
            &nbsp; 1. &nbsp; EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks<br>
            &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [논문 리뷰 블로그](https://catsirup.github.io/ai/2020/04/21/nlp_data_argumentation.html)<br>
            &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [논문 리뷰 유튜브](https://www.youtube.com/watch?v=UVtMqh3agQY&list=PLZKRQf7b07bSp_V-7DpK9AHpFGImiKKQb&index=17)<br>
            &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [한국어 EDA code](https://github.com/catSirup/KorEDA/tree/master)<br>
            <br>
            &nbsp; 2. &nbsp; Understanding Back-Translation at Scale<br>
            &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [논문 리뷰 유튜브](https://www.youtube.com/watch?v=UVtMqh3agQY&list=PLZKRQf7b07bSp_V-7DpK9AHpFGImiKKQb&index=17)<br>
        <br><br>
        * 접근법<br>
            &nbsp; 1. &nbsp; bert/roberta에 layer(linear or convolution) 또는 model을 추가해보자<br>
            &nbsp; 2. &nbsp; dataset의 entity(object, subject)등을 활용해보자<br>

* KLUE 대회 관련
    * 모델에 추가로 layer or model을 추가해볼 생각이다.
        * [참고용 코드 - 데이콘](https://dacon.io/competitions/official/235747/codeshare/3072)
    * 위의 참고용 코드에서 MLM pre-train 시키는 코드가 있어서 내 코드에 맞게 수정하여 사용하였다.
        * 학습은 내일정도 끝날 것 같아서 결과도 내일 나올것 같다. ->  micro_f1 : 67.468, auprc : 70.972

<br>

## 2. 과제 정리

없음

<br>

## 3. 피어세션 정리

* 참석자
    * 김신곤, 김재영, 박세진, 손희락, 심우창, 이상준, 전상민

* 강의 리뷰
    * 4장
    * 5장

* 대회 관련

* 현재
    * KLUE-RoBERTa-Large가 현재 최고 성능의 모델
        * epoch 10과 20 차이는 크지 않음... overfitting의 문제가 있는 것 같음
* 각자 역할 분담을 한다면?
    * hyperparameter_search로 parameter를 tuning
        * 각자 hyperparameter를 나누고 최고의 조합을 구하는 방법이 있음
    * model, optimizer 바꾸기
    * data 관련해서 아이디어를 생각해야할 것 같음
    * type을 data에 붙여서 비교하는 등
    * tokenizing부터도 다양하게 시도해볼 수 있음
    * 객체명 인식해서 tag 붙이기
    * class를 30가지로 나누는 대신 layer 또는 model 추가
    * loss 측정 방식 다양화 (근데 이거 좀 어려움)

* 오늘의 결정 사항!
    * 다음 주 일요일(10/3)까지는 자유롭게! 하고 싶은 거 하기!
        * seed는 42. loss도 고정...도 그냥 참고하삼
        * model도 자유임~^.^
    * base code는 본인 거 사용하거나 아님 희락님 거 사용하거나! 이건 자율!
        * 희락님이 batch size 45로 바꿔두셨다고 하니... 참고하삼
* 논문
    * RoBERTa

<br>

## 4. 학습 회고

* 강의를 4~6강까지 들었는데 남는게 없는것 같다 ㅠㅠ 
* 아마도 급하게 들은 것도 있고 지금 competition이라서 해당 내용과 관련이 없으면 개인적으로 관심도가 떨어져서 집중이 잘 안되고 자꾸 딴짓을 하려고 한다. .... 음... 반성해야 된다. 지금 제대로 안 들으면 나중에 또 시간내서 들어야 되는데... 
* 이미 시간을 흘러버렸으니까 다음 번에는 최대한 집중해서 강의를 들을려고 하고 주말에는 항상!!! 꼭!!! 해당 주차 내용을 복습하는 시간을 갖도록 하자!!!!
<br>

* 피어세션때 competition관련한 여러 이야기를 했고 결론적으로 다음주 월요일전까지는 각자 해보고 싶은 여러 시도를 하는 것으로 했다. 이 기간동안 나는 hugging face의 trainer를 사용하는 것이 아닌 customizing을 할 수 있는 방식으로 사용할 예정이다. 분명 어렵고 쉽지 않을 것 같은데 그래도 도전해보고 싶다 ㅎㅎ

<br>

* 마지막으로 요즘 competition을 참가하는 나의 태도가 공부/배움을 위한 competiton이 아닌 only 등수만 위한 competition인 것 같다. MLM pre-train 코드도 전반적인 이해를 한 후에 내 코드에 접목시키는 것이 아닌 내 코드에 해당 코드가 잘 돌아가게끔 하나씩 수정하면서 집어넣었다. 결국에는 오류는 안 나지만 가져온 코드에 대한 이해도 떨어지고 '공부를 위한 competion 참여'라는 나의 방향성과도 다르게 흘러가는 것 같다. 이미 1주일 가깝게 시간이 흘렀지만 지금부터라도 '공부를 위한 competition', 즉 빨리빨리 가져와서 적용하고 등수 올리는 것이 아닌 늦더라도 내가 가져온 코드에 대해서 남들에게 설명하고 내 스스로 그 코드를 작성할 수 있겠다-라는 자신감이 생길때까지 공부하고 그 후에 적용시켜야겠다.
* 결과적으로 위의 방식대로 대회를 참가하면 여러 실험을 못 할 것이라고 예상한다. 하지만 중요한 점은 이 competition은 팀 단위이기 때문에 다른 팀원들의 실험 결과를 보고 듣으면서 간접경험하는 것으로 만족하자!
* 대신 내가 한 실험(작업)에 대해서는 꼼꼼하게 실험하고 완벽하게 이해해서 팀원들에게 잘 공유하는 것을 목표로 삼자!!! 아자!아자! 화이팅~~~!!!!👍
* ＼＼\(۶•̀ᴗ•́)۶//／／

<br>