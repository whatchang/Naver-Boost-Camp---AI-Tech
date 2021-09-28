<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# week8-5 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [학습 회고](#2-학습-회고)

## 1. 공부한 내용 정리

BERT 논문 정리

Abstract
- BERT는 unlabeled text에 대해서 양방향 pre-train을 할 수 있도록 설계되어졌다.
- BERT는 한 개의 output layer를 추가함으로써 여러 task를 수행할 수 있다.

Introduction
- 이전까지의 LM은 feature-based와 fine-tuning의 전략을 사용하는 모델들이 있었다. 그러나 해당 모델들은 unidirectional이거나 완벽한 bidirectional 모델이 아니였다. -> feature-based(Elmo), fine-tuning(GPT-1)
- 위와 같은 모델의 한계는 단어의 관계에 대해서 문맥 정보를 제대로 반영하지 못한다.
- BERT는 위와 같은 한계를 극복한 모델이다.
- BERT는 MLM(Masked Language Model)방식을 pre-training에 사용하므로써 이전의 unidirectional의 한계점을 완화시켰다. * MLM은 좌우 문맥(단어)를 잘 녹여서 학습하는데 도움을 준다.
- BERT는 NSP(Next Sentence Prediction)이라는 방식도 pre-train시 사용을 한다.

Conclusion
- 저자의 기여한 점은 deep bidirectional architectures방식을 일반화시킨 것이다.

나의 생각(Abstract와 Introduction, Conclusion을 읽고 난 후)
- 무엇을 해결하고 싶은 것인가?
    - 이전까지의 한계(unidirectional)를 극복하고자 했다.
- 이전 모델과 달라진 점은?
    - MLM과 NSP 방식을 사용하여 pre-training에서 bidirectional하게 학습하여 좌우 문맥(단어)의 관계를 반영시켰다.
- 핵심 키워드
    - Bidirection
    - MLM
    - NSP
    - Encoder
- 논문 진행 방향(흐름) 예상
    - MLM과 NSP에 대해서 자세하게 설명을 하고 이것이 좌우 문맥을 이해하는데 어떤 도움을 주었는지 설명할 것 같다.
    - 이전 모델에 비해서 BERT의 성능이 어느정도 좋아졌는지 비교하고 bidirectional language model의 강점을 설명할 것 같다.
	
Related Work
- Unsupervised Feature-based Approaches

- Unsupervised Fine-tuning Approaches

- Transfer Learning from Supervised Data

BERT 동작 원리
- BERT는 먼저 pre-train으로 파라미터를 initialization을 하고 fine-tuning을 통해서 해당 task에 맞게 파라미터를 다시 학습시켜준다.
- Architecture
    - Base : num of layer 12, hidden size 768, number of self-attention head 12 => total parameter 110M
    - Large : num of layer 24, hidden size 1024, number of self-attention heads 16 => total parameter 340M
        * 위의 계산에 대한 자세한 것은 https://github.com/google-research/bert/issues/656 참고
- Input/Output Representations
    - WordPiece embeddings을 사용
    - Input sequence의 맨 처음은 CLS라는 special token을 사용한다.
    - 2개의 sentence를 하나의 input으로 받을때 이것을 구별하기 위해서 SEP라는 special token을 사용한다. 이것에 따라 segment embedding을 해준다.
    - Position embedding도 사용한다
    - 총 3가지의 embedding 방식을 사용한다.
- Pre-training BERT 
    - MLM(Masked Language Model) 
        * deep bidirectional representation을 위해서 input의 무작위로 masking을 한다. 이때 input에 대한 masking 비율은 15%이다.
        * masking된 부분은 80%가 mask token으로 바뀌고 10%는 무작위로 바뀌며 남은 10%는 변화되지 않는다.
    - NSP(Next Sentence Prediction)
        * 50%정도는 앞뒤 문장이 선택되고 50%정도는 무작위로 2개의 문장이 추출된다.
        * 추출된 문장이 연속적인지에 대해서 구별하는 task를 수행하면서 학습을 한다.
- Fine-tuning BERT
    - CLS는 classfication(entailment or sentiment analysis)에 대한 task를 수행할 때 사용하며 sequence tagging or question answering과 같은 token level task들은 token representation을 통해서 task를 수행한다.
    - 
Experiments

Ablation Studies

내 생각(1회독 후 BERT에 대한 생각)
- 핵심 키워드
- 저자의 말하고자 한 것
- 추가로 보고 싶은 reference
- 활용 방안 및 발전 방향 생각해 보기


<br>

## 2. 학습 회고

* 오늘 BERT 논문을 다 읽을 생각이었지만 다 읽지 못하였다 ㅠㅠ
* 그래도 정리하면서 읽으니까 뭔가 더 잘 읽히는 느낌이다. 그러나 영어는... 어려...다... ㅠㅠ
* 이번 주도 수고 많았고 다음 대회 화이팅~~~!👍

<br>