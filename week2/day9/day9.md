# Day 9 DL basic 7~8강 

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* DL basic 7~8강
    * 7강 : Convolutional Neural Networks
        * convolution 기본<br>
        &nbsp; - &nbsp; convolution 연산 <br>
        <img src='./img/cnn_basic1.png'>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 커널(filter)을 image에 convolution 연산을 통해 output이 만들어 진다. 이때 output의 (i-k+2p)/s + 1이다(p는 padding, s는 stride를 뜻한다). <br>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 연산방법은 커널과 image를 element wise로 각각의 원소끼리 곱하고 결과를 다 더하면 된다. 이런식으로 stride로 지정된 크기만큼 이동하면서 하면 위의 결과에서 output과 같은 size의 결과가 나온다.  <br><br>
        &nbsp; - &nbsp; RGB image convolution <br>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 아래와 같이 깊이(채널)이 생격다. 하지만 연산방법은 위와 동일하며 이런식의 계산 결과로 나온 값의 깊이는 1이 된다.<br>
        <p align='center'><img src='./img/rgb1.png' width=350></p>
        <br>
        &nbsp; - &nbsp; Stack of Convolutions <br>
        &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 아래 그림과 같이 32 * 32 * 3의 이미지에서 5 * 5 * 3 커널을 이용하면 28 * 28 * 1 이미지가 나온다 이때 각 원소에 Relu, 활성화 함수를 적용시켜주면 하나의 feature가 나오게 된다. 이것을 4번 해주면 가운데 모양처럼 깊이가 4인 feature가 나온다. <br>
        <p align='center'><img src='./img/stack_of_convolutions.png' width=350></p>
        &nbsp;&nbsp;&nbsp;&nbsp; Quiz. &nbsp; 위에서 첫번째 이미지에서 kernal(5 * 5 * 3)을 가지고 convolution연산을 할때(이때 그림과 맞찬가지로 출력의 채널은 4이다.) 몇개의 파라미터가 필요한가?<br>
        &nbsp;&nbsp;&nbsp;&nbsp; Answer. &nbsp; 5 * 5 * 3 * 4 이다.<br>
        <br>
        
        * CNN<br>
        &nbsp; - &nbsp; 일반적으로 CNN의 구성 요소 : convolution layer, pooling lyaer, fully connected layer <br>
        &nbsp; - &nbsp; 최근에는 fully connected layer부분 말고 다른 방식을 사용하여 파라미터의 개수를 줄이고자 한다. <- 정확하게는 layer은 deep하지만 파라미터 개수는 적은 방식을 이용 <br>
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; Deep learning에서 학습시켜야할 파라미터가 많으면 많을수록 학습이 어렵고 generaliztion performance가 떨어진다.<br><br>
        &nbsp; - &nbsp; stride : kernel을 몇칸씩 이동하면서 convolution을 시행하는지에 대한 것 <br>
        <p align='center'><img src='./img/stride.png' width=350></p>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; padding : 가장자리에 채워주는 것 <-  input과 output의 special dimension을 똑같게 만들어주기 위해 사용(special dimension이란 input의 데이터를 말함.)<br><br>

        * Exercise : AlexNet구조에서 파라미터 구하기 연습<br>

        &nbsp; 1. &nbsp; 가장 오른쪽 화살표는 그 화살표 기준으로 왼쪽에서 convolution을 해서 오른쪽 output이 나온 것이다. 이때 필요한 파라미터의 개수를 구하시오. 대략적인 개수는 화살표 위의 숫자와 같습니다. <br>
        <p align='center'><img src='./img/ex1.png'></p>
        &nbsp; ->  &nbsp; 11 * 11 * 3 * 48 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 2. &nbsp; 문제 내용 동일 <br>
        <p align='center'><img src='./img/ex2.png'></p>
        &nbsp; ->  &nbsp; 5 * 5 * 48 * 128 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 3. &nbsp; 문제 내용 동일<br>
        <p align='center'><img src='./img/ex3.png'></p>
        &nbsp; ->  &nbsp; 3 * 3 * 128 * 2(자세히 보면 커널이 위, 아래로 사용됨) * 192 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 4. &nbsp; 문제 내용 동일<br>
        <p align='center'><img src='./img/ex4.png'></p>
        &nbsp; ->  &nbsp; 3 * 3 * 192 * 192 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 5. &nbsp;문제 내용 동일<br>
        <p align='center'><img src='./img/ex5.png'></p>
        &nbsp; ->  &nbsp; 3 * 3 * 192 * 128 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 6. &nbsp; 문제 내용 동일 <br>
        <p align='center'><img src='./img/ex6.png'></p>
        &nbsp; ->  &nbsp; 13 * 13 * 128 * 2048(벡터) * 2(output이 위, 아래 2개 이므로)<br>
        &nbsp; *  &nbsp; dense layer는 MLP이다. -> 파라미터 개수는 input의 파라미터 * out의 개수이다.<br>
        <br>

        &nbsp; 7. &nbsp; 문제 내용 동일 <br>
        <p align='center'><img src='./img/ex7.png'></p>
        &nbsp; ->  &nbsp; 2048 * 2(2개의 벡터가 크로스 되기도 해서 -> 한개당 크로스 + 직선) * 2048 * 2(output이 위, 아래 2개 이므로)<br>
        <br>

        &nbsp; 8. &nbsp; 문제 내용 동일 <br>
        <p align='center'><img src='./img/ex8.png'></p>
        &nbsp; ->  &nbsp; 2048 * 2 * 1000<br>
        <br>

        * 1 * 1 convolution<br>
        &nbsp; - &nbsp; special dimension을 유지하되 파라미터를 줄일 수 있다. <- 자세한 것은 5강에서~~ <br>
        <br>

    * 8강 : Modern Convolutional Nerual Networks
        * AlexNet<br>
        &nbsp; - &nbsp; 당시 GPU가 부족했기 때문에 2개의 GPU에서 활용하고자 다음과 같이 2개로 나누는 전략을 선택함. <br>
        <img src='./img/alexnet1.png'>
        &nbsp; - &nbsp; 네트워크의 총 깊이는 8 layer이다. <br>
        &nbsp; - &nbsp; 그 당시 성공 요인<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; ReLU 사용 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; GPU 활용 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; local response normalization(지금은 많이 활용되지 않음), overlapping pooling <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Data augmentation <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Dropout <br>
        
        <br>

        * VGGNet<br>
        &nbsp; - &nbsp; 3 * 3 convolution filter만 사용한다. <br>
        &nbsp; - &nbsp; 1 * 1 convolution을 fully connected layer에 이용 <br>
        &nbsp; - &nbsp; dropout <br>
        &nbsp; - &nbsp;  왜 3 * 3 filter만 사용했을까? 아래의 그림을 예시로 설명을 하력고 한다. 둘 중 어느게 파라미터가 더 적을까?<br>
        <img src='./img/vggnet.png'>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 3 * 3을 2번 쓴 경우 : 3 * 3 * 128 * 128 * 2(2번 사용했으니까)  = 18 * 128 * 128<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 5 * 5 1번 쓴 경우 :  5 * 5 * 128 * 128 = 25 * 128 * 128<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 아래 그림과 같이 3 * 3을 2번 쓴 것과 5 * 5를 1번쓴 것에 사이즈는 같기 때문에 파라미터가 더 적은 3 * 3 filter를 2번 쓰는게 더 좋다. <br>
        <p align='center'><img src='./img/ex1.jpg' width=350></p>
        
        <br>

        * GoogleNet<br>
        &nbsp; - &nbsp; 1 * 1 convolution을 잘 활용한 방법 <br>
        &nbsp; - &nbsp; inception blocks이란 다음과 같이 input을 받은 후 퍼졌다가 다시 합쳐지는 모양을 가진다. 이때 1 * 1 convolution이 중요하다. <br>
        <img src='./img/inception_block.png'><br>
        <br>
        &nbsp; - &nbsp; 1 * 1 filter가 중요한 이유는 아래와 같이 1 * 1 filter를 거치고 3 * 3 filter를 적용하는게 더 파라미터가 적다. <- 이것덕분에 googleNet은 이전 기법들에 비해 layer가 깊지만 파라미터는 적게 가져간다.<br>
        <img src='./img/inception_block2.png'>
        <br>

        * ResNet<br>
        &nbsp; - &nbsp; 예전부터 많은 레이어를 쌓게 된다면 아래와 같이 학습이 제대로 이루어지지 못하여 성능이 좋지 않게 나온다. <br>
        <img src='./img/resnet1.png'>
        &nbsp; - &nbsp; 이 문제를 아래와 같이 resdual 방식으로 layer를 거쳐서 나온 학습결과(f(x))와 이전 값(x)을 더해준다. <br>
        <img src='./img/resnet2.png'>
        &nbsp; - &nbsp; 이 방식을 사용해주면 더 많은 layer를 가지고 있는 network를 이전 보다 더 학습을 잘 시켜줄 수 있다. <br>
        <br>
        <img src='./img/resnet3.png'>
        &nbsp; * &nbsp; batch norm의 위치에 대해서는 여러 이야기가 있는듯 하다(먼저 사용하는게 더 좋다. 아니다, 지금과 같은게 더 좋다 등).<br>
        <img src='./img/resnet4.png'>
        &nbsp; - &nbsp; 위의 그림처럼 그냥 3 * 3을 사용해주는게 아니라 1 * 1 filter로 채널의 수를 줄여서 3 * 3 convolutioin을 해주고 이후에 이전과 채널의 사이즈를 맞춰주기 위해서 1 * 1 filter로 채널을 늘려준다..<br>


        * DenseNet<br>
        &nbsp; - &nbsp; 이 방법의 핵심은 ResNet과 달리 이전값과 학습값을 더해주는 것이 아니라 붙여주면(concatenation) 어떨까 - 라는 것이 중요한 부분이다.  -> 붙여주면 붙여줄수록 채널의 사이즈가 증가하게 된다. <- 이러면 파라미터의 개수도 같이 증가하게 된다.<br>
        &nbsp; - &nbsp; 위의 문제를 해결하기 위해서 1 * 1 convolution을 이용해서 채널 사이즈를 줄여준다. <br>
        <img src='./img/densenet.png'>
        <br>
      


    

