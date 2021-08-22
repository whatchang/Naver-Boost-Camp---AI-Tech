<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Transformer 내용 정리
### 목차
1. [어떻게 단어끼리의 연과성을 찾을까? - 문자의 벡터화](#1.-어떻게-단어끼리의-연관성을-찾을까?---문자의-벡터화)
2. [seq2seq란?](#2.-seq2seq란?)
3. [seq2seq에 attention이라는 것을 적용해 보자!](#3.-seq2seq에-attention이라는-것을-적용해-보자!)
4. [transformer 두둥등장!](#4.-transformer-두둥등장!)
    - [4-1. encoder](#4-1.-encoder)
    - [4-2. decoder](#4-2.-decoder)
    - [4-3. 학습과정 다시 보기](#4-3.-학습과정-다시-보기)
    - [4-4. Loss Function](4-4.-Loss-Function)
5. [참고 사이트 및 자료](참고-사이트-및-자료)
___

### 1. 어떻게 단어끼리의 연관성을 찾을까? - 문자의 벡터화

* 기본적으로 컴퓨터가 어떤 단어에 대해 인지할 수 있게 하기 위해서는 수치적인 방식으로 단어를 접근해야 한다. 그러나 수치화를 통해 단어의 개념적 차이를 나타내기는 근본적으로 어렵다.

* 이러한 한계를 극복하기 전에 NLP에서는 'one-hot'encoding'이라는 방식을 많이 사용했다. -> [과자, 아이스크림, 햄버거, 피자] 라는 사전이 있을때 어떤 단어가 사전에 해당 단어와 같다면 1로 표시해주고 나머지를 0으로 표시하므로써 0과 1의 벡터로 표현하는 방식이다. 만약 햄버거라는 단어를 표시하고 싶으면 [0, 0, 1, 0] 이라는 벡터로 표현하면 된다.

* 하지만 위의 방식으로는 컴퓨터가 단어와 단어 사이의 관계 혹은 어떤 차이점을 가지는지 이해할 수 없다.

* 이러한 단점을 해결하기 위해 고안된 방식이 바로 단어의 벡터화이다. -> 이것은 단어 자체가 가지는 의미 자체를 다차원 공간에서 벡터로 만드는 것이다.

* 위의 방식의 장점은 
    
    1. 유사도를 측정할 수 있다.
    2. 여러 개의 단어들에 대해서 평균이나 분산, 분포 등의 수치적으로 접근할 수 있따.
    3. 1~2번의 이유로 벡터 연산을 통해 추론을 내릴 수 있다.

* 이러한 단어를 벡터로 만드는 방법에는 여러 종류가 있다. 이것에 대해서는 아래의 '참고 사이트 및 자료' 부분에서 링크를 타고 좀 더 알아보면 좋을 것 같다.
<br>

### 2. seq2seq란?

* seq2seq 모델은 글자, 단어, 이미지의 feature 등의 아이템 시퀀스를 입력으로 받아 또 다른 아이템의 시퀀스로 출력을 한다.

* 이때 모델은 encoder와 decoder로 나눠지며 encoder에서 decoder로 context(hidden state)정보를 넘겨줍니다.

* seq2seq 모델 디자인에서는 하나의 RNN은 한 타임 스텝마다 sequence의 input 값과 이전 hidden state 정보 입니다. 이 두 입력은 벡터로 변환(word embedding)하여 들어가야 합니다(이유는 '1.어떻게 단어끼리의 연관성을 찾을까? - 문자의 벡터화'에서 설명을 하였습니다). 

* seq2seq에서 encoder는 input값과 hidden state의 값을 받아서 새로운 hidden state값을 만들어 내면서 동작하고 최종 만들어진 hidden state(context)를 decoder에게 전달해줍ㄴ디ㅏ.

* seq2seq에서 decoder는 decoder의 input과 context정보(2번째 step부터는 이전 hidden state정보)를 바탕으로 output과 hidden state를 생성해 나갑니다.
<br>

### 3. seq2seq에 attention이라는 것을 적용해 보자!

* 위와 같이 RNN에서 seq2seq를 이용하게 된다면 긴 문장들에 대해서 하나의 고정된 벡터(context)를 생성하는데 매우 어렵습니다. 이러한 것을 해결하기 위한 방법론이 바로 attention입니다.

* attention이란 해당 step에서 특정 단어에 더 집중할 수 있도록 만들어 줍니다. 예를 들어서 I ate apple이라는 sequence를 encoder에 넣고 생성한 context를 decoder에 넣었을때 decoder에서 step 1은 I를 step 2는 apple, step3는 ate을 집중하게 만들도록 합니다. 그래서 나는 사과를 먹었다 - 를 각 단어별로 각 step에 출력하도록 해줍니다.

* 위의 각 step별로 특정 단어에 집중을 하게 만들어주는 매커니즘은 encoder에서 decoder로 넘겨주었을때 각 encoder의 hidden state를 중첩하여 넘겨주고 이것을 decoder가 출력을 생성할 때 계속 사용하게 됩니다(기존에는 첫 step에서만 사용하고 그 후에는 decoder에서 새로 생성한 hidden state정보만을 사용했습니다).

* 위의 내용을 좀 더 자세하게 살펴보겠습니다.

    1. encoder에서 받은 전체 hidden states를 보고 각 hidden state마다 점수를 매깁니다. 점수를 매기는 방식은 밑에서 따로 설명하겠습니다.
    2. 매겨진 점수들에 softmax를 취하고 이것을 각 타임 스텝의 hidden states에 곱해서 더합니다. 이를 통해 높은 점수를 가진 hidden states는 더 큰 부분을 차지하게 되고 낮은 점수를 가진 hidden states는 작은 부분을 가져가게 됩니다. <- 특정 스텝에 특정 단어를 집중시키는 방법

* 위의 decoder에서 encoder에서 받은 hidden state에 대해서 각 step 마다 점수를 매기는 방식

    1. attention 모델에서의 RNN은 decoder의 initial decoder hidden state 마지막에 <END>가 추가로 입력을 받습니다.
    2. decoder RNN은 위의 iniial decoder hidden state와 <END>를 가지고 hidden state vector를 출력합니다. 그 후 encoder의 hidden state 모음과 
<br>

### 4. transformer 두둥등장!


<br>


#### 4-1. encoder


<br>

#### 4-2. decoder


<br>

#### 4-3. 학습과정 다시 보기


<br>

#### 4-4. Loss Function



<br>

### 5. 참고 사이트 및 자료

* ['어떻게 단어끼리의 연관성을 찾을까? - 문자의 벡터화' 참고 사이트 ](https://shuuki4.wordpress.com/2016/01/27/word2vec-%EA%B4%80%EB%A0%A8-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC/)
* ['seq2seq란?', 'seq2seq에 attention이라는 것을 적용해 보자!'](https://nlpinkorean.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
* ['transformer 두둥등장!'](https://nlpinkorean.github.io/illustrated-transformer/)
* ['transformer 두둥등장!'에서 positional vector에 대한 부분에 대해서 참고한 유튜브](https://www.youtube.com/watch?v=AA621UofTUA&t=2621s)

