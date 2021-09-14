<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day31 Self-supervised Pre-training Models

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 강의내용 정리

### Self-supervised Pre-training Models -> GPT1, BERT

#### GPT-1

* 무엇을 해결하고자 하는가?

<br>

* 이전과 transformer과 다른 점은?
    * transformer에서 decoder구조만 사용.
<br>

* 특징
    * 다양한 토큰 사용 -> 심플한 task + 다양한 NLP에서의 많은 task를 처리할 수 있다. => 통합된 모델
    * 아래의 그림과 같이 task에 따라서 input의 구조와 들어가는 special token이 다르다. + task에 따른 마지막 layer는 다르게 사용하지만 transformer block은 그대로 사용한다.
    <img src=./img/specialtoken.png>
    
<br>

* 핵심구조
    <img src=./img/structure.png width=300><br>
    * input text를 positional enbedding을 더한다.
    * 이전에 배웠던 transformer의 block과 같은 multi-head attention -> residual connection -> layer normalization -> feed forward -> residual connection -> layer normalization로 구성된 block을 12번 정도 거친 후 task에 따라서 마지막 linear layer가 달라진다. 

<br>

* 동작과정

<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용
    * [좀 더]self-supervised learning
<br>

* Question!

<br>
<br>

#### BERT

* 무엇을 해결하고자 하는가?

<br>

* 이전과 GPT-1과 다른 점은?
    * transformer에서 encoder만 사용. -> 앞 뒤 문맥을 고려할 수 있다.
    * NSP(Next Sentence Prediction) : 문장관의 관계 등을 추론할 때 사용되는 방식이다. 이때 GPT-1에서는 마지막에 extract token을 사용하였지만 BERT는 input의 맨 처음에 CLS token을 넣어서 사용한다.
    * 학습을 위해 사용한 data corpus의 개수 : BERT > GPT-1
    * 학습시 사용한 batch size : BERT > GPT-1
    * GPT-1은 task가 다르더라도 같은 learning rate 사용하였지만 BERT는 각기 다른 learning rate을 사용한다.

<br>

* 특징
    * MLM(Masked Language Model) : input의 특정 부분을 mask로 치환한다. Mask의 비율은 hyperparameter이다.
    * MLM은 전체 input의 15%만 masking을 하고 이때 mask는 80%만 실제 mask로 치환, 10% random word로 치환, 10%는 이전과 같은 mask(mask를 안 해주는 것과 같음)로 치환해주는 것이 가장 성능이 좋았다고 한다.
    * input word에 WordPiece + segmentation + positional 등의 embedding을 해준다.

<br>

* 핵심구조
    * BERT는 transformer의 encoder부분을 그대로 사용했으며 아래와 같이 Base와 Large에 따라 구조가 다르다.
    <img src=./img/bert-architecture.png>


<br>

* 동작과정
    * step1 : 3가지의 embedding을 통해서 input word를 만들어준다.
    * step2 : transformer의 encoding과 동일한 구조로 된 block을 각 bert architecture에 맞게끔 수행해준다.
    * step3 : 이렇게 나온 값에 대해서 task에 따라 마지막 linear layer를 다르게 해준다.
<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용
    * [아직]QuA를 BERT로 푸는 부분에 대해서


<br>

* Question!

<br>
<br>

#### GPT-2

* 무엇을 해결하고자 하는가?
    * decaNLP에서

<br>

* 이전과 GPT-1과 다른 점은?
    * transformer layer를 더 쌓았다.
    * 학습을 위한 데이터 40GB이고 질이 좋은 데이터 사용
<br>

* 특징
    * down-stream tasks in a zero-shot setting

<br>

* 핵심구조


<br>

* 동작과정

<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용


<br>

* Question!

<br>
<br>

#### GPT-3

* 무엇을 해결하고자 하는가?

<br>

* 이전과 GPT-1과 다른 점은?

<br>

* 특징

<br>

* 핵심구조


<br>

* 동작과정

<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용


<br>

* Question!

<br>
<br>

#### ALBERT

* 무엇을 해결하고자 하는가?

<br>

* 이전과 GPT-1과 다른 점은?

<br>

* 특징

<br>

* 핵심구조


<br>

* 동작과정

<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용


<br>

* Question!

<br>
<br>

#### ELECTRA

* 무엇을 해결하고자 하는가?

<br>

* 이전과 GPT-1과 다른 점은?

<br>

* 특징

<br>

* 핵심구조


<br>

* 동작과정

<br>

* 아직 이해가 덜 된 부분 / 좀 더 공부할 내용


<br>

* Question!

<br>
<br>
<br>

## 2. 과제 정리

#### 아직 선택과제에 대해서는 하지 못했다 ㅠㅠㅠㅠ

<br>

## 3. 피어세션 정리
# 7, 8강.  Transformer

---

발표자:  진명훈