### 2. 과제 수행 과정 / 결과물 정리
<br>

#### 필수과제 MHA에 대해서 하는데 어려웠다 ㅠㅠ. 분명 강의를 통해서 차근차근 따라갔지만 이해가 잘 안되었다. 그래서 이 부분에 대해서 주말에 다시 한번 정리해야겠다.

<br>

### 3. 피어세션 정리
<br>
20210812 피어세션<br><br>

모더레이터: 박승찬<br><br>

회의록작성: 심우창<br><br>

📎[새로운 캠퍼님에게 그라운드룰 소개]<br><br>

모더레이터 순서에 대해서 소개(강진선 -> 김범수 -> 박승찬 -> 심우창 - 우원진 -> 최성욱 -> 배민환)<br>
코드리뷰를 위한 github 초대<br><br>
 

🔍[이전 질문 리뷰]<br><br>

이전 시간에 대한 질문은 당일날 해결해서 생략<br><br>
 

 

📒[금일 질문 목록]:<br><br>

* 선택과제 3번(승찬님이 하시다가 막히거나 잘 이해되지 않았던 부분)<br>
    * Gaussian mixture를 왜 사용하는지 그리고 어떻게 사용해야 하는지에 대해서 궁금하다.
    * 주어진 MDN class를 참고하여 과제를 수행했다. <- 이상한 값이 섞여서 나왔다.
        * 이유 : gaussian을 제대로 이용하지 못해서 그런 것 같다.
