# Day 15 이미지 분류 1~2 강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [Competition](#2-Competition)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* 이미지 분류 1~2강
    * 1강 : Competition with AI Stages!
        * P_Stage 목적<br>
        &nbsp; - &nbsp; U_Staage에서 배운 이론을 토대로 대회형식으로 실습하는 과정이다. 즉, 경진대회를 통해서 배운 이론을 직접 코드로 작성하여 익히는 과정이다. <br>
        <br>

        * Overview에 주목하자!<br>
        &nbsp; - &nbsp; 해결해야 하는 문제가 무엇인지 확인하자. <- 어느 분야의 문제인지, 어떤 부분이 해결해야 되는 문제인지 등<br>
        &nbsp; - &nbsp; overview를 통해서 대회를 개최한 배경에 대해서 알게 되면 학습 및 데이터를 활용할때 도움이 된다.<br><br>
        &nbsp; - &nbsp; 문제 정의하기!<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 내가 지금 풀어야 할 문제가 무엇인지? <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 이 문제의 input과 output은 무엇인가?<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 이 솔루션은 어디서 어떻게 사용되는지는가?<br><br>
        &nbsp; - &nbsp; data description을 잘 읽자!<br><br>
        &nbsp; - &nbsp; 등수도 중요하지만 성장(배움)도 중요하다! 서로의 지식을 공유하자!<br>
        <br>

        * 내가 P_Stage에서 얻고자 하는 것 생각해보기 <br>
        &nbsp; - &nbsp; 등수가 목적이 아닌 __배움이 목적__ 인 것을 잊지 말자!!!!(매우 중요)<br>
        &nbsp; - &nbsp; 데이터 전처리부터 ~ 데이터 학습 및 평가까지 코드 스스로 작성 해보기<br>
        &nbsp; - &nbsp; 위에서 작성하는 각 부분마다 어떤점을 주의해야 하고 어떤 부분에서 내가 실수를 많이 하는지 파악하기<br>
        &nbsp; - &nbsp; pre_trained 모델도 사용해 보고 augmentation도 해보고 parameter tuning도 해보고 이것저것 해보면서 경험쌓기<br>

        * 이번 competition에서 내 스스로 주의할 점<br>
        &nbsp; - &nbsp; 남과 비교하지 않기 -> 차리리 잘하는 사람보고 '나도 저렇게 잘 하고 싶디.... 그러니까 기초부터 차근차근 쌓아서 지금보다 더 발전해야지'라는 생각으로 동기부여 받는 정도로만 생각하기, 결코 못난 내 자신 비하하지 않기!<br>
        &nbsp; - &nbsp; 피어세션때 다른 사람이 말하는 내용 중에 모르는 내용이나 competition 코드 어렵거나 해결이 잘 안되는 문제에 대해서 적극적으로 질문하기! -> 절대로 아는척 가만히 있지 않기! 모르는 건 꼭 질문! <br>
        &nbsp; - &nbsp; 다음 날 지장이 갈 만큼 무리하지 말기! -> 저번에 약속한 취침시간 꼭 지키기!<br>

        <br>

    * 2강 :  EDA(Explorary Data Analysis)
        * EDA란?<br>
        &nbsp; - &nbsp; 데이터를 이해하기 위한 노력<br> 
        <br>

        * 어떻게 해야 할까?<br>
        &nbsp; - &nbsp; EDA를 주어진 데이터에 대한 자신의 생각을 채워넣는 서술형 문제라고 생각하면 좋다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 자신만의 생각/방식으로 접근<br>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; EDA에 정답은 없다. -> 여러 방식으로 접근해보면서 자신의 방식을 만들자!<br>
        <br>

        <br>

        * 마스터님이 생각하는 EDA란<br>
        &nbsp; - &nbsp; 데이터를 분석하기 위한 모든 접근 방식<br>
        &nbsp; - &nbsp; 화련한 코드 거창한 생각등이 아닌 자신이 데이터를 보고 의문점이 듣는 거에 대해서 파헤치면서 데이터를 이해하는 것! -> 파헤치기 위한 도구가 코드일뿐 코드 말고 다른 방식을 사용해도 된다! 그러니 너무 겁먹지 말자!<br>
        

        <br>
    

### 2. Competition
<br>

####  ㅎㅎㅎㅎㅎㅎㅎ 이미지 분류 competition덕분에~~~ 아무것도 안하고 이것만 하다가~~~~ 하루가 지나갔다 ㅎㅎ;;;;

<br>

#### 그래도 다행인 점은 새롭게 lable.csv를 만들어서 커스텀 데이터셋, 데이터로더를 이용하여 학습시키는 것까지 구현을 했다. 다만, ... 정확도가 매우 안 좋다 ㅎㅎ; <- 이때 모델은 필수 과제에서 나왔더 CNN 모델 코드를 이용했다.

<br>

#### 아직 시간이 있으므로 여러 방식을 사용해서 성능도 올리고 공부도 해보자!

<br>

#### 오늘 최고 점수는 정확도 : 6.2857%, f1 점수 : 0.0238이다.


<br>
### 3. 피어세션 정리
<br>
20210823 피어세션
<br><br>
🔍[마스크 데이터 분류 대회]
<br><br>
마스크 데이터 분류 대회에 대하여 토의함
 
<br><br>
📒[데이터 전처리]
<br><br>
center crop, background masking, 등의 방법이 제안됨.
 
<br><br>

📎[DataLoader]

<br><br>

확장자 뿐 아니라 속성도 다양함. → glob 이용 시 편리함.<br>
데이터를 읽는 방법에 관하여 토의함: map-style, iterable-style
 <br><br>

📝[EDA]
<br><br>
각 속성(성별, 나이) 에 관련한 데이터 분포를 시각화 함.

 
<br><br>
🖐[모델 관련]<br><br>

주어진 input으로부터 label 유추를 어떻게 해내는지 궁금하다.<br>
레이블링의 방법: classification / regression<br>
→ 주어진 age 속성을 정형 데이터로 이용하는 방법에 관하여<br><br>

따라서 피어세션 진행 형식을 미리 정하면 계획적으로 시간을 활용할 수 있을 것<br>
end-to-end 학습 방법을 이용해도 되는지 토의해 봄.<br>
: 마스크 착용 여부, 나이, 성별의 독립적인 속성이 섞여 있기 때문.<br><br>

 

🍋[학습정리]<br><br>

배운 것, 시도한 것 등을 기입할 것.



<br><br>

### 4. 학습 회고

#### 보안에서 CTF와 비슷하게 이번 주부터 시작하는 경진대회는 매우 재미있고 집중이 잘 되어서 좋았다. 다만, 남과 나를 비교하지 말고 과거의 내 자신과 비교하고 스트레스를 최소화하는게 중요할 것 같다.

<br>

#### 그리고 부스트 캠프의 Copetition의 주 목적은 학습/배움 이므로 다음 날 공부에 피해가 갈 정도로 늦게까지 무리해서 하지 말자. 또 주 메인이 강의 내용 정리이고 그 후에 competition에 대해서 여러 시도를 해보자! 그리고 그때 그때 정리를 잘 해놓자!

<br>