- 발표 내용
    - 논문에 충실한 강의 내용

    - RNN의 Long-term dependency 문제 해결 위해 제안됨
    - forward, backward 연산 path가 너무 길어 장기 의존성 포착이 어렵다.
    - 또한 Recurrent 연산은 차원에 대해 Quardratic 연산이라 hidden unit 늘리기는 부담

    ## Transformer: Long-Term Dependency

    - 서로 간의 상관성을 Globaly 하게 엮어줌
    - 노드 별로 모두 연결되어있기 때문에 RNN 방식처럼 참조하는 토큰에 대해 seq length 만큼 연산을 수행할 필요 없음. 그러나 이 부분 때문에 Seqeunce 길이에 Quadratic하게 연산 및 메모리 사용
    - Convolution을 이용한 경우 receptive filed 만큼은 한 번에 볼 수 있지만 전체를 한 번에 보진 못함

    [How Transformers work in deep learning and NLP: an intuitive introduction | AI Summer](https://theaisummer.com/transformer/)

    ## Transformer: Scaled Dot-Product Attention

    - MHSA의 경우 연산 복잡도에 영향을 미치는 연산이 크게 2가지가 있음
    - BS = 1, Seq_Len = 4, Hidden_dim = 3 이라 가정
    - Query와 Key에 대한 MatMul : (4, 3) x (3, 4) → O(4^2 * 3)
    - [참고] MatMul의 시간 복잡도 : (a, b) x (b, c) → O(a * b * c)
    - Attention Score와 Value에 대한 MatMul : (4, 4) x (4, 3)  → O(

    ## Scaling

    - 3.2 Scaled Dot-Product Attention
        - Attention 종류로 Additive attention( Bahdanau Attention)와 Dot-product attention이 있다.
        - 이론적인 복잡도는 동일하지만, Dot-product attention이 빠르고 메모리 효율적
        - Additive Attention은 Query Key를 concat하므로 한 번에 올리는 양이 많아 메모리 비효율적 Matmul 코드에 최적화 되어 짤 수 있기 때문에 훨씬 빠르다
        - scaling을 안해줬을 때는 Additive가 성능이 더 높다(이에 대한 분석은 하지 않고, 주석으로 추측을 추가함)
        - HF에서도 scaling 구현 여부를 보자
            - BART


        - Multi-Head로 나눌 때 전체 dim을 나눠주는 전략을 취함 (1, 10, 512) → (1, 10, 32, 16)
        - [참고]Attention 종류
            - Additive
            - Dot-Product
            - Location-based (conv와 비슷, locally하게 봄)

    ## Positional Encoding

    - 위치 정보를 반영시키기 위해 각 위치별 Positional encoding 벡터값을 만들어두고 해당 위치의 임베딩 벡터에 더한다
    - RNN은 순차적으로 토큰을 넣어주기 때문에 순서 관계가 반영됨
    - Encoding : 고정된 규칙
    - Embedding : 학습 가능한 벡터
        - BERT에서는 이걸 사용함

    - 이후 등장하는 논문에서는 Attention map에 직접 주입해주는 논문도 있음

    ## MHA(Multi-Head Attention)

    - 여기선 source와 target 이 모두 동일
    - Q, K, V까지는 동일하나 프로젝션을 하는 순간 다른 값의 텐서가 됨 → symetric matrix가 아님

        $QW_i^Q(KW_i^K)^T$

# Masking

- Encoder에서도 Padding에 Masking을 해줌
- Pad에 -inf 후 exp 취하면 0에 가까운 값이 됨
- softmax의 연산에서 차이가 있는 부분에 대해서만 연산을 하게됨, 불필요한 패딩 연산을 줄임

## Multi-Head View

- head의 개수 만큼 다른 부분을 참조한다고 직관적으로 설명하는 글들이 많으나 실제로 그렇지 않다고 주장하는 논문들이 있다.
- 이에 대해 궁금하다면
    - Why multi-head self-attention works

        [Why multi-head self attention works: math, intuitions and 10+1 hidden insights | AI Summer](https://theaisummer.com/self-attention/)

# Multi-Head를 합친 이후의 Matrix는 Low-Rank

- 각각의 head 출력을 concat 후 linear해 출력하는 게 MHA 모듈인데,
- 중간 중간 생기는 attention map이 low-rank
- 독립인 Rank가 많을 수록 더 많은 정보를 담고 있다고 이해

- 10개의 head가 있다고 할 때, Low-rank 가 발생했다는 건, 서로를 다른 head로 표현 가능하다는 것. 즉비효율적인 학습

- linformer에서는 eigen value, vector 중에서 상위 ???
- 이 부분은 다시 살펴봄
- Linformer의 경우 이론적 복잡도 O(n * d)

# Residual Connection

# Layer Normalizatoin

# FFN

- Attetnion 결과 끝나고 넘겨주는 부분인데 중간에 4배를 키워줌

- 이유
    - Attention 만으로는 안된다. FFN, Skip-Connection이 없으면 빠르게 1-rank matrix로 수렴 모든 token 이 종속적인 값을 갖게 됨
    - FFN이 중요한 이유 (수식 정리 결과) → 4배 키워 주는 부분과 관련
    - 실험적 증명이므로 주장에 가깝지만, 4배 키워주는 것과 Skip-Connection이 없으면 성능 저하

- Layer-Normalization 에 대해선 아직 논란이 있는 듯
- Encoder는 마지막 hidden state가 Decoder의 모든 레이어에 들어감

- Decoder
- 코드

- 크로스엔트로피 ignore index 값이 기본 -100이라 계산에서 제외하여 효율적으로 연산됨

- Optiimizer Part에서

- PostLN: LN(x + F(x)
- PreLN( x + F(LN(x))
- Pre-LN으로 구조를 바꾸면 학습이 안정적으로 되었다.

- Discussion

# Further Question

---

- Attention은 이름 그대로 어떤 단어의 정보를 얼마나 가져올 지 알려주는 직관적인 방법처럼 보입니다. Attention을 모델의 Output을 설명하는 데에 활용할 수 있을까요?

# 실습 코드 리뷰

---

발표자: 김제우

- 8강 코드는 아직 준비되지 않아 내일 다시 리뷰
- 발표 내용

    ## 7강 코드리뷰, MHA

    - 100개의 단어가 있다고 가정하고 인코딩된 입력 데이터가 있다 가정함
    - 제일 긴 문장을 중심으로 패딩

    - Hyperparameter setting & embedding

    - 임베딩에 대한 개념 정리: 각 단어(토큰)에 512 차원을 부여

    - Linear Transformation & Head로 나누기


    - 512개의 차원을 8개로 쪼갬 → 각각의 head의 dim = 64, 이후 concat해 linear로 나옴



- 최종적 Attention Score 구함


- head 별 concat


- 질문 : contiguous()를 언제 쓰느냐?
    - BartAttention 객체



    - 쿼리에 _shape, 키 밸류에도 처리



    - 텐서 뷰를 먼저 해주고, 트랜스포스를 하면 (B, num_head, seq_len, ...) 순서가 되는데 메모리 순서가 뒤섞이므로 contiguos() 처리

- 텐서의 모양을 바꿔줄 때 Reshpae,  Transpose, Permute, View(모양도 바꾸면서 메모리 위치까지 바꿔주고 - contiguous를 안써도 됨)

- View와 Reshape은 Contiguous 가 True, Permute와 Transpose는 False이므로 무조건 contiguous() 붙여줄 것

    [Difference between view, reshape, transpose and permute in PyTorch](https://jdhao.github.io/2019/07/10/pytorch_view_reshape_transpose_permute/)

- Matrix 연산 시 데이터들이 연속적으로 배열되어있어야 한 번에 cache로 옮길 수 있고, vector 연산을 효율적으로 하는 모듈이 cpu에 있음, 연속적으로 배열되어 있어야 빠르게 연산 가능하다(numpy가 빠른 이유와 관련)
- transpose 후 view 하면 contiguous가 깨져있어 에러가 발생, view는 원래 메모리 위치 안에서 텐서의 시작점을 기억해 변환함, 메모리 상에선, view는 contiguous 가 보장된 것에 쓸 수 있지 그렇지 않은 것에 적용할 경우 깨짐.


<br>

## 4. 학습 회고

#### 오늘 오전에는 9강 강의를 듣고 내용을 정리하였다. 다 정리하지는 못했지만 금방 시간이 지나가서 점심을 먹었고 1~2시는 논문 리뷰를 듣고 2~3시30분까지는 BART 논문을 읽었다. 시간이 별로 없어서 전체를 다 읽지는 못하였고 abstract, introuction, conclusion 부분만 읽었다. 대신 저번에 멘토님께서 조언해 주신 방법대로 요약집이나 유튜브 영상을 보지 않고 논문을 읽고 이전 모델에서 어떤 부분이 달라졌고 무엇을 해결하고 싶은지, key point, 논문 진행 흐름 등을 생각해서 정리하였다. 이런 부분은 신경쓰면서 읽으니까 확실히 더 집중이 되고 재미?있었던 것 같다 ㅎㅎ
<br>

#### level3 팀에서는 알고리즘 문제를 풀었는데 오랜만에 풀어서 어색하고 어려운 점도 있었지만 해결했을때의 성취감이 매우 좋았다 ㅎㅎ
<br>

#### 원래는 오늘 강의 듣고 정리를 한 후 내일 발표할 ppt를 만들어야 하지만 오늘 무리하면 내일 오전시간이 아예 없어질 것 같아서 이만 잠 자려고 한다.
<br>

#### 오늘도 수고했지만 내일 강의 꼭 듣고 ppt 잘 만들도록 ~!!!