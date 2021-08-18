# Day 12 Pytorch 4~5 강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Pytorch 4~5강
    * 4강 : AutoGrad & Optimizer
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

    * 5강 : Dataset & Dataloader
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

#### 드디어 부덕이를 통과하고 오늘 새로나온 과제를 해야 한다. ㅎㅎ;;; 피어세션때 팀원들과 같이 조금 봤는데 음... 오늘도 험난할 것 같다. ㅠㅠㅠㅠ

<br>

### 3. 피어세션 정리
<br>
Report
📒[금일 질문 목록]:

* nn.Linear에서의 크기 변환의 원리는 어떻게 되는가?
    * Linear(NH, NH) 이므로 H값이 변경
* torch.swipdim(input, dim0, dim1)
* Hook의 실제 사용 사례는 대표적으로 어떤게 있는가?
    * CNN모델에서 filter 설계에 사용되는것으로 알고있다.
* register_forward_pre_hook(), register_forward_hook(), register_full_backward_hook() 의 차이는 무엇인가?
    * forward_pre_hook():
        * forward가 진행되기 전에 어떠한 작용을 하겠다
        * pre_hook : parameter가 어떻게 변하는지 확인할 때 사용, input밖에 없다.
    * full_hook: input output이 있다.
* Apply 문제 해결을 방법은 어떤것이 있는가?
    * apply를 이용하거나 split을 사용하여 해결할 수 있다.
* 일반적으로 Model에서 Parameter정의를 하는데 외부에서 Parameter 정의가 가능한가?
    * 명확한 해답을 결론짓지 못했다.
📎[금일 과제 분석]

* Dataloader의 num_workers는 무엇인가?
    * 데이터를 불러올때 사용하는 서브 프로세스(subprocess) 개수이다.
* collate_fn의 역할은 무엇인가?
    * [[data1, data2, ...], [label1, label2, ...]] → [[data1,label1],[data2,label2],...]
* batch_size 문제
    * 명확한 해답을 결론짓지 못했다.



<br><br>

### 4. 학습 회고

#### 강의 내용과 정리를 하는데 오래 걸리지 않았으나 어제 과제를 하는데 시간을 많이 소비하였다. 이제 오늘 과제와 Transformer 논문 봐야 하는데.... 오늘은 늦게 자고 내일 일찍 자야겠다 ㅠㅠ

<br>

#### 이번 주는 과제가 어렵고 강의를 어렵지 않아서 피어세션 때 주로 과제를 중심으로 질문을 하고 답하는 형식으로 진행이 되었다.

<br>

#### 시각화.... 들어야 하는데.... 어제 정리 못한 프로젝트 파일 관계도 그림 그려야 하는데~~~~😂 우선 이슈에 등록해야겠다.