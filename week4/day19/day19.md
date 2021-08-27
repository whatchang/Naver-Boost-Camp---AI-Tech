<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 19 이미지 분류 9~10 강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [Competition](#2-Competition)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* 이미지 분류 9~10강
    * 9강 : Training
        * Loss<br>
       &nbsp; - &nbsp; 복습 : error backpropagation<br>
       <img src='./img/loss.png'><bt>
       &nbsp; - &nbsp; loss에 대한 것도 nn.패키지에 구현이 되어있다.<br>
       &nbsp; - &nbsp; 관용적으로 criterion에 loss 함수를 정의해 주고 input값에 forward 결과와 실제값을 넣어줘서 loss를 구해주고 loss.backward()를 해주면 backpropagation이 진행된다. -> 이것이 가능한 이유는 pytorch의 경우 forward를 해주면 input부터 시작해서 각 모듈들을 지나 output가지 체인이 형성이 되는데 이것을 criterion에 input으로 줘서 만들어진 loss또한 같은 체인을 갖고 있게 되고 이 체인을 이용했기 때문에 backpropagation이 가능한 것이다.<br>
       &nbsp; - &nbsp; 특별한 loss들<br>
       &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Focal Loss : Class Imabalance문제가 있는 경우, 맞출 확률이 높은 class는 조금의 loss를 맞추기 어려운 classsms loss를 높게 부여한다. -> 즉 class의 분포정도에 따라 loss에 가중치를 두자는 것!<br>
       &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Label smoothing loss : class target label을 onehot ㅠㅛ현으로 사용하기 보다는 조금 soft하게 표현해서 일반화 성능을 높이기 위함. -> [0, 1, 0, 0, ...] -> [0.025, 0.025, 0.9, 0.025, ...]<br>
       <br>

       * optimizer<br>
       &nbsp; - &nbsp; loss가 0인 부분을 찾기 위해서 어느 방향으로 얼마나 움직일지를 정한다.<br>
       &nbsp; - &nbsp; StepLR : 특정 step마다 LR감소<br>
       &nbsp; - &nbsp; CosineAnnealingLR : Cosine 함수 형태처럼 LR을 급격히 변경한다.<br>
       &nbsp; - &nbsp; ReduceLROnPlateau : 더 이상 성능 향상이 없을때 LR 감소<br>
        <br>

        * metric : 모델이 일반적으로 봤을때 성능이 어느정도인지 정의하기 위해서 사용한다. <br>
        &nbsp; - &nbsp; 모델의 평가 - 학습에 직접적으로 사용되는 것은 아니지만 학습된 모델을 객관적으로 평가할 수 있는 지표가 필요하다.<br>
        <img src='./img/metric.png'>
        &nbsp; - &nbsp; 모델의 정확도를 평가할때 해당 target의 class 분포에 따라서 적용하는 방식을 달리해야 할때가 있다. 이때는 단순히 맞은 개수를 전체 개수로 나누는게 아니라 적은 각 class별로 어느 정도 맞췄는지, 그것을 평균내면 전체적으로 어느정도 맞췄는지를 평가하는 지표를 사용해야 한다.<br>

       <br>

    * 10강 : Inference
        * Computer Vision의 발전<br>
        &nbsp; - &nbsp; ImageNet 대회의 질 좋은 데이터가 computer vision에서 획기적인 알고리즘 개발을 위한 토대가 되었다.<br> 
        <img src='./img/imagenet.png'>
        <br><br>

        * pretrained model<br>
        &nbsp; - &nbsp; 모델의 일반화를 위해 매번 수 많은 이미지를 학습시키는 것은 어렵고 비효율적이다. -> 그렇기 때문에 좋은 품질의 데이터로 대량으로 학습된 모델을 이용하자! -> 이 모델을 우리의 목적에 맞게 잘 다듬자.<br>
        &nbsp; - &nbsp; torchvision.models를 이용해서 손쉽게 pretrained 모델과 weight를 가져올 수 있다.<br>

        <br>

        * transfer learning : 우리 목적에 맞게 pretrained model 사용하기<br>
        &nbsp; - &nbsp; ex) CNN pretrained model을 가지고 설명<br>
        <img src='./img/ex_cnn1.png'>
        &nbsp; - &nbsp; 위와 같이 pretrained model이 backbone + classifier로 구성이 되어 있다고 가정하자<br>
        &nbsp; - &nbsp; 그리고 위의 모델은 어떤 문제를 해결하기 위해 classifier에서 어떤 카테고리를 output해주는지 내가 해결하기 위한 카테고리가 이 모델이 해결하고자 하는 문제에 겹치는 부분이 많은지 등을 생각해야 한다. -> pretraining할 때 설정했던 문제와 현재 문제와의 유사성을 생각해봐야 한다.<br>
        &nbsp; - &nbsp; 이때 아래와 같이 case별로 전략을 짜면 좋다.<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; 문제를 해결하기 위한 데이터가 충분하다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1-1. &nbsp; 해결하고자 하는 문제가 pretrained model과 유사하다. -> backbone은 freeze해주고 classifer만 학습시켜주면 된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1-2. &nbsp; 해결하고자 하는 문제가 pretrained model과 유사하지 않다. -> backbone ~ classfier를 학습시켜줘야한다.<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 문제를 해결하기 위한 데이터가 충분하지 않을 경우.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2-1. &nbsp; 해결하고자 하는 문제가 pretrained model과 유사하다. -> backbone은 freeze해주고 classifer만 학습시켜주면 된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2-2. &nbsp; 해결하고자 하는 문제가 pretrained model과 유사하지 않다. -> pretrained model을 사용하지 않는게 좋다. -> 새로운 모델을 만들어서 사용하거나 다른 pretrained model을 찾아야 한다.<br>
        
        

        <br>
    

### 2. Competition
<br>

####  어제 undersampling과 그것을 바탕으로 좌우 30도 범위 내에서 회전 시킨 이미지를 추가한 data를 가지고 학습을 시켜보았다. 학습시킨 모델을 가지고 평가한 후 csv파일을 만들어서 가장 좋은 성능이 나왔던 csv랑 비교를 해 보았다. 주로 나이와 성별부분에서 차이가 있었다. 예를 들어서 60이상인 것처럼 보이는데 나의 모델은 30이상 60이하로 평가하였고 여성인데 남성으로 평가하는 등 이런 부분에서 차이가 있었고 생각보다 마스크에 관련된 부분에서는 큰 차이를 보이지 않았다. 
#### *TMI이지만 이때 차이가 나는 부분에 대해서 어떻게 비교를 해냤면 해당 파일명의 이미지를 직접보고 내 생각에 어떤 카테고리에 들어갈지 평가를 하면서 내 모델의 예측과 성능이 좋았던 모델의 예측에 어떤 차이가 있는지 비교해 보았다.

<br>

#### 그리고 매우 신기했던게 undersampling한 후 data augmentation을 적용한 것보다 undersampling한게 더 효과적인 것 같았다.

#### 우선 마지막으로 내 모델에 undersampling한 데이터를 적용해서 5-fold에서 epoch 4정도 적용하여 생성한 model이 예측한 값만 본 후에 괜찮은 것 같으면 제출하고 아니면 바로 다른 캠퍼님의 모델을 가지고 undersampling data를 활용하여 학습시킬 예정이다.
<br>

#### 추가적으로 가장 높은 점수 받은 csv파일과 자신의 모델이 예측한 값이 어떤 부분이 다른지 보여주는 코드를 작성해볼 생각이다.


### 3. 피어세션 정리
<br>
20210826 피어세션

🔍[마스크 데이터 분류 대회]

* 다양한 시도

    * VGG → DenseNet활용하여 성능 증가
    * Crop만 진행 → 성능 증가 x
    * ResNet50활용 (Parameter의 수를 봤을 때, 적절한 것 같다)
    * Crop진행 → Shape의 문제 발생 → Shape이 같아야 Batch를 뽑아올 수 있는 것으로 보이나 어떻게 Shape을 맞춰줘야 하는지에 대해서는 미지수.
    * ResNext50_32x4d 활용
    * 얼굴 위치에 대한 분포도를 바탕으로 평균, 분산을 활용하여 적당한 Crop 진행 → 얼굴이 해당 위치에 있었으면 했지만 잘 나오지는 않음
    * 전처리를 활용하여 주름을 구분해낼 수 있다.(Contrast, Sharpness, Brightness, Color)


* 해 볼 시도

    * OverSampling
    * SMOTE → 직접 적용하기에 어려움이 있지만 시도 해볼 것이다.
    * Label이 작은 것을 랜덤 복제하여 Sampling 시도


* 질답

KFold는 Data 수가 너무 적을 때, Validation Set의 Robustness를 주기 위해서 활용하는 방안인데 코드에 직접 입력할 때 성능의 개선이 이루어졌다. 왜 그럴까?
<br><br>
→ 이전 Fold에서의 개선된 Parameter가 다음 Fold로 이어짐으로서 성능 향상을 나타낸다.
<br><br>
Gradient Accumulation에서 Num_Accum으로 loss를 나누어주게 되는데, 왜 이렇게 하는가?
<br><br>
→ 이유 모색 후 토의
<br><br>
Brightness & Contrast를 활용하여 배경을 아예 흰색으로 만들 수 있지 않을까?
<br><br>
→ 일정 임계값 이하일 경우, 배경이 검은색이라면 얼굴이 날아갈 위험이 있다.
<br><br>
Focal Loss 직접 활용해 보았는가?
<br><br>
→ Weight를 직접 조정할 수 있는데 이것이 Focal Loss의 방법과 유사한 것 같다.
<br><br>
서버에서 깃헙으로 바로 업로드하는 방법이 있는가?
<br><br>
→ 기존의 방식에서 조금 변화가 있어, 이제는 token을 입력해주면 서버에서 깃헙으로 업로드 할 수 있다.
<br><br>
코드 리뷰
<br><br>
원진님, 우창님, 성욱님, 승찬님, 범수님



<br><br>

### 4. 학습 회고

#### 오늘 피어세션때는 다양한 data augmentation에 대해서 적용한 코드와 강의에 관련된 질문, 팀 회고록등을 했었다. 
<br>

#### 강의와 관련된 질문에서는 복습의 중요성에 대해서 깨달게 되었다. 오늘부터 복습을 실천해야 하지만 음... 하하;;; 노... 노력해봐야겠다!

<br>

#### 코드 리뷰에서 이미지를 ratete할때 짤리는?채워 넣어야 하는 영역을 최대한 원본의 이미지와 비슷하게 만들어주는 함수를 알게 되었다. 또 data augmentation을 할 때 회전 말고도 어떤식으로 할지에 대한 생각들을 공유받을 수 있어서 매우 유익한 시간이었다.

<br>

#### 팀회고록때에는 나만 힘든게 아니였구나 - 를 느낄 수 있었고 그러면서 다른 캠퍼님들의 열정도 함께 느낄 수 있어서 나에게 새로운 자극을 준 것 같다. 

<br>

#### 이번 주 정말 수고 많았고 주말에 쉬면서 파이썬 프로젝트 및 팀 회고록때 계획했던 도전들을 시도해 보자~!!! 화이팅~~~!!!

