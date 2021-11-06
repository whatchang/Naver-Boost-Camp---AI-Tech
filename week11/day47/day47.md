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

* 강의 3강 듣기 완료 < - 추후 정리 할 예정

* Roberta 논문 읽기 

* 알고리즘 1문제

<br>

## 2. 과제 정리

없음

<br>

## 3. 피어세션 정리

## 참석자
김신곤, 김재영, 박세진, 손희락, 심우창, 이상준, 전상민

## 피어세션 내용

> 1. RoBERTa 논문 질문 & 답변

* cross-entropy가 MLM 과정에서 가장 적합한 손실함수일까요?? 아니면 가장 일반적인 함수여서 쓴 것일까요?
* 답변: 일반적이어서 쓴 것 같긴한데 멘토님에게 더 여쭤보면 좋을 것 같음

* we do not train with a reduced sequence length for the first 90% of updates. 이 부분 무슨 의미인가요?
* 답변: 재영: BERT 논문에서는 90%는 max length 를 줄이고 10%는 512 만큼 길이로 사용했는데 RoBERTa 에서는 길이를 줄이지 않고 무조건 512 로 고정
* ![image](https://user-images.githubusercontent.com/52475378/137085174-25c16645-bb8f-4a9a-9ebd-9150741af8e1.png)
* Transforemr 에서는 positional embedding 을 그냥 더하지만 BERT 에서는 학습을 하므로 128 로 했을 때는 129~512 의 positional embedding
을 학습이 안되었으므로 나머지 10%를 512 의 길이만큼 해서 BERT 에서는 나머지를 학습

* To avoid using the same mask for each training instance in every epoch, training data was duplicated 10 times so that each sequence is masked in 10 different ways over the 40 epochs of training. Thus, each training sequence was seen with the same mask four times during training. 이부분 이해가 잘 안되요
* 세진 : 마스킹 자체가 랜덤하게 되는 거라 열 번 문장을 복제(?)해도 다른 곳에 되어서~ 다른 문제가 될 것이다~ 라고 이해했어요
* 상민 : static 은 epoch 를 돌 때마다 마스크 위치가 똑같음 그런데 dynamic 은 epoch 마다 다르게 하기 위함임
쉽게 생각하면 학습할 때마다 매번 masking 위치를 바꿔야 하는데 dynamic 에서는 mask 위치를 다르게 한 10개의 데이터를 만들어서 학습했음
* 재영 : BERT original(reference) vs static vs Dynamic Masking 이 다 다름 그래서 original 은 a single-static 이고 static 은 10배로 늘려서 다른 masking 을 적용한 것이고 Dynamic 에서는 모델에 feed 할 때 masking 을 새로 해줌

* SENTENCE-PAIR+NSP 와 SEGMENT-PAIR 와의 차이
* 재영 : segment 는 BERT 에서 말하는 문장 여러개를 의미하고 sentence 는 진짜 문장1개를 의미한다고 봄
* 세진 : segment-pair는 segment를 한 덩이로 보고 sentence는 sentence를 한 덩이로 보고...!

* the median development set results 중앙값 개발 세트 결과? -> 5개 모델의 중앙값을 이야기 하는 것 맞나요?
* 상민 : development set 은 valid set 을 의미하는 것 같다 random seed 를 다르게해서 5개 모델을 학습하고 그 중에 중앙값을 선택하는 것 같음

* QNLI: Recent submissions on the GLUE leaderboard adopt a pairwise ranking formulation for the QNLI task, in which candidate answers are mined from the training set and compared to one another, and a single (question, candidate) pair is classified as positive pairwise ranking formulation 이란?
* 재영 : 어떤 context 가 있고 그 안에서 질문을 하는데 candidate 들이 있을거고 정답이 비슷하게 느껴지는게 여러개가 있을 거고 제일 그럴듯한 답을 하나 고르고 그래서 최종적으로 그 답이 맞는지 아닌지를 있다 없다를 판별하지 않을까?
* ![image](https://user-images.githubusercontent.com/52475378/137096261-c26a40e2-d64e-4b85-a614-64b712fbdc47.png)
* 우창 : QNLI 데이터는 이렇게 되어 있음
* qeustion 과 candidate 의 ranking 을 먼저 찾는다?

> 2. ELECTRA 논문 질문 & 답변

* Our approach also works well at large scale, where we train an ELECTRA-Large model that performs comparably to RoBERTa (Liu et al., 2019) and XLNet (Yang et al., 2019), KLUE 대회에서 RoBERTa보다 인기가 없었던 이유를 알 수 있을까요?
* 상민 : KoElectra 가 large 모델이 없었다. 그래서 사람들이 안찾아본게 아닐까?

* We found that without the weight initialization the discriminator would some-times fail to learn at all beyond the majority class, perhaps because the generator started so far ahead of the discriminator. 특히 "beyond the majority class" 이 부분이 이해가 안가네요
* 상민 : discriminator 와 generator 의 지식수준이 비슷해야한다고 받아들여짐 마치 5살 애기랑 20살 영재를 데려와서 경찰과 도둑을 하고있는 격 그러다보니 너무 차이가 많이나면 압도적으로 누군가 누를수밖에 없고 그런 의미에서 대부분의 class 를 학습하는데 실패했다고 하는게 아닌가 싶음
* 멘토님께 물어보겠음


<br>

## 4. 학습 회고

* 강의 3강 듣고 피어세션 전까지 RoBERTa 논문만 읽었다. 이해 안 되는 부분들이 있었는데 이 부분은 질문으로 남겨서 피어세션 때 해결하였다.

<br>