* 선택과제 3번 추가 질문
    * foward부분에서 shape를 어떻게 맞춰줬는지?
        * hidden layer로 들어가서 n_gaussians으로 나오기 때문에 이 부분을 통해서 shape를 맞춰줬다(코드상에 맞춰져 있었다).
    * 코드상에 x.mm이 무엇을 의미하는지? 
        * 행렬곱인것 같다.
* 선택과제 3번 참고 자료
    * 진선님이 참고하신 블로그(https://mikedusenberry.com/mixture-density-networks)
* 필수과제(MHA)에서 Q,K,V의 개수에서 K와 V는 같아야 되지만 Q는 달라도 된다 - 라고 하셨는데 이 부분이 잘 이해가 되지 않는다.
* 선택 과제에 대해서 해설 듣고 거기서도 이해가 안 되면 주말에 찾아보고 그것으로도 해결이 안되면 멘토님에게 물어보기 
* LSTM에서 update cell이랑 output gate가 이해가 잘 안되었습니다. 
    * forget gate : 이전의 hidden state와 가중치를 시그모이드 해준 결과이다.
    * input gate : 전 hidden state와 가중치를 시그모이드 해주고. hidden state에서 
    * update cell : 이전 cell state에서 다음으로 전달할 cell state구하는 방법으로 과거에 잊어버릴것(ft(이전 hidden state 시그모이드를 거친 값) * Ct-1(이전 cell state))은 잊어버리고 새로 기억할것(it(이전 hidden state 시그모이드를 거친 값) * Ct(hidden state가 tanh를 거친 값))은 기억하자
    * output gate : ot(이전 hidden state에서 시그모이드 거친 값) * (다음 cell state에서 tanh를 거친값)이다.
 <br><br>

* 📎[선택과제 정답 살펴보기]<br><br>

* 선택과제 3 - softmax함수 인자로 dim을 주는게 어떤 의미인가? 
    * softmax연산을 해당 dim을 기준으로 한다.
* 선택과제 1 - residual부분 -> 통합적인 구조를 만들고 싶을때 사용
* 선택과제 1 - attention list부분
* 선택과제 1 - encoder부분에서 MHA 후 norm하기 전 원래값 더해주는 부분



#### 내가 질문 했던 내용

#### Q. LSTM에서 update cell이랑 output gate가 이해가 잘 안되었습니다. 
#### A.     
    * forget gate : 이전의 hidden state와 가중치를 시그모이드 해준 결과이다.
    * input gate : 전 hidden state와 가중치를 시그모이드 해주고. hidden state에서 
    * update cell : 이전 cell state에서 다음으로 전달할 cell state구하는 방법으로 과거에 잊어버릴것(ft(이전 hidden state 시그모이드를 거친 값) * Ct-1(이전 cell state))은 잊어버리고 새로 기억할것(it(이전 hidden state 시그모이드를 거친 값) * Ct(hidden state가 tanh를 거친 값))은 기억하자
    * output gate : ot(이전 hidden state에서 시그모이드 거친 값) * (다음 cell state에서 tanh를 거친값)이다.

#### Q. 필수과제(MHA)에서 Q,K,V의 개수에서 K와 V는 같아야 되지만 Q는 달라도 된다 - 라고 하셨는데 이 부분이 잘 이해가 되지 않는다.
#### A. 해결 못 함.

<br><br>

### 4. 학습 회고

#### 오늘 강의 또한 집중해서 보지 않으면 잘 이해되지 않는 내용들이 많았다. 그래서 강의 정리하면서 강의를 한번 더 듣는다. 이러한 방식때문에 강의를 정리하는데 시간을 많이 소비하고 선택과제에 대해서는 많이 못하지만 어쩔 수 없는 것 같다. 일단, 1~2주 후에 있을 팀프로젝트에 도움이 되려면 기본기가 튼튼해야 될 것 같아서 부스트캠프에 메인부분만 잘 이해하고 따라갈 생각이다.

<br>

#### git에 대한 특강을 들었는데 github와 vscode에 대한 유익한 내용을 알 수 있어서 매우 좋았다. 이전까지는 terminal로 git clone, push, pull, fetch, merge등을 했는데 vscode의 palette와 git graph를 이용하면 좀 더 쉽게 할 수 있다는 것을 알 수 있어다. 또 github issue에 용도에 대해서는 알고 있었지만 오늘 설명을 통해서 좀 더 알 수 있어서 좋았다.
<br>

#### 피어세션에서는 선택과제 3에 대해서 많은 이야기를 했다(물론 나는 듣기만 했다 ㅎㅎ;). 이번주는 메인 내용에 대한 완벽한 이해를 목표로 하고 있어서 피어세션에서는 주로 듣거나 궁금한 것에 대해서 가끔 질문정도 할 것 같다.
<br>

#### 그리고 새로운 캠퍼분이 우리조로 배정이 되셨다. 앞으로 4주간 잘 지내서 팀프로젝트 때 다 같이 좋은 결과를 얻었으면 좋겠다 ㅎㅎㅎㅎ

<br>

#### 질문게시판에 글을 읽으면서 여러 질문에 대해서 생각해볼 수 있어서 가끔씩 질문게시판에 들어가서 눈팅하려고 한다. 그리고 내가 아는 것에 대해서는 답을 하려고 하지만 대부분 잘 모르는 내용들이었다 ㅎㅎ; 

<br>

#### 오늘도 즐거운 하루였다~~~~~ㅎㅎㅎㅎㅎㅎㅎㅎ 