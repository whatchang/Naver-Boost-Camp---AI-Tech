<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [학습 회고](#2-학습-회고)

## 1. 공부한 내용 정리

* 강의 내용 정리
    * 강의 내용 정리하려고 하였으나 대회 관련된 작업에 정신이 팔리는 바람에 하나도 못 했다 ㅠㅠ
    * 이번 주 강의 내용 정리는 아마도 다음주 주말이나 대회 끝나고 시간이 조금 있을때 차근차근 정리할 것 같다 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

* KLUE 대회 관련
    * model customizing 시도 -> 하지 못함
    * pre-train MLM에서 sentence만 학습하는게 아니라 entity도 concat해서 학습시켜보았다. -> 해당 모델은 validation 평가시 성능이 별로 좋지 않아서 리더보드에 제출하지 않았다 ㅠㅠ
    * optimizer를 바꿔보는 시도를 해보았다. -> 최고 성능이 나온 모델에서 optimizer를 MADGRAD로 바꿔서 해본 결과 micrio_f1 : 68.372, auprc : 72.896으로 사용하지 않았을때에 비해 micro_f1이 1.3정도 떨어졌다.

<br>


## 2. 학습 회고

<p>
오늘은 optimizer를 바꾸는데 시간을 엄청 많이 쏟아부었다.

baseline code에서는 transformers.trainer 코드를 사용하기 때문에 hugging face에서 해당 코드 부분에서 optimizer와 관련된 부분을 분석하였다. 
코드를 분석하고 이해하는 능력이 부족하다보니 오래걸린 점도 있지만 이것보다 더 큰 이유는 빨리 끝내고 싶은 마음에 코드를 분석하고 이해할 때 대강대강 훑어본 점이 이 작업을 수행하는데 있어서 시간을 많이 소비하도록 만들었다. 결과적으로 처음에 분석할때 느리지만 꼼꼼히 보고 정리하면서 진행했더라면 시간을 30%정도 절약할 수 있지 않았을까 싶다. 

비록 비효율적으로 해당 작업을 수행했지만 좋은 경험이 된 것 같고 오늘 있었던 일을 통해서 다음에는 이런 실수가 발생하지 않도록 주의해야겠다.

+ 분석할때는 꼭!!!! 정리하면서 하자!

[실험 결과에 대한 정리한 내용1 - MLM에 대한 내용](https://github.com/sangmandu/SangSangPlus/issues/118)
[실험 결과에 대한 정리한 내용2 - MADGRAD에 관한 내용](https://github.com/sangmandu/SangSangPlus/issues/120)
</p>
<br>