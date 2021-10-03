<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# week9-2

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [학습 회고](#2-학습-회고)

## 1. 공부한 내용 정리

* KLUE 대회 관련 내용
    * model customizing을 진행하였다. 해당 작업을 수행하는데 8~9시간 정도 했던 것 같은데.... 실패하였다. level 1의 마스크 분류 competition때와 비슷하게 customizing을 하면 될 것 같았지만 그때보다 많은 부분을 고쳐야 했다(정확하게 말하면 baseline code를 활용하지 않고 새롭게 작성해야 하는 부분이 많았다). 최대한 모델을 학습하고 예측하는데 필요한 부분만 작성해서(구글링해서) 만들려고 했지만 기본기(pytorch 메소드 관련, input/output의 차원/사이즈 관련)가 탄탄하지 못해서 학습이 제대로 되지 않은 모델을 만들었다 ㅠㅠ 내가 오늘 고생해서 만든 코드로 탄생한 모델을 eval(inference)시 class 1만 고른다.... 🥲

<br>


## 2. 학습 회고

오늘 Model customizing을 하면서 느낀점과 KLUE 대회 참여 방향성
<br>

1. Model customizing을 하면서 느낀점
<br>

klue/roberta-large or klue/robert-small 모델 등 기존의 pretrained된 모델에 layer를 추가하는 작업이 이렇게 어려운 줄 몰랐다 ㅠㅠ
개인적으로 어렵다고 느껴진 이유는 2가지가 있는데 첫번째로 모델을 추가하게 되면 baseline code를 사용할 수 없고 전반적인 코드를 스스로 다시 작성해야 된다는 점과(dataset, dataloader, custom model, forward, train, inference, compute_metric 등) 모델을 hugging face의 transformer 안에 method를 통해서 가져오기 때문에 해당 부분의 hugging face 코드를 이해하고 코드를 작성해야 된다는 점이다.
이 작업을 시작한지 얼마 안 되었을때는(1~2시간 쯤에) 4~5시간 안에 끝낼 수 있을것 같았다(그때는 모델 커스텀과 train부분만 작성하면 되는줄 알았다). 그러나 일을 수행할수록 조금씩 추가로 해야하는 부분이 있다는 것을 인지하였고 그럴수록 더 조급해져만 갔다. 그래서 어제와 비슷하게 천천히 이해하고 정리하면서 분석하는게 아니라 구글링을 통해서 정보를 대충 이해하고 가져다 쓰는데 바뻤고 참고 하기위한 code도 대충 이해하고 내 코드에 오류가 안 날때까지 print문을 찍어가면서 디버깅하였다. 결과적으로 9시간 정도 투자하였지만 해당 작업을 끝내지 못했고 포기하고 싶은 마음이 컸다. 그러나 이와 같은 일이 추후에 또 있을 것이고 어짜피 극복해야 된다면 지금 극복하는 것이 더 낫다고 생각했다(지금은 막히는 부분에 대해서 멘토님 혹은 다른 캠퍼님들에게 질문할 수 있기 때문이다. 또 지금 이러한 부분을 극복하고 내것으로 만든다면 나중에 큰 도움이 될거라고 생각했기 때문이다). 

<br>

2. KLUE 대회 참여 방향성
<br><br>

오늘 실패했던 model customizing을 이번 대회 안에 꼭 끝내고 커스텀하는 법을 내것으로 만들겠다는 목표/방향성을 갖게 되었다.
<br><br>

그래서 model customizing을 하기 위해서 어떻게 할 것인지에 대해서 간단하게 적어볼 생각이다.<br><br>

model customizing을 하기 위해서 필요한 것들<br>
1. nn.Module을 상속받는 모델 커스텀 class만들기
2. 위의 클래스에서 init, forward메소드 작성하기
3. init에서 layer 추가할때 input/output size(차원)에 대해서 잘 알아야 됨
4. forward시에도 input/output 차원을 잘 알고 적용시켜야 된다.
5. Dataset을 상속받은 train dataset 클래스 만들고 init, len, getitem 등을 구현해주어야 한다. 
6. batch size마다 모델에 dataset을 feed시키기 위한 dataloader를 생성
7. 주어진 epoch동안 모델을 학습시키는 반복문 구현하기
8. 위의 반복문에 validation(사전에 total data에서 split해서 tarin, validation으로 나눠줘야 한다.)을 평가하는 코드도 작성
9. validation 평가때 사용할 metric 코드도 작성(f1, micrio_f1, auprc 등)
10. 모델을 저장하기 위한 코드도 작성

위의 것들은 오늘 9시간 동안 하면서 느꼈던 것들인데 아래의 코드를 통해서 필요한 부분에 대해서 좀 더 자세하게 알아볼 생각이다.
[model customizing에 대해서 참고할 코드 - 데이콘 : 뉴스 토픽 분류 task](https://dacon.io/competitions/official/235747/codeshare/3072)
<br><br>

앞으로의 계획<br>
step1 : 위의 코드를 분석하면서 구현해야 하는 것들에 대해서 파악하기 <- 정리하기<br>
step2 : 위의 코드를 분석하고 따라치는 것을 여러번 반복하면서 익숙해지기(이때 뉴스 토픽 분류 task라는 점을 고려하면서 분석하기)<br>
step3 : 위의 코드에 대한 전반적인 이해와 model customizing에 대해서 익숙해지고 있다면 step2와 병행하면서 내가 현재 수행할 task에서 customizing을 할 때 어떻게 구현할지(step1의 내용을 참고하여) 생각해보기 <- 아이패드 혹은 공책에 정리하면서<br>
step4 : step1~step3의 내용을 바탕으로 하나씩 차근차근 구현해보기 <- 이때 한 번에 완성하려고 하지 말고 작은 모듈 단위로 하나씩 작업하기.<br>
step5 : step4에서 구현한 것들을 하나로 합치기<br>
step6 : 잘 동작하는지 체크하고 수정하거나 발전시킬 부분있는지 생각해보기<br>
step0 : 위의 모든 과정을 잘 기록하기!(매우 중요)<br>

<br>