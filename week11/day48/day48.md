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

* 강의 듣기 4~5강

<br>

## 2. 과제 정리

없음

<br>

## 3. 피어세션 정리
# 참석자
김신곤, 김재영, 박세진, 손희락, 심우창, 이상준, 전상민

# 피어세션 내용

> 강의 질문 3 ~ 4강

우창 : 실습 코드에서 '평가하기' 부분의 outputs = model.generate(input_ids)는 단어 및 문장을 생성해서 ids형태로 반환을 해준다고 교수님께서 설명을 해줬습니다.  
그러면 만약 vocabulary에 없는 단어/문자는 생성할 수 없는 건가요?ex) vocabulary에 '갑'이라는 token이 없다면 해당 모델은 '갑오징어'라는 단어를 만들어 내지 못하는 건가요?  
(이때 vocabulary에는 '갑오징어'에 대한 subword가 없고 '갑오징어'가 subword가 되는 경우도 없다고 가정하겠습니다.)  

답변 : vocab 에 들어있지 않은 경우에 특별히 추가하지 않는 이상 생성하지 못할 것 같음

상준 : 2. seq_length 내 각 위치마다 들어가야할 단어를 하나씩 선택 
Decoder 에서 문장을 생성할 때 단어를 하나씩 선택이라는 말이 위치에 들어가야할 단어를 선택이라는 말인지?  
한번에 다 뽑아내고 순서를 정렬한다는 느낌이라서 알고있는 방법과 다르게 또 다른 방법인가? 해서 물어봤음


답변 : 학습단에는 Teachere Forcing 방법으로 넣는 방법으로 진행

상준 : TF-IDF 에서 나오는 vector 의 차원이 문서에서 나오는 모든 단어의 개수가 되는건가요?

답변 : n-gram 이라고 하면 n-gram 까지 포함한 BoW 의 개수가 차원이 됨

상준 : 여기에서 음식에 대한 TF-IDF 가 11차원인데 그런데 질문은 토큰이 11개가 아닌데 어떻게 되나요?


답변 : 질문에서는 있고 TF-IDF 만들 때 모든 문서를 통해 만들어진 BoW 에서의 단어를 카운트하고 IDF 는 기존 문서로 만들어진 IDF 를 곱함

우창 : 의문점 : 강의 + 베이스라인 코드

기본적으로 dataset에서 query와 context가 주어진다(대회 dataset기준). open-domain question answering은 query의 대한 답변의 내용이 있는 context를 찾는데 database를 이용한다.  
여기서 드는 의문점  
개인적인 생각 : retrieved passage를 할 때 주어진 context와 database에 있는 내용의 TF-IDF를 통해서 context를 가져와야 된다고 생각함.  
강의와 코드를 봤을때는 dataset의 context는 고려하지 않고 database에서만 TF-IDF를 통해서 context를 가져오는 것 같았다.  
질문 정리 : query에 대해서 dataset의 context와 database 둘 다 고려해서 적합한 context를 가져와야 하지 않나요?  

답변 : 안하는 줄 알았지만 baseline 코드로 주어진 retrieval.py 191~208 line 코드를 보니 train 시에는 데이터를 사용한다.

> ELECTRA 논문 관련 

다음주 멘토링 시간에 

1. ELECTRA 만 볼 것인가
2. ELECTRA 를 보고 실험논문까지 같이 읽자
3. ELECTRA 를 한번 더 하지 말고 다른 논문을 읽자

투표결과 : ELECTRA 말고 MRC 관련 논문을 읽자


> MRC git repository 에 project 에 MRC 칸반보드를 만들었음


project 관리를 이렇게 하자!

하이퍼파라미터 통일 필요!

> description 폴더를 하나 만들자

나중에 포트폴리오나 대회 자료를 정리하기 용이하게!

동일한 세팅에서 어떤 실험을 진행했고 그 결과가 이렇게 나왔다. validation score 가 이렇게 나왔다.

무엇을 바꿨고 score 가 이랬고 LB 는 이랬다. 

실험이 끝난 후 성과가 있는 경우 pull requests 로 뭘 했는지 공유하고 main 에 합치기

commit message 를 잘 작성해주시면 PR 을 작성하는데 도움이 될 수 있음

> project 의 칸반보드를 사용하면 issue 나 pr 을 끌어와서 같이 볼 수 있음


<br>

## 4. 학습 회고

<br>