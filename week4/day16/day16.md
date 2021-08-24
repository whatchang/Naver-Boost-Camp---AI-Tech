# Day 16 이미지 분류 강

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
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; forward : 1 ~ 4번 과정<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; backward : 5 ~ 8번 과정<br>
        &nbsp; - &nbsp; Data parallel의 문제점 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 단순히 데이터를 분배한 후에 평균을 취해주는 과정이므로 GPU 사용 불균형 문제와 Batch 사이즈 감소가 된다. <위에서의 예시로는 분배하고 취합해주는 gpu가 더 많은 시간을 사용한다. 그리고 한 gpu가 조금 더 많이 사용하므로써 메모리도 더 사용하게 되므로 다른 gpu중에 batch size가 작은 것이 생기고 이 gpu를 기준으로 batsize를 설정해야 되므로 batch size가 줄어들게 된다)<br>
        &nbsp; - &nbsp; 위의 문제를 해결?하는 방식이 distributed data paralle이다. <- 위의 동작 방식보다 구현이 좀 더 어려움<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 위의 과정에서 하나의 gpu가 gradient를 계산하는게 아니라 각 gpu에서 gradient를 계산해주고 평균을 내준후 하나의 gpu로 취합해주는 것 같다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 좀더 찾아보니까 distributed data parallel(DDP)는 data parallel(DP)보다 더 적은 개수의 모델의 layer를 쌓아도 똑같은 동작을 수행하는 것 같다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; [참고한 사이트](https://algopoolja.tistory.com/56) <- 이 글의 비교 표 부분의 예시를 위의 설명할때 참고했다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; [나중에 코드로 실제 구현할때 참고해 보면 좋을 것 같은 사이트](https://medium.com/daangn/pytorch-multi-gpu-%ED%95%99%EC%8A%B5-%EC%A0%9C%EB%8C%80%EB%A1%9C-%ED%95%98%EA%B8%B0-27270617936b)<br>
        &nbsp; - &nbsp; 사용방법 <br>

                ex)

                step 1 : sampler 만들기
                train_sampler = torch.utils.data.distributed.DistributedSampler(train_data)
                shuffle = False
                pin_memory = True
                trainloader = torch.utils.data.DataLoader(train_data, batch_size=20, shuffle=True, pin_memory=pin_mempory, num_wokers=3, shuffle=shuffle, sampler=train_sampler)
                
                step2 : torch.multiprocessing.spawn에 우리가 멀티프로세싱 처리를 할 함수와 gpu 개수, 등을 인자로 넘겨주고 함수에서 처리하는데 필요한 argument들도 넣어준다.

                step 3 : 멀티프로세싱 통신 규약 정의하기
                torch.distributed.init_process_group(backend='nccl', init_method='tcp://127.0.0.1:2568', world_size=gpu 개수, rank=gpu)

                step 4 : DDP 정의
                torch.nn.parallel.DistributedDataParallel함수를 통해서 DDP를 정의해주면 된다.
               
        <br>

    * 9강 : Hyperparameter Tuning
        * 개요<br>
        &nbsp; - &nbsp; 좋은 성능을 내기 위해서 좋은 모델과 좋은 데이터의 적당한 양을 가지고 학습을 시킨 후 마지막으로 성능을 올릴 수 있는 방법 중에 하나가 바로 'Hyperparameter Tuning'입니다. <br> 
        <br>

        * Hyperparameter Tuning<br>
        &nbsp; - &nbsp; 모델 스스로 학습하지 않는 값은 사람이 지정 -> ex. learning rate, 모델의 크기, optimizer 등 <br>
        &nbsp; - &nbsp; hyperparameter에 의해서 성능이 크게 좌우될 때도 있었지만 요즘은 큰 폭은 아니지만 어째든 조금이라도 성능에 영향을 준다. <- 마지막까지 최선을 다하기 위해서는 사용해야 한다. <br>
        &nbsp; - &nbsp; Hyperparameter tuning 방식 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; Grid : hyperparameter의 값의 범위를 일정범위 기준으로 나눠서 찾는 방법.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; Random : hyperparmeter의 값을 무작위로 선택해서 찾는 방법.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; 예전에는 Random 방식을 이용해서 성능이 잘 나오는 구간의 hyperparameter 범위를 찾아주고 그 구간에서 grid를 이용해서 찾아주는 방식을 많이 사용했다고 한다. <- 지금은 베이지안 기법들을 주로 많이 사용한다고 함(<- 논문 이름 : BOHB) <br>

        <br>

        * Ray<br>
        &nbsp; - &nbsp; multi-node multi processing 지원 모듈 <br>
        &nbsp; - &nbsp; ML/DL의 병렬 처리를 위해 개발된 모듈<br>
        &nbsp; - &nbsp; 기본적으로 현재의 분산병렬 ML/DL 모듈의 표준<br>
        &nbsp; - &nbsp; Hyperparameter Search를 위한 다양한 모듈 제공 <br>
        &nbsp; - &nbsp; 사용 방법 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; config에 search space를 지정해 준다. <- 찾고자 하는 hyperparameter와 값의 범위 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 학습 스케줄링 알고리즘 지정<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 3. &nbsp; 결과 출력 양식 지정 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 4. &nbsp; 병렬 처리 양식으로 학습 시행 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; Ray와 tensorboard, wandb를 같이 사용하면 눈으로 보기 용이하다. <- 함께 사용하는 것을 권장<br><br>
        
        * 조금 더 알아보기<br>
        &nbsp; - &nbsp; 4학년 1학기때 했던 프로젝트에서는 Optuna라는 모듈을 사용해서 hyperparameter를 찾았는데 Ray와 Optuna는 어떻게 다른 걸까? 그리고 어떤 상황에서 어떤 것이 더 좋을까? <br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; 0. &nbsp; 들어가기에 앞서서 알아야 하는 부분<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; Ray를 hyperparameter를 찾기 위한 모듈로 사용하는 이유는 hyperparameter를 찾는 방식 자체가 여러 값들을 대입해 보고 성능이 어떻게 나왔는지 파악하면서 최고의 성능을 찾는 방식이기 때문이다. 즉, 다시 말해서 값만 다르게 하고 찾는 알고리즘을 동일하게 줘서 병렬적으로 처리를 해주면 된다는 말이다. <- 그래서 Ray를 multi processing 지원 모듈이라고 소개한 것 같다.<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; 어떻게 다를까?<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; Ray는 HyperParameter Optimization Library들이 병렬적으로 일을 처리해줄 수 있게 도와주는 역할을 하는 것 같다(<- 제가 글을 읽고 이해한 것을 바탕으로 적은 것이기 때문에 아닐 수도 있습니다). 그렇기 때문에 optuna를 병렬적으로 돌려서 hyperparameter를 찾고 싶다면 ray를 이용하면 되지 않을까 싶다.<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 어떤 상황에서 어떤 것이 더 좋을까?<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; 이 부분은 TMI이고 정확하지 않지만 블로그와 여러 사이트를 참고한 결과 Tune과 RaySGD를 사용하는 것이 좋아보인다.
        왜냐하면 Tune같은 경우는 High level HPO로 low level인 HyperOpt와 Optuna를 내부적으로 import하여 사용하고 있고 이것들을 통합하여 Ray core위에서 분산/병렬화를 가능하게 해주기 대문이다. 또 RaySGD는 DDP를 위한 Ray기반 Library인며 tensoflow와 pytorch와 같은 framwork에서도 쉽게 통합 가능하며 Tune과 같은 HPO와도 통합되어 사용될 수 있기 때문이다.
        <br>
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 참고한 사이트 <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; [주로 여기서 ray에 대한 개념 및 역사 등을 알 수 있었습니다.](https://riiidtechblog.medium.com/ray-%ED%99%95%EC%9E%A5-%EA%B0%80%EB%8A%A5%ED%95%9C-%EA%B3%A0%EC%84%B1%EB%8A%A5-%EB%B6%84%EC%82%B0-%EB%B3%91%EB%A0%AC-machine-learning-%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC-f17f9c9cbef3)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; [Ray 사용법에 대해서 참고하면 좋을 것 같은 사이트 - 변성윤 마스터님 블로그 입니다.](https://zzsza.github.io/mlops/2021/01/03/python-ray/)<br>
        <br>

    * 10강 : Pytorch Troubleshooting
        * 개요<br>
        &nbsp; - &nbsp; OOM(Out Of Memory) : 대량의 메모리를 이용할 경우 시스템의 메모리가 부족할 경우 os에 따라 프로그램을 강제로 종료하는 경우가 발생하는데 이러한 것을 OOM이라고 한다.<br> 
        &nbsp; - &nbsp; OOM을 해결하기 어려운 이유들<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 왜 발생했는지 알기 어렵다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 어디서 발생했는지 알기 어렵다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Error backtracking이 이상한데로 간다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 메모리의 이전상황의 파악이 어렵다. <br>
        <br>
        &nbsp; - &nbsp; OOM 해결 방안<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Batch size를 줄인다. -> GPU를 clean해준다. -> Run <br>
        <br>

        * 그 외에 발생할 수 있는 문제들 해결하는 방법<br>
        &nbsp; 1. &nbsp;GPU Util 사용하기 : iter나 epoch에 따라 메모리의 상태를 확인하여 문제를 예방하기 위한 용도<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; nvidia=smi처럼 GPU의 상태를 보여주는 모듈 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Colab은 환경에서 GPU 상태를 보여주기 때문에 편함 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; iter마다 메모리가 늘어나는지 확인할 수 있다. <br>
        &nbsp; 2. &nbsp; torch.cuda.empty_cache() <- 자바의 가비지 콜렉터와 같은 역할 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 사용되지 않은 GPU상 cache를 정리 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 가용 메모리를 확보<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; del과는 구분이 필요 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; reset 대신 쓰기 좋은 함수<br><br>
        &nbsp; 3. &nbsp; trainning loop에 tensor로 축적 되는 변수는 확인할 것! <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; tensor로 처리된 변수는 GPU상에 메로리 사용 <- backward와 같이 이전의 loss값은 1번만 이용하지만 해당 값은 메모리에 계속 남아있게 된다 이러한 것은 아래와 같은 메모리를 잠식하는 문제점을 발생시킨다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 해당 변수 loop 안에 연산에 있을 때 GPU에 computational graph를 생성(메모리 잠식) <- 파이썬의 기본 객체로 만들어 주기 : .itm(), float()등을 이용 <br>
        <br>
        &nbsp; 4. &nbsp; del 명령어를 적절히 사용하기 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 필요가 없어진 변수는 적절한 삭제가 필요하다. 특히 pytho의 메모리 배치 특성상 loop이 끝나도 메모리를 차지하는데 이때 del을 이용하여 없애주자!<br><br>
        &nbsp; 5. &nbsp; 가능 batch 사이즈 실험해보기 <- 위의 개요에서 언급한 내용 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 학습시 OOM이 발생했다면 batch 사이즈를 1로 해서 실험해보기 <br>
        <br>
        &nbsp; 6. &nbsp; torch.no_grad() 사용하기 <- 3에서 언급한 문제를 해결할 수 있다.  <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Inference 시점에서는 torch.no_grad() 구문을 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; backward pass로 인해 쌓이는 메모리에서 자유롭다.<br>
        <br>
        &nbsp; 7. &nbsp; 예상치 못한 에러 메시지 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; OOM 말고도 유사한 에러들이 발생한다. <- CUDNN_STATUS_NOT_INIT이나 device-side-assert 등 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 해당 에러도 cuda와 관련하여 OOM의 일종으로 생각될 수 있으며, 적절한 코드 처리가 필요하다. <br>
        <br>
        &nbsp; 8. &nbsp; 그외... <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; colab에서 너무 큰 사이즈는 실행하지 말 것 <- 예를 들어서  linear, CNN, 특히 LSTM(backpropagation때 너무 많은 메모리를 사용한다.)<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; CNN의 대부분의 에러는 크기가 안 맞아서 생기는 경우 <- torchsummary 등으로 사이즈를 맞출 것 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; tensor의 float precision을 16bit로 줄일 수 도 있다.<br>

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