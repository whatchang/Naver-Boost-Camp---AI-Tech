# Day 13 Pytorch 6~7 강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Pytorch 6~7강
    * 6강 : AutoGrad & Optimizer
        * 신경망<br>
        &nbsp; - &nbsp; 여러 layer들이 합쳐져 하나의 network를 만든다. <br>
        &nbsp; - &nbsp; 여기서 똑같은 layer들이 반복되기도 한다. <- 이러한 점이 layer와 레고 블록과 비슷하다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 이러한 layer는 torch에서 torch.nn.Module을 이용하여 만들 수 있다.<br>
        <br>

        * torch.nn.Module<br>
        &nbsp; - &nbsp; 딥러닝을 구성하는 Layer의 base class이다. <br>
        &nbsp; - &nbsp; Input, Output, Forward, Backward 정의 <br>
        &nbsp; - &nbsp;  학습의 대상이 되는 parameter(tensor) 정의 <br>
        <br>

        * nn.Parameter<br>
        &nbsp; - &nbsp; Tensor 객체의 상속 객체 <br>
        &nbsp; - &nbsp; nn.Module 내에 attribute가 될 때는 required_grad=True로 지정되어 __학습 대상이 되는 Tensor__ <br>
        &nbsp; - &nbsp; 우리가 직접 지정할 일은 잘 없다. <- 대붑분의 layer에는 weights값들이 지정되어 있다. <br>

        * Module의 forward & backward<br>
        &nbsp; - &nbsp; foward <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 모듈 instance를 만들고 거기에 input을 주게 되면 자동으로 foward가 실행이 된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; forward 전후에 hook을 집어 넣을 수 있다.  
        &nbsp; - &nbsp; backward <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Layer에 있는 Parameter들의 미분을 수행한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Forward의 결과값(model의 output=에측치)과 실제값간의 차이에 대해 미분을 수행한다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 해당 값으로 Parameter 업데이트 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; step()함수로 Parameter 업데이트<br>
        &nbsp; - &nbsp; 학습 진행 순서 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; optimizer를 zero_grad()함수를 통해서 이전 미분값에 영향을 받지 않도록 초기화 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 만든 instance에 input을 줘서 예측값을 구해준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 3. &nbsp; loss instance를 통해서 차이를 계산해 준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 4. &nbsp; backward()를 통해서 gradient를 계산해준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 5. &nbsp; step()을 통해서 Parameter들을 업데이트 해준다. <br>
        &nbsp; - &nbsp; backward에 대한 TMI <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 실제 backward는 Module 단계에서 직접 지정가능하다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Module에서 backward와 optimizer오버라이딩은 (알아서)자동으로 해준다.<br>
               

        <br>

    * 7강 : Dataset & Dataloader
        * 개요<br>
        &nbsp; 1. &nbsp; 데이터를 모으고 전처리하면 학습을 위한 Data가 만들어 집니다. <br> 
        &nbsp; 2. &nbsp; Dataset 클래스에서 데이터에 대한 init, len, getitem등의 매직 메서드를 정의해줍니다. <br> 
        &nbsp; 3. &nbsp; DataLoader 클래스에서 데이터를 어떤식으로 가져올지 정합니다. <br> 
        &nbsp; 3.5 &nbsp; Dataset 혹은 DataLoader 부분에서 data를 transforms 클래스를 통해서 tensor로 바꿔줍니다. <br> 
        &nbsp; 4. &nbsp; Model에 데이터를 전달하여 학습을 합니다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Dataset 클래스에서 __ getitem __()은 하나의 데이터를 어떻게 반환을 해줄지에 대해서 정의되어 있는 매직 메소드입니다. <- map-style <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [transforms에 대한 좀더 자세한 내용(한국어)](https://tutorials.pytorch.kr/beginner/data_loading_tutorial.html)<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [transforms에 대한 좀더 자세한 내용(영어)](https://pytorch.org/vision/stable/transforms.html)<br>
        <br>

        * Dataset 클래스<br>
        &nbsp; - &nbsp; 데이터 입력 형태를 정의하는 클래스 <br>
        &nbsp; - &nbsp; 데이터를 입력하는 방식의 표준화 <br>
        &nbsp; - &nbsp; Image, Text, Audio 등에 따른 다른 입력정의 <br>
        &nbsp; - &nbsp;  __ init __ : 초기 데이터 생성 방법을 지정 <br>
        &nbsp; - &nbsp; __ lend __ : 데이터의 전체 길이 지정 <br>
        &nbsp; - &nbsp;  __ getitem __ : index 값을 주었을 때 반환되는 데이터의 형태 정의 <br>
        &nbsp; - &nbsp;  Dataset 틀래스 생성시 유의점<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 데이터 형태에 따라 각 함수를 다르게 정의해야 한다. <br>
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 모든 것을 데이터 생성 시점에 처리할 필요는 없다 : image의 Tensor 변화는 학습에 필요한 시점에 변환해도 상관없다 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 데이터 셋에 대한 표준화된 처리방법을 제공해야 한다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; 후속 연구자 도는 동료에게 많은 도움이 된다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 최근에는 HuggingFace 등 표준화된 라이브러리 사용함 <br>
        

        <br>

        * DataLoader 클래스<br>
        &nbsp; - &nbsp; Data의 Batch를 생성해주는 클래스 <br>
        &nbsp; - &nbsp; 학습직전(GPU feed전) 데이터의 변환을 책임진다.<br>
        &nbsp; - &nbsp; Tensor로 변환하는 업무 + Batch 처리 업무 <- 메인 업무<br>
        &nbsp; - &nbsp; 병렬적인 데이터 전처리 코드의 고민이 필요하다.<br>
        &nbsp; - &nbsp; instance 생성시(dataset instance를 인자로 받음) batch_size와 shuffle 유무를 지정해 줄 수 있다.<br>
        &nbsp; - &nbsp; 예를 들어서 target : [A, B, C, D, E]와 label : [a, b, c, d, e]인 데이터가 있고 Dataset 클래스에서 getitem부분을 {'target : [A], 'label' : [a]}와 같은 형식으로 반환해 줄때 DataLoader(dataset instance, batch_size=2)라면 아래와 같이 된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; iter 1 : {'target : [A, B], 'label' : [a, b]}  <br>
        &nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; iter 2 : {'target : [C, D], 'label' : [c, d]}  <br>
        &nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; iter 3 : {'target : [ E ], 'label' : [ e ]}  <br>
        &nbsp; - &nbsp; DataLoader의 파라미터 중 sampler : 데이터를 어떻게 뽑을지 인덱스를 정하는 거 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [참고할 블로그 - 안수빈 마스터님](https://subinium.github.io/pytorch-dataloader/)<br>
        &nbsp; - &nbsp; DataLoader의 파라미터 중 collate_fn : data와 label 한 쌍으로 묶여있는 것을 data, label 따로 묶어주는 형태로 변환  <- 데이터 자체의 길이가 동일해야 할 때, 다시 말해서 패딩이 필요한 데이터 들이 섞여 있을때 사용하는 파라미터이다.<br>
        <br>
       
    

### 2. 과제 수행 과정 / 결과물 정리
<br>

####  과제ㅠㅠㅠㅠㅠ 너무 어렵다.... 마지막 torchtext에 대한 내용인데 이해가 잘 안 된다 ㅠㅠ 

#### 일단 해볼 수 있는데 까지 해보고 그래도 잘 안되면 우리조 다른 캠퍼님들꺼 코드를 참고해서 이해해 보려고 한다.

#### 아무튼 마지막까지 화이팅~~~!!!

<br>

### 3. 피어세션 정리
<br>\
📒 오늘의 질답 및 과제 분석

- (지난 질문) Custom data loader - batch_size 문제
- Tensor는 concatenate를 통해 value 삽입. ~ 가장 긴 값을 찾고 순차 삽입.
- functional.pad 사용
- hstack 사용
- 과제
- 흑마법 구현 : forward.hook 사용
- TitanicDataset 접근 : 성욱님의 코드 리뷰.
- __getitem__ 에서 학습 데이터가 아닐 경우, y를 반환하지 말라? : y는 라벨. train=True 여부를 판단하고 getitem에서 조건문을 사용하기.
- init 함수 구현에 대한 자세한 설명 요 : 학습 레이블을 잡았을 때, 레이블을 제외한 것들이 features(데이터 목록(string)). ~ 멘토님께 이어 질문하기.

🚀 논문 리뷰

- Transformer (Attention is All needs you)
- 구성 흐름 및 질답(Q, K, V 생성) 진행.
- 참조 ↓
- 나동빈님 강의
- https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a8f8b4e-926a-4fec-baf5-03c31ece02e4/Untitled.png
- https://nlpinkorean.github.io/illustrated-transformer/


📎 멘토링 질문

- 다음주면 이미지 분류 대회. 어떤 모델을 사용할지, 참조 자료가 있을지?
- 데이터셋에 관한 질문.



<br><br>

### 4. 학습 회고

#### 오늘 transformer 논문 리뷰 하는 날이라서 나동빈님의 리뷰 영상이라 여러 사이트를 참고해서 공부했다. 확실히 여러번 보고 익숙해지니까 이전보다 많이 이해된 것 같다. 그리고 단어를 임베딩해주는 이유를 잘 몰랐었는데 https://shuuki4.wordpress.com/2016/01/27/word2vec-%EA%B4%80%EB%A0%A8-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC/ 이 글을 통해서 잘 이해가 되었다. 오늘은 뭔가 평소보다 더 많은 내용을 배운 것 같아 너무 좋다 ㅎㅎ 

#### transformer에 대해서 공부한 것들은 주말에 따로 정리해서 한 번 더 봐야겠다~~!

<br>

#### 피어세션때 논문 리뷰하고 과제에 대해서 서로 여러 고민을 하고 모르는 것 물어보면서 좋은 시간을 보냈다. 다만 조금 아쉬웠던게 논문 리뷰부분이었다. 이번에 진행했던 방식은 모르는 내용에 대해서 서로 질문하고 그랬는데 음... 뭔가 한 명이 논문에 대해서 간략하게(10~15분정도) 발표하고 서로 모르는 것 질문하면 더 좋지 않을까 싶었다. <- 물론 이번주는 할게 너무 많아서 transformer에 대해서 공부를 한 것만 해도 대단한 거라고 생각한다. 

#### + 다음 논문 리뷰를 하는 시간이 있을때 미리 많이 준비해서 ppt도 만들고 다른 사람들에게 내가 배운 내용에 대해서 공유해보도록 해야겠다, <- transformer도 해보려고 했지만... 부덕이.... 2번째 과제.... 😭😭😭

<br>

#### 멘토링때 '다음 주 대회에서 점수를 측정하는 방식이 개인 단위인가요?'라는 질문을 했었는데 개인단위라고 답을 주셨다. 다행히? 개인단위라서 내가 다른 사람들에게 피해를 끼칠 일이 없어서 마음이 놓였다 ㅎㅎ <- 그리고 대회때 열심히 공부하고 서로 문제를 해결하기 위한 접근 방식을 공유하고 토론?의논? 해보면 좋을 것 같다.

<br>

#### 오늘은 일찍자고 내일 아침에 일찍 일어나서 과제 도전하다가 잘 안되면 다른 캠퍼님 코드를 이해해서 내 문제에 적용시켜볼 예정이다. + 오늘 강의 내용 정리도 내일 해야 될 것 같다 ㅠㅠ
<br>

#### 내일이면 한 주가 또 끝나간다. 요즘 정신없이 과제하고 강의 듣고 정리하다 보니 시간이 참 빠르게 지나간다. 기분이 묘하게 이상하다(긍정적으로). 또 할 일이 많아서 잠도 줄이고 의자에 오랫동안 앉아있어서 허리랑 목도 아프지만 매일매일이 행복하다. 그리고 항상 느끼는 것인데 오늘 피어세션때에는 어떤 질문들이 나오고 또 그것에 대한 어떤 답변이 나올지 기대되서 부스트캠프 혹은 내 일상에서 피어세션이 메인이지 않나 싶다. <- 물론 강의 듣는거와 필수 과제 하는 것도 중요하다! ㅎㅎ

<br>

#### 아~무~튼 오늘도 고생한 내 자신아~~~ 대단하구머이~~~!😆