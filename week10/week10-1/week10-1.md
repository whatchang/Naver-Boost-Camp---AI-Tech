<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# week10-1 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [학습 회고](#2-학습-회고)

## 1. 공부한 내용 정리

### model customizing에 대해서 - step1

[model customizing에 대해서 참고할 코드 - 데이콘 : 뉴스 토픽 분류 task](https://dacon.io/competitions/official/235747/codeshare/3072)
<br><br>

#### 위의 코드를 분석하면서 구현해야 하는 것들에 대해서 파악하기

* 위의 코드는 다음과 같이 구성이 되어있습니다.
    * MLM - pretrain
    * training
    * make psuedo labels

<br>
<br>

이 중에서 제가 볼 코드 부분은 MLM과 training 부분입니다. <br>
(MLM부분은 layer를 추가하는 모델 커스텀마이징과는 관련이 없지만 해당 코드를 이번 competition에 적용시켜보았기 때문에 공부차원에서 분석해보려고 합니다.)
<br><br>

* MLM
    * Class 
        * Config : MLM pre-training한 모델을 저장할 위치, seed, epoch, batch size, save step, MLM 비율, dataset directory등을 설정하는 class<br>
        * TokenizerDataset : pre-train시킬 모델의 modelForMaskedLM의 pretrain 모델과, Config 인스턴스의 정보를 바탕으로 dataset의 문장을 전처리 한 후 __ getitem __ 을 통해서 학습시 적절한 data를 feed 시켜준다.<br>
    <br>
    * method(def)
        * preprocessing : 인자로 들어온 line(학습에 사용될 데이터)을 영어와 한글 정보를 제외한 모든 정보를 filtering시켜서 반환해준다.
        * main : hugging face library(AutoModelForMaskedLM, AutoTokenizer, DataCollatorForLanguageModeling, TrainingArguments, Trainer)과 위에서 정의한 Class, method를 이용하여 주어진 데이터와 pre-trained model에 대해서 MLM pre-training을 수행하고 저장한다. <br>
    <br>
    * 좀 더 알아보고 정리할 것들(함수 사용 목적과 인자값, 리던값 등에 대해서 살펴보고 간단하게 정리하기)
        * AutoModelForMaskedLM : <br>
        * AutoTokenizer : <br>
        * DataCollatorForLanguageModeling : <br>
        * TrainingArguments : <br>
        * Trainer : <br>
        <br>

* Training
    * Custom model 만들기

    * train 시키기(for문 이용)

<br>

* 위의 training을 분석 및 정리하던 중에 팀원 중 한 명이 custom model class는 만들되 train시 hugging face의 trainer를 사용하는 방식으로 코드를 작성해서 해당 코드를 보면서 공부할 생각이다. 이때 for문을 이용하는 방식과 어떤 차이점이 있는지 비교해보면서 공부할 생각이다.


## 2. 학습 회고
<br>

모델 커스텀마이징에 대해서 공부하던 중 팀원이 작성한 코드 덕분에 nlp model의 커스텀마이징에 대해서 잘 이해할 수 있을 것 같다. 또 위에서 언급한 것처럼 비교분석을 해서 두 방식 모두 다룰줄 알도록 학습할 예정이며 이번 대회에서는 이 부분에 대해서만 집중할 생각이다. 
<br>
+ MLM에서 정리한 좀 더 알아보고 정리할 것들도 시간을 내서 정리하도록 해야겠다 ㅎㅎ
<br>