<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day27 NLP 5~6강 

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 강의내용 정리

* NLP 5강



<br>

* NLP 6강



<br>

<br>

## 2. 과제 정리

필수과제 3번을 해결했고 torkenizer에 대한 간단한 사용법과 필수 과제 2번의 내용이 겹쳐서 쉽게 해결한 것 같다. 다만, 내용이 좋아서 한 번더 훑어보고 내용정리를 하면 좋을 것 같다.

<br>

## 3. 피어세션 정리

#### 3강.  Recurrent Neural Network and Language Modeling

---

발표자:  `심우창` 

- 발표 내용

    [NLP3강.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c08bf727-6ec5-4543-96bd-98cb3561d6d0/NLP3강.pdf)

- Discussions

    **RNN에서  활성화함수로 Tanh를 사용하는 이유** : RNN에서는 이전 값을 중첩으로 사용하기 때문에 normalizing을 효과를 줄 수 있는 활성화함수가 필요. ReLU를 사용할 경우 이전 값이 커짐에 따라 전체적인 출력이 발산하는 문제가 생길 수 있다! Normalize 효과를 줄 수 있는 비선형 함수로 Sigmoid와 Tanh가 있는데 sigmoid는 중심값이 0이 아닌 점과 gradient vanishing이 더 잘 일어난다는 문제 때문에 tanh 함수가 더 좋은 성능을 보임. (하지만 tanh도 gradient vanishing 문제를 완전히 벗어나지는 못함.) 

    1. centre value가 0이냐 0.5냐
    --> hidden state를 time step별로 공유하기 때문에 open boundary가 단방향으로 shift됨
    2. BackProp시 sigmoid나 tanh나 문제가 되긴 함 ;; 이건 ReLU로도 해결 불가능
    때문에 Residual Learning이나 Clipping 기법이 RNN에서 해결책으로 제시되어 옴
    그러나 90년대 연구에선 그나마 tanh가 1번의 이유 + BackProp시 계산 효율이 좋았다는 결과가 있음 (LeCun의 Efficient Backprop)
    [https://arxiv.org/pdf/1211.5063.pdf](https://arxiv.org/pdf/1211.5063.pdf) (clipping)
    [https://arxiv.org/pdf/1607.03474.pdf](https://arxiv.org/pdf/1607.03474.pdf) (residual connection)
    [http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf) (tanh가 그나마 나음)
    - lstm에서 sigmoid는 analog swiching!

    **RNN BPTT의 문제점** : 자원의 한계, Gradient Exploding/Vanishing  ⇒  보완: truncated backprop (하지만 여전히 뒤쪽의 정보까지 반영해 업데이트하지 못하는 문제 존재)  ⇒  LSTM, GRU 등의 모델로 발전

    질문 :  이 부분의 $W_{hy}$ 파라미터의 역할이 무엇인지 잘 이해가 되지 않습니다!

    답변 : 아마 출력을 위해 하나의 레이어를 더해준 것 같습니다!

질문 : Sigmoid 함수의 중심값이 0이 아닌것이 왜 학습을 느리게 하는 이유인지 잘 모르겠습니다!

답변 : (블로그 다시 보고 정리)  ⇒  Sigmoid를 활성화 함수로 사용하게 되면 시퀀스로부터 전달되는 모든 입력값(x, h)들이 양의 부호를 갖게 되고, 가중치 파라미터의 미분값이 $\frac{\partial L}{\partial a}$ 의 부호에 따라 결정된다. 따라서 가중치 파라미터가 업데이트 되는 패턴이 지그재그 형태로 움직이고 학습이 원활하게 진행되지 못 하는 것이라고 한다.  (자세한 내용은 블로그 참조.)



- Sigmoid 함수의 중심값이 0이 아닌 것의 단점. (직관적인 이해에 좋음.)

[딥러닝에서 사용하는 활성화함수](https://reniew.github.io/12/)

- Why are non zero-centered activation functions a problem in backpropagation?

    [Why are non zero-centered activation functions a problem in backpropagation?](https://stats.stackexchange.com/questions/237169/why-are-non-zero-centered-activation-functions-a-problem-in-backpropagation)

    [Downsides of the sigmiod activation and why you should center your inputs](https://rohanvarma.me/inputnormalization/)

    [](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture6.pdf)

    [8. activation function - saturation현상 / zigzag현상 / ReLU의 등장](https://nittaku.tistory.com/267)

#### 4강.  LSTM and GRU

---

발표자:  `김제우` 

- 발표 내용

    [https://smilingface.notion.site/LSTM-GRU-31a25ac6805d4e8e909cb285844e53b1](https://www.notion.so/LSTM-GRU-31a25ac6805d4e8e909cb285844e53b1)

- Discussions

    질문 : LSTM의 forget gate, input gate 에서 얼마나 이전의 정보를 덜어주고 얼마나 현재 입력의 정보를 더해줄 것인지 정하는 것이 학습되는건지? 아니면 하이퍼 파라미터처럼 정해지는건지?

    답변 : $W_{ih}$ , $W_{hh}$ 에 따라서 학습되는 파라미터입니다!

    우창님 의견 : 값이 소실된다는 것이 입력값이 사라진다고도 볼 수 있을까요?

    답변 : 네! 정확히는 희석된다는 표현이 느낌상 잘 맞는거 같지만, Cell state를 업데이트할 때 계속해서 이전의 값들은 얼마나 덜어줄 것인지를 결정하고, 현재의 입력값을 얼마나 더해줄 것인지를 결정해주면서 값을 업데이트 해가다 보면 시퀀스가 길어졌을 때 앞부분의 입력값 또한 희석된다고 볼 수 있을것 같습니다!

    그리고 Gradient 소실과 입력값이 희석되는 문제 때문에 공유되는 가중치 $W_{hh}$ , $W_{ih}$ 를 업데이트할 때 시퀀스 앞부분의 입력이 Loss에 미치는 영향이 적어지면서 앞부분의 정보가 잘 반영되도록 가중치 학습이 이루어지는 것이 어렵다는 문제도 있는것 같구요!

### Further Question

---

Q )  BPTT 이외에 RNN/LSTM/GRU의 구조를 유지하면서 gradient vanishing/exploding 문제를 완화할 수 있는 방법이 있을까요?

A )  [https://proceedings.mlr.press/v28/pascanu13.pdf](https://proceedings.mlr.press/v28/pascanu13.pdf)

- Gradient Clipping
- `Regularization` L1 or L2 Penalty on $W_{hh}$
- `Teacher Forcing`
- Use Hessian-Free Optimizer in conjunction with structural damping
    - [https://icml.cc/Conferences/2011/papers/532_icmlpaper.pdf](https://icml.cc/Conferences/2011/papers/532_icmlpaper.pdf)
- $W_{hh}$의 diagonal term을 1로, off-diagonal term은 small random value로 초기화
    - A Simple Way to Initialize Recurrent Networks of Rectified Linear Units
- Leaky Integration units or Recurrent Highway Network
    - a * x + (1-a) * f(x)

⇒  정리  :  **구조적인 변화** (lstm, gru) / **가중치에 직접 변화를 가하는 형식** (regularization, clipping, diagonal term)  / **학습 방식에서의 차이** (teacher forcing , *hessian-free optimizer* , leaky integration ...)

Q )  RNN/LSTM/GRU 기반의 Language Model에서 초반 time step의 정보를 전달하기 어려운 점을 완화할 수 있는 방법이 있을까요?

A )

Attention 모듈을 이용하면 출력 시퀀스가 입력 문장에서 참조하는 주요 부분에 가중치 파라미터를 두고 Loss 역전파가 추가로 이루어질 수 있도록 만들어서 초반 time step의 정보 전달 문제를 완화하는 방법이 될 수 있을것 같습니다.

5강에서 교수님께서 살짝 언급해주셨던게 앞부분의 정보를 잘 전달할 수 없으니까 아예 입력문장을 뒤집어서 뒤쪽부터 넣어주고 앞부분의 정보가 더 많이 포함되어 있도록 하는 방법도 사용할 수 있다고 하셨는데, Bidirectional 네트워크를 사용해서 순방향의 입력으로 만들어진 Context vector 와 역방향의 입력으로 만들어진 Context vector를 모두 이용하여 다음 Layer의 입력 또는 마지막 출력값으로 이용하면 역시 앞부분의 정보 전달 문제를 보완할 수 있을것 같습니다!



### 회의록

---

-  내일 모더레이터: 준영님 ,  5강: 대웅님 , 6강: 전진님

-  특이사항: 맡은 논문 차근차근 읽고 있기 , 필수과제 RNN-based Language Model 오늘까지 제출.

다들 정리 어떻게 하세요?

명훈님 : 이번주 내용은 교수님께서 굉장히 스텝 별로 자세히 알려주셔서 내용정리에 집중하기보다는 코드 수준에서 한단계씩 살펴보고 구현하는 방식으로 공부를 하고 있습니다!

대웅님 : 기존에는 전부 쓰는 식으로 정리를 했는데 너무 시간이 오래 걸리다보니 그냥 제 방식대로 간편하게 정리합니다!

나 (동규) : 그냥 냅다 씁니다..

제우님 : 냅다 듣는데로 전부 notion에 작성하고 다시 읽으면서 중요 keyword들이랑 summary를 github에 정리하려고 하고 있습니다!

질문과 답변이 아주 활발하게 이루어짐. 굳굳.

<br>

## 4. 학습 회고

#### 아침에 강의를 듣고 오후에는 3시간정도 PPT만들고 피어세션하고 밥먹고 쉬고 과제를 하다보니 벌써 새벽 1시30분이 되려고 한다 ㅎㅎ;;;;

#### 아직 강의 내용정리는 못했지만 오늘 무리해서 한다면 분명 내일 큰 악영향을 줄 것 같아서 오늘은 여기까지만 하고 내일 8시30~9시 정도에 일어나서 공부하려고 한다.

<br>

#### 오늘은 NLP 3강 내용에 대해서 발표를 하게 되었고 내가 이해한 내용과 궁금했던 내용등에 관해서 발표를 했다. 다행히 열심히 준비한 만큼 팀원들과 여러 내용을 공유할 수 있어서 좋았고 다른 캠퍼님의 발표와 여러 질문들 그리고 further question에 대한 서로의 생각을 공유해서 정말 알찬 피어세션이었다.
#### 하루하루 팀원들 덕분에 많은 것을 배우고 느끼는 하루인것 같다. 
<br>

#### 내일 강의 정리 잘 하고~ BERT 꼭 읽어야 되~!!! I can do it!!!
#### 아무튼 수고 많았어~~~ ㅎㅎ
<br>