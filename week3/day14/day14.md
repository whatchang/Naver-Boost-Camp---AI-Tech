# Day 14 Pytorch 8~19 강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Pytorch 8~10강
    * 8강 : Multi-GPU
        * 개요<br>
        &nbsp; - &nbsp; 모델들이 점차 발전함에 따라 필요한 데이터의 개수와 학습시킬 파라미터의 양이 기하급수적으로 늘고 있다. -> 하드웨어의 발전보다 더 빠르게 늘고 있기 때문에 한개의 gpu보다는 여러 개의 gpu를 가지고 학습시키는게 좋다 <br>
        &nbsp; - &nbsp; 그렇다면 이런 멀티 gpu를 이용하는 방법은 어떤게 있을까?<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; model을 병렬화 시키는 방법 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 데이터를 병렬화 시키는 방법 <br>
        <br>

        * Model parallel <br>
        &nbsp; - &nbsp; alexnet방식때부터 사용한 방식(<- 당시 최고성능의 gpu memory가 4~8G였다고 함>) <br>
        &nbsp; - &nbsp; 문제점 : 모델의 병목, 파이프라인의 어려움 <- 해결하기 어려운 고난이도 문제이다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 좋은 병렬처리란 다중 시분할 시스템과 다르게 겹치는 부분이 있어야 좋은 것이다. <- 시분할 시스템인 경우 1개를 가지고 여러 작업을 하는 거라서 겹칠 수 가 없지만 multi-gpu는 여러개를 가지고 여러개의 작업을 하므로 시간의 흐름에 따라 동시에 처리되는 일들이 많아야 좋은 것이다. + 각 gpu에서 수행한 작업의 결과물들을 다른 gpu에게 줌으로써 학습을 하는데 지장이 없어야 한다.<br>

        <br>

        * Data parallel <br>
        &nbsp; - &nbsp; 데이터를 나눠 GPU에 할당후 결과의 평균을 취하는 방법 <br>
        &nbsp; - &nbsp; minibatch 수식과 유사한데 한번에 여러 GPU에서 수행한다. <br>
        &nbsp; - &nbsp; 동작 방식 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; 데이터를 여러 gpu에게 나눠서 할당 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 각 gpu에 모델을 복사해준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 3. &nbsp; 각 gpu에 연산을 시켜준다.  <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 4. &nbsp; 연산의 결과를 하나의 gpu로 모아준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 이렇게 하나의 gpu에 연산 결과를 모아주는 이유 : 파이썬의 multi-processing 제약사항때문이다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 5. &nbsp; 4에서 받은 각 loss값들에 대해서 각 gradient값들을 구해준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 6. &nbsp; 각 gradient에 대해서 해당 gpu에게 전달 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 7. &nbsp; 각 gpu들은 backward를 실행해준다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 8. &nbsp; 나온 결과를 다시 하나의 gpu에 모아준 후 평균을 취해준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; forward : 1~4번 과정<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; backward : 5~8번 과정<br>
        &nbsp; - &nbsp; Data parallel의 문제점 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 단순히 데이터를 분배한 후에 평균을 취해주는 과정이므로 GPU 사용 불균형 문제와 Batch 사이즈 감소가 된다. <위에서의 예시로는 분배하고 취합해주는 gpu가 더 많은 시간을 사용한다. 그리고 한 gpu가 조금 더 많이 사용하므로써 메모리도 더 사용하게 되므로 다른 gpu중에 batch size가 작은 것이 생기고 이 gpu를 기준으로 batsize를 설정해야 되므로 batch size가 줄어들게 된다)<br>
        &nbsp; - &nbsp; 위의 문제를 해결?하는 방식이 distributed data paralle이다. <- 위의 동작 방식보다 구현이 좀 더 어려움<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 위의 과정에서 하나의 gpu가 gradient를 계산하는게 아니라 각 gpu에서 gradient를 계산해주고 평균을 내준후 하나의 gpu로 취합해주는 것 같다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 좀더 찾아보니까 distributed data parallel(DDP)는 data parallel(DP)보다 더 적은 개수의 모델의 layer를 쌓아도 똑같은 동작을 수행하는 것 같다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; [참고한 사이트](https://algopoolja.tistory.com/56) <- 이 글의 비교 표 부분의 예시를 위의 설명할때 참고했다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; [나중에 코드로 실제 구현할때 참고해 보면 좋을 것 같은 사이트](https://medium.com/daangn/pytorch-multi-gpu-%ED%95%99%EC%8A%B5-%EC%A0%9C%EB%8C%80%EB%A1%9C-%ED%95%98%EA%B8%B0-27270617936b)<br>
        &nbsp; - &nbsp; 사용방법 <br>

                step 1 : sampler 만들기
                ex)
                train_sampler = torch.utils.data.distributed.DistributedSampler(train_data)
                shuffle = False
                pin_memory = True
                trainloader = torch.utils.data.DataLoader(train_data, batch_size=20, shuffle=True, pin_memory=pin_mempory, num_wokers=3, shuffle=shuffle, sampler=train_sampler)
                
                step2 : torch.multiprocessing.spawn을 통해서 <- 이 부분부터 다시 작성하기

                step 3 : 멀티프로세싱 통신 규약 정의하기
                torch.distributed.init_process_group(backend='nccl', init_method='tcp://127.0.0.1:2568', world_size=gpu 개수, rank=gpu)

                step 4 : DDP 정의
                1. gpu 선택

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

    * 9강 : Monitoring tools for Pytorch
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

    * 10강 : Monitoring tools for Pytorch
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

####  오전 11시까지 과제를 도전해 봤지만 잘 안되었다 ㅠㅠ

#### 내일까지 다른 캠퍼님 코드랑 답지를 참고하면 공부해야겠다~~!!!

<br>

### 3. 피어세션 정리
<br>
20210820 피어세션

🔍[팀 회고록 정리]

* 각자 회고록을 조금의 시간을 갖고 작성했다.
* 각자 잘했던것, 아쉬운것, 도전할것을 발표하는 시간을 가졌다.


📒[스페셜 피어세션]

* 다른 팀들 중 참고할만한 것 - 하루의 TODO 리스트를 만들어 각자 slack에 공유하기


🔍[그외에 한일]

* 다음주 목요일까지 ViT 논문을 읽고 피어세션과 멘토링 시간에 리뷰하기
* CV, NLP 도메인에 대한 이야기를 깊게 나누었다.



<br><br>

### 4. 학습 회고

#### 오늘 오전에는 필수 과제2를 해결하기 위해서 모든 시간을 투자를 하였고 결국 ㅠㅠ 해결하지 못 해서 주말에 다시 해볼 생각으로 넘어가고 오후부터 강의를 들었다.

<br>

#### 강의 내용 자체는 어렵지 않았고 교수님께서 설명을 잘 해주셔서 편안하게 들을 수 있었다 ㅎㅎ

<br>

#### 스페셜 피어세션때는 다른 팀과 만나 자기 소개 -> 관신 분야 -> 팀 자랑 거리 등을 이야기하면서 즐거운 시간을 보냈다. 이야기를 들으면서 느낀 거지만 음.... 다들 공부에 대한 열정이 대단하다 - 라고 생각했다. 

<br>

#### 피어세션때는 저번주 금요일과 같이 팀회고록을 했는데 서로에 대해서 좀 더 알아가는 것 같아서 좋았다. 그리고 다음번에 진행할 논문에 대해서도 이야기를 했고 이번에는 꼭 미리 열심히 공부해서 정보를 공유할 수 있는 자료? 아니면 발표? 등을 통해서 팀원들에게 도움이 되어야겠다! 
#### + to do list에 대해서 slack에 공유하기로 했다. 내 할 일을 미루지 않도록(게을러지지 않도록) slack에 올려서 스스로 하게끔 만들어야겠다 ㅎㅎ
<br>

#### 오늘부터는 할 것이 있더라도 너무 급한것이 아니면 2시 이전에 자고 다음날 8시 30분에 일어나서 전날 못했던 것을 이어서 할 생각이다. 왜냐하면 이번에 잠을 너무 줄였더니 피곤이 누적되서 학습과 과제를 하는데 영향을 크게 미쳤기 때문이다 ㅠㅠ
<br>

#### 주말에 할 것
- 강의 내용 정리(만약에 밀렸으면) 
- transformer 공부한 것 정리 
- 시각화 강의 듣기 및 내용 정리하기 
- 2강 내용에서 프로젝트 디렉토리에 대한 상관관계?를 그림으로 그려서 day11 보강하기
- 필수과제 한번 더 보고 내용 정리하기
- 운영진님 운영하시는? 모각코 참여하기

#### 적어넣고 보니까 생각보다 주말에 할게 많다 ㅎㅎ;;; 
#### 일단 오늘의 내가 하는게 아니니까 상관없다~😃

<br>

#### 내 자신아 이번 주 고생많았어~~~ 그런 의미로 주말에도 조금만 더 고생하자 ㅎㅎㅎㅎ
#### 오늘의 나는 못 할것 같지만 내일의 너는 할 수 있어!!! You can do it!😝

<br>

#### TMI - 우리 팀에 이전에 만났던 사람들이 있어서 신기신기! 크으~~~ 역시 우리팀~!😆