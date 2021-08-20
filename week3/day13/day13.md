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
    * 6강 : 모델 불러오기
        * 개요<br>
        &nbsp; - &nbsp; 학습 결과를 공유하기 위해! <br>
        <br>

        * model.save() <br>
        &nbsp; - &nbsp; 학습의 결과를 저장하기 위한 함수 <br>
        &nbsp; - &nbsp; 모델 형태(architecture)와 파라메터를 저장 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 모델 형태 말고 파라메터만 저장시 적은 용량으로 비슷하게 구현할 수 있다. 모델 형태로 저장하면(파라메터에 비해 용량 좀 차지함) 따로 구현할 필요없이 해당 모델을 가져다 사용하면 된다.<br>
        &nbsp; - &nbsp; 모델 학습 중간 과정의 저장을 통해 최선의 결과모델을 선택 <br>
        &nbsp; - &nbsp; 만들어진 모델을 외부 연구자와 공유하여 학습 재연성 향상 <br><br>
        
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; model.state_dict() : 모델의 파라메터를 표시<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 모델 저장시 확장자는 주로 .pt로 많이 사용한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; torch.load()를 통해서 path 인자에 해당하는 모델 파일을 불러온다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; model.state_dict()로 해당 모델의 파라미터를 확인할 수 있지만 torchsummary를 이용하면 좀 더 깔끔하게? 볼 수 있다.<br>

        <br>

        * checkpoints <br>
        &nbsp; - &nbsp; 학습의 중간 결과를 저장하여 최선의 결과를 선택하기 위해서 사용하는 방식 <br>
        &nbsp; - &nbsp; earlystopping 기법 사용시 이전 학습의 결과물을 저장 <br>
        &nbsp; - &nbsp; loss와 metric 값을 지속적으로 확인 저장 <br>
        &nbsp; - &nbsp; 일반적으로 epoch, loss, metric을 함께 저장하여 확인하는 방식 <br>
        &nbsp; - &nbsp; colab에서 지속적인 학습을 위해 필요하다.<br>
        &nbsp; - &nbsp; 저장하는 방식 <br>

                torch.save({
                    'epoch' : epoch 변수
                    'model_state_dict' : model.state_dict(),
                    'optimizer_state_dict' : optimizer.state_dict()
                    'loss' : loss 변수
                },
                f'saved/checkpoint_model_{e}_{epoch_loss/len(dataloader)}_{epoch_acc/len(dataloader)}.pt')

            &nbsp; - &nbsp; 저장하는 방식 <br>

                checkpoint = torch.load(모델 파일 경로)
                model.load_state_dict(checkpoint['model_state_dict' < - 위에서 저장할 때 지정할 문자 포맷])
                model.load_state_dict(checkpoint['optimizer_state_dict'])
                epoch = checkpoint['epoch']
                loss = checkpoint['loss']

        * Pretrained model & transfer learning<br>
        &nbsp; - &nbsp; transfer learning <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 다른 데이터셋으로 만든 모델을 현재 데이터에 적용<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 일반적으로 대용량 데이터셋으로 만들어진 모델의 성능이 높다. <br>  
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 현재의 DL에서는 가장 일반적인 학습 기법 <br>  
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; backbone architecture가 잘 학습된 모델에서 일부분만 변경하여 학슴을 수행한다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 멘토님께서 다음주 있을 대회에서 '2.기본적으로 pretrained model을 사용하는데 제한은 없다고 합니다.(이부분은 대회마다 조금씩 달라질 수 있다고하네요)' 라고 알려주셨는데 음... 그러면 이 부분의 내용을 잘 듣고 대회때 활용해 봐야겠다! <br><br>
        &nbsp; - &nbsp; Freezing : pretrained model을 활용시 모델의 일부분을 frozen 시킨다. <- 다른 사람의 모델을 자신의 데이터에 맞게끔 특정 layer부분만 학습시키는 방식<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 가져온 모델에 대해서 자신이 새로 layer를 추가할 수 도 있다. <- 이때 일반적으로 모델을 직접적으로 수정하지 않고 복사를 하여 사본에 변형을 준다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 모델 저장시 .pht를 지양하는게 좋다. <- 기존의 사용하는 확장자이므로 <br>
               

        <br>

    * 7강 : Monitoring tools for Pytorch
        * 개요<br>
        &nbsp; - &nbsp; 모델을 학습하기 위해서는 일반적으로 긴 학습 시간이 필요하다. 이러한 긴 시간의 학습을 기록들을 모니터링하기 위해서 Tensorboard와 weight & biases(wandb)를 사용한다.<br> 
        <br>

        * Tensorboard<br>
        &nbsp; - &nbsp; TensorFlow의 프로젝트로 만들어진 시각화 도구 <br>
        &nbsp; - &nbsp; 학습 그래프, metric, 학습 결과의 시각화 지원 <br>
        &nbsp; - &nbsp; pytorch도 연결 가능 -> DL 시각화 핵심 도구 <br>
        &nbsp; - &nbsp; tensorboard에서 저장하는 값 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; scalar : metiric(accurancy, loss 등의 지표) 등 상수 값의 연속(epoch)을 표시<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; graph : 모델의 computational graph 표시 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; histogram : weight 등 값의 분포를 표현<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; image : 예측 값과 실제 값을 비교 표시<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; mesh : 3d 형태의 데이터를 표현하는 도구<br><br>
        &nbsp; - &nbsp; Tensorboard를 사용하기 위한 준비 단계 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; Tensorboard 기록을 위한 디렉토리 생성 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 기록 생성을 위한 SummaryWriter isstance 생성 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 3. &nbsp; 기록하기 위한 함수들을 이용하여 값을 기록 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 4. &nbsp; %load_ext tensorboard과 %tensorboard  --logdir {logs_base_dir}을 이용하여 juptyer와 같은 notebook형태에서 tensorboard 수행 <- logs_base_dir은 해당 값이 쓰여진 directory path를 뜻한다. <br>

        <br>

        * weight & biases<br>
        &nbsp; - &nbsp; 머신러닝 실험을 원할히 지원하기 위한 상용도구 <br>
        &nbsp; - &nbsp; 협업, code versioning, 실험 결과 기록 등을 제공한다.<br>
        &nbsp; - &nbsp; MLOps의 대표적인 툴로 저변 확대하는 중이다.<br>
        &nbsp; - &nbsp; wandb를 사용하기 위한 준비 단계 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; [https://wandb.ai/site](https://wandb.ai/site) 에 가입후 API 키 확인하기 <- 개인 정보에 settings에 보면 확인 할 수 있다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 새로운 프로젝트 생성하기 <- 이때 이름 기억할 필요가 있다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 3. &nbsp; pip 혹은 anaconda로 wandb 패키지 설치 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 4. &nbsp; config 설정 (변수 초기화 및 wnadb.init()에 config파라미터에 초기화한 변수를 넣어준다. + 위에서 만든 프로젝트명 + entity명 등도 추가로 전달해준다.) <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 5. &nbsp; wandb.log()를 통해서 기록 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 6. &nbsp; 위의 사이트에서 위에서 만든 프로젝트에 가면 기록을 볼 수 있다. <br>
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