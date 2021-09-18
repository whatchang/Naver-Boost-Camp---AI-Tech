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

* 주제 : LSTM은 완벽하게 gradient vanishing/exploding 문제를 해결하였는가?

    * 간단한 LSTM 소개

    * gradient vanishing을 해결하였는가?

    * gradient exploding을 해결하였는가?

    * 결론

    * TMI : vanilla LSTM에서는 forget gate없었고 대신 CEC(Constant Error Carousel, 이것 덕분에 vainshing/exploding을 완화시킬 수 있었다.)라는 고정 weight가 1인 순환 연결 구조를 사용하였고 추후 forget gate가 추가되면서 CEC를 forget gate로 reset할 수 있게 되면서 LSTM이 long term dependency 문제를 완화시킬 수 있게 되었다[7].

    * 참고한 사이트 및 논문  
        * 간단한 LSTM 소개
        &nbsp; [1] &nbsp; 
        &nbsp; [2] &nbsp; <br>
        * gradient vanishing을 해결하였는가?
        &nbsp; [3] &nbsp; <br>
        * gradient exploding을 해결하였는가?
        &nbsp; [4] &nbsp; <br>
        * 결론
        &nbsp; [5] &nbsp; <br>
        &nbsp; [6] &nbsp; <br>
        * TMI 
        &nbsp; [7] &nbsp; 'What is a Constant Error Carousel?', https://deepai.org/machine-learning-glossary-and-terms/constant%20error%20carousel<br>

* 실습 코드 .py파일로 바꿔서 모듈화 하기 - [템플릿은 이것 이용](https://github.com/victoresque/pytorch-template)


2. [피어세션 정리](#2-피어세션-정리)

3. [학습 회고](#3-학습-회고)

## 1. 공부한 내용 정리


<br>


## 2. 피어세션 정리
- 연휴 간 각자의 계획 공유

```
- 연휴 간 목표
  - 모두들 밀린 시각화 강의 따라잡기..!!
  - 제우님: 부스트코스 확률 강의 수강 목표
  - 동규님: GNMT, Conv Seq2Seq, BERT
  - 명훈님: 토요일은 풀잠, RoFormer (RPE), Hi-Transformer
  - 우창님: 실습 코드 모듈화 + hugging face 사용해보기(멘토님 추천해주신 사이트)
  - 대웅님: Transformer 자체에 대한 이후의 논문들에 대한 공부, 멘토님 추천해주신 자료 보면서 공부, KLUE RE 태스크 베이스라인 뜯어보며 공부!
  - 전진님: 추천 논문 복습, huggingface 튜토리얼, 부스트코스 NLP 강의 보기
  - 준영님: 국립국어원 대회 베이스라인 만들어서 제출해보기, 트랜스포머 구현해보기 (멘토님 추천 유튜브).
```

- 준영님 질문: 이번 연휴 기간 동안에 트랜스포머를 직접 구현해보는 것이 좋은 선택일까요?
    - 대웅님: 처음부터 하기에 부담스러울 수 있는데 멘토님이 공유해주신 유튜브 자료에서 굉장히 잘 설명해주고 있어서 그 자료로 공부하는 것도 충분히 많은 도움이 될 것 같다.
    - 유경 멘토님 추가 답변: from scratch 로 구현하는 것도 물론 좋지만 너무 스트래치말고 스트레스일 수 있다. 유튜브에서 설명을 잘 해주고 있으니 그 부분들만 열심히 보고 넘어가도 좋다고 생각한다.
    - 제우님 추가 공유: 이전 캠퍼님이 만들어주셨던 트랜스포머 구현 빈칸완성 문제.

        [transformer_implementation_for_potato/[선택 과제 -1] Transformer.ipynb at main · ddobokki/transformer_implementation_for_potato](https://github.com/ddobokki/transformer_implementation_for_potato/blob/main/%5B%EC%84%A0%ED%83%9D%20%EA%B3%BC%EC%A0%9C%20-1%5D%20Transformer.ipynb)

- 대웅님: 서브워드 토크나이저에 대해서 전에 정리해놨던 자료가 있는데 이번 연휴 기간 다시 한번 정리를 해보면 좋을것 같다. (자료 공유해주심 ㅠㅠ)

    [토크나이징](https://www.notion.so/8548e2a5db9445f0872d216b4d435346) 

- 동규님: 전에 이야기가 나왔었던 파이썬의 벡터 연산과 메모리 단편화 문제에 대한 내용을 간단히만 공유.

    [Chapter 6. 행렬과 벡터 계산](https://www.notion.so/Chapter-6-1dd0678777fd414383a88097358274d2) 

- 명훈님 꿀팀  (P stage 에서 간편하게 쓸 수 있는 두줄의 강력한 코드!)

    ```python
    from datasets import load_dataset 
    re = load_dataset("klue", "re")
    ```

<br>

## 3. 학습 회고

#### 오늘도 목표로 세운 것들을 다 끝내지 못했다 하하하하하..... ㅠㅠ
<br>

#### level2 팀원들,멘토님과는 오늘이 마지막 피어세션 및 멘토링시간이었다. 2주라는 시간이 매우 빠르게 흘러갔던 것 같다. 뭔가... 많은게 들어왔고 정신을 차리니 2주가 흘러간 느낌?
<br>

#### 이번 level2 팀원들은 모두 열정적이고 토론 및 질문 등을 공유하는 하고 이야기하는 것을 좋아해서 항상 피어세션 시간이 2시간이상이었다. 팀 전반적으로 엶심히 하는 분위기라서 매 피어세션이 재미있고 흥미로웠다. 그래서 2주라는 시간이 너무 짧고 아쉬었지만 ㅠㅠㅠㅠㅠㅠ 어쩔 수 없이 이제는 헤어져야 할 시간인 것 같다.
<br>

#### 멘토님도 너무 좋은 분이셨고 우리에게 많은 것을 알려주시고 분위기 메이킹도 해주셔서 너무 감사했다. 또 개인적으로 질문한 내용에 대해서 잘 읽어주시고 답변해주셔서 감동이었고 감사했다. 덕분에 지금은 정신차리고 내 현재 수준에서 좀 더 성장할 수 있는 것과 나에게 중요한 기초/기본 공부에 더 집중하려고 한다. 그래서 이번 연휴때 NLP 실습 코드를 모듈화 시켜서 pytorch-project-templete을 이용하여 KLUE나 MRC 경진 대회 대비 + 이론에서 배운 내용을 코드화 하므로써 기초를 좀 더 다져볼 생각이다.
<br>

#### 비록 짧은 기간이었지만 다들 좋은 사람들이었고 좋은 시간을 보내서 정말 좋았고 이제 남은 기간동안 level3 팀원들과 새로운 멘토님과 으쌰으쌰 해야겠다.