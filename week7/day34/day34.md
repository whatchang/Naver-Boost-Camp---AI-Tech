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

2. [피어세션 정리](#2-피어세션-정리)

3. [학습 회고](#3-학습-회고)

## 1. 공부한 내용 정리

* 주제 : LSTM은 완벽하게 gradient vanishing/exploding 문제를 해결하였는가?
    * 이것을 조사하게 된 계기
        * 이제까지 배운 내용에서는 cell state에 대한 backpropagation을 다뤘고 cell state 덕분에 gradient vanishing/exploding이 완화되었다고 배웠다.
        * 그런데 내 생각에는 중요한 것은 hidden state의 backpropagation이라고 생각한다.
        * 다음은 LSTM에서 사용되는 구조인 여러 gate와 cell state, output(hidden state)를 구하는 식이다[1]. ht는 ouput(t)와 tanh(t번째 time step의 cell state)를 아마다를 곱한 값이다.
        <img src=./img/lstm0.png><br>
        * 만약 ht의 backpropagation을 생각해본다면 ht에 대한 o(t)의 미분값을 구하고 그쪽방향으로 역전파를 진행하고 ht에 대한 tanh(cell state(t))의 도함수를 구하고 해당 방향으로도 역전파가 진행되므로 cell state에서의 backpropagation만 생각했을때와 다를 수도 있다고 생각하였다.
        * 요약 : 중요한 것은 hidden state vector부터의 backpropagation이라고 생각하였고 이 부분부터의 역전파를 생각한다면 이전에 배운 내용과 차이가 있을 거라고 생각하여 조사하게 되었다.

    * 간단한 LSTM 소개
        * LSTM은 아래와 같이 forget gate, input gate, output gate, cell state가 있으며 이전 cell state와 input gate에서 나온 값을 더하여 새로운 cell state를 만듭니다[1].
        <img src=./img/lstm1.png>

    * gradient vanishing을 해결하였는가?
        * gradient vanishing 문제를 완전히 해결한 것은 아니지만 vanilla RNN에 비해서 완화시켰다.
        * 완화시킨 방식을 알기 전 상기시키면 좋은 개념 : 이전의 hidden state vector의 정보를 forget gate에서 input으로 사용한다. 또 Ct부분에서의 역전파를 생각한다면 forget gate값만 이용한다(Ct에 대해서 Ct-1의 도함수이므로).
        * 완화시키는 원리는 ht부분부터의 backpropagtaion때 output gate에 대한 부분이 gradient vanishing이 있더라도 cell state 부분에서 gradient가 남아 있으므로 전체 gradient는 사라지지 않게 된다.[2],
        * LSTM의 ht를 구할때 ⊙(아다마르 곱hadamard product, 행렬곱이 아닌 원소곱을 뜻함) 덕분에 곱셈이 누적되는 효과가 발생하지 않아서 기울기 소실 혹은 exploding이 발생하기 어렵다고 나옴(아마다르 곱은 원소별 곱이며 이는 LSTM에서 매번 새로운 게이트 값을 이용하여 원소곱을 하므로 곱셈의 효과가 누적되지 않아 기울기 소실이 일어나기 힘들다.).[3]

    * gradient exploding을 해결하였는가?
        * gradient vanishing과 같이 완벽하게 해결한 것은 아니다[1].
        * [4] Ottokar Tilk 사람이 작성한 글을 보면 LSTM에서 활성화함수의 도함수(derivative)가 1.0인 identity function이고 이때 유효한 순환 가중치는 forget gate이기 때문에 exploding현상이 발생하지 않는다고 한다(forget gate는 1보다 큰 값을 output할 수 없기 때문이다).
        * [5],[7] LSTM 원본 논문에서는 gradient exploding에 해결여부가 언급되어 있지는 않다. 그러므로 [4]를 통해서 어느 정도 완화 시켰다고 추측해볼 수 있을 것 같다. 만약 exploding이 발생한다면 ht = o(t) ◉ tanh(ct) 부분에서의 아마다르 곱의 누적때문에 발생하지 않을까 싶다(개인적인 추측).

    * 결론
        * cell state라는 constant error carousel구조 덕분에 gradient vanishing/exploding을 완화시킬 수 있었던 것 같다.
    
    * 배운 것
        * 이전에는 막연하게 cell state에서 더하기 연산을 하므로 이때 도함수가 forget gate값이므로 gradient vanishing/exploding이 해결되었다고 알았다. 그러나 이번 기회를 통해서 LSTM의 구조적인 부분으로 인해서 gradient vanishing을 완화시킬 수 있고([2], [3]) gradient exploding부분도 추측해볼 수 있었다([4],[5],[7]).

    * TMI
        * vanilla LSTM에서는 forget gate없었고 대신 CEC(Constant Error Carousel, 이것 덕분에 vainshing/exploding을 완화시킬 수 있었다.)라는 고정 weight가 1인 순환 연결 구조를 사용하였고 추후 forget gate가 추가되면서 CEC를 forget gate로 reset할 수 있게 되면서 LSTM이 long term dependency 문제를 완화시킬 수 있게 되었다[6].
        * backpropagtion에서 도함수 값이 1보다 크거나 작다고 해서 반드시 vanishing or exploding 현상이 나타나는 것은 아니다. 즉, 필요조선이지 충분조건은 아니라는 의미이다.[7]
        * gradient exploding 문제를 완벽하게 해결하기 위해서는 clipping방식을 사용해야 한다([1] 의 p.18~20과 [7]논문에 제시되어 있다.)

    * 참고한 사이트 및 논문  
        * 간단한 LSTM 소개<br>
        &nbsp; [1] &nbsp; https://web.stanford.edu/class/cs224n/slides/cs224n-2019-lecture07-fancy-rnn.pdf, p.22~26
        * gradient vanishing을 해결하였는가?<br>
        &nbsp; [2] &nbsp; https://stats.stackexchange.com/questions/185639/how-does-lstm-prevent-the-vanishing-gradient-problem<br>
        &nbsp; [3] &nbsp; Deep Learning from Scratch2 (한빛미디어), p.256
        * gradient exploding을 해결하였는가?<br>
        &nbsp; [4] &nbsp; https://www.quora.com/How-does-LSTM-help-prevent-the-vanishing-and-exploding-gradient-problem-in-a-recurrent-neural-network<br>
        &nbsp; [5] &nbsp; S.HochreiterandJ.Schmidhuber.Longshorttermmemory.Neuralcomputation,9(8):1735–1780,1997.
        * TMI <br>
        &nbsp; [6] &nbsp; 'What is a Constant Error Carousel?', https://deepai.org/machine-learning-glossary-and-terms/constant%20error%20carousel<br>
        &nbsp; [7] &nbsp; Pascanu, Razvan, Tomas Mikolov, and Yoshua Bengio. "On the difficulty of training recurrent neural networks." ICML (3) 28 (2013): 1310-1318. p.4

* 실습 코드 .py파일로 바꿔서 모듈화 하기 - [템플릿은 이것 이용](https://github.com/victoresque/pytorch-template)

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
