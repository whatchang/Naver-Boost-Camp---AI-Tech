<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day32 

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 강의내용 정리

#### 오늘은 10강 강의를 한 번더 듣고 10강 정리 후 강의 정리를 위해서 몇가지 내용을 좀 더 찾아보았고 9강도 정리를 하였다. 해당 내용은 전날 day31.md에 기록을 해놓았다.

<br>

## 2. 과제 정리


<br>

## 3. 피어세션 정리

##### 9강 Self-supervised Pre-training Models

---

발표자: `전준영`

- 발표 내용

    [https://github.com/20180707jun/naver-boostcamp-ai/blob/main/week7/ch9_self-supervised-PLM.md](https://github.com/20180707jun/naver-boostcamp-ai/blob/main/week7/ch9_self-supervised-PLM.md)

- Discussions
    - learned positional embedding
        - Transformer : 위치 정보
        - BERT : random initialization 하고 학습을 통해 position 정보를 배우길 기대
    - BERT : 4 tasks
        - 쌍, 단일 분류 문제 : 위치 별로 해당하는 토큰 임베딩 벡터를 FCN 과 같은 분류 적용
        - QA : 관련 있는 정보의 시작과 끝
        - 단어의 의미를 tagging
        - 다운스트림 사용 예시를 잘 표현한 그림

            1 )  하나의 텍스트에 대한 텍스트 분류 유형 (Single Text Classification)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ea29de0-ac76-46ca-987b-132a58dd333c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ea29de0-ac76-46ca-987b-132a58dd333c/Untitled.png)

            2 )  하나의 텍스트에 대한 태깅 작업 (Tagging)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67259884-877a-43ac-bbf0-f76deb5bdc24/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67259884-877a-43ac-bbf0-f76deb5bdc24/Untitled.png)

            3 )  텍스트 쌍에 대한 분류 또는 회귀 문제 (Text Pair Classification or Regression)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bce37765-946b-40cc-88d5-92ec4d63478c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bce37765-946b-40cc-88d5-92ec4d63478c/Untitled.png)

            4 )  질의 응답 (Question Answering)

            ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ce9d2cf-2532-4231-be4d-d6f81b85079f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ce9d2cf-2532-4231-be4d-d6f81b85079f/Untitled.png)

**Further Question**

- BERT의 Masked Language Model의 단점은 무엇이 있을까요? 사람이 실제로 언어를 배우는 방식과의 차이를 생각해보며 떠올려봅시다
    - Mask를 씌우는 방식에서 문제가 있다.
    - 여러개의 빈칸이 있을 경우 사람은 Mask 간의 관계도 고려해서 파악
    - 일상 Task에서도 Mask가 뚫려있지않음, 사전학습과 실제 Task간의 불일치
    - 외부데이터(배경지식, 상식)를 활용시 문제가 있을 수 있다.
- CutMix와의 차이?
    - 이건 복원하는 방식은 아님
    - DEiT 가 MLM과 비슷한 방식을 씀

##### 10강 Advanced Self-supervised Pre-training Models

---

발표자: `심우창`

- 발표 내용

    [https://github.com/whatchang/Naver-Boost-Camp---AI-Tech/blob/master/week7/day31/day31.md](https://github.com/whatchang/Naver-Boost-Camp---AI-Tech/blob/master/week7/day31/day31.md)

    [점프 투 파이썬](https://wikidocs.net/22592)

- Discussions
    - GPT-2
        - task에 대한 fine tuning 없이 사용했는데 어떻게 결과가 괜찮게 나온 것일까?
            - CV 와 다르게 (다른 개념) NLP 에서 few-shot 은 단순 : fine tuning 안시키면 zero-shot , 한번에 얼마나 많은 샘플을 보여줄건지(shot), TL;DR
            - 질의 응답으로 바꾸어주었다고 이해하면 됨, 프롬프트
            - 이미 결과가 잘 나오도록 설계됨
            - 
    - GPT-3
        - initialization, pre-normalization, reversible tokenization
        - Transformer layer <- SparseTrnsformer(기존의 transformer layer 당 복잡도를 줄이기 위한 방식, O(Nlogn))와 유사한 alternationg dense와 locally banded sparse attention
        - one/few shot에서 example을 주지만 output layer를 추가해 주지 않는다(기존의 GPT-1에서는 task에 따른 output layer를 추가해주었다.). 그렇다면 추가해줄 때와 추가하지 않을 때는 어떤 차이들이 있나?(성능, data의 shape, 장단점은?, 이 부분이 학습에 영향을 주는가?)
    - ALBERT
        - 파라미터를 공유했는데 성능이 많이 떨어지지 않는 이유? -> layer간의 파라미터를 공유하면 layer를 그만큼 적게 쌓는거랑 같은거 아닌가?
    - ELECTRA
        - backpropagation이 어떤 식으로 진행되는지 궁금하다
    - 

    [실습 코드] Transformer 라이브러리 사용하기

    "bert-base-uncased"

    - Config
        - head layer, ...
    - Tokenizer
        - input_ids, token_type_ids ,attention_mask
    - Model
        - word_embeddings
        - position_embeddings
        - token_type_embeddings
        - encoder x 12
        - pooler (논문에는 없었던 부분)

    seq_model = BertForSequenceClassification.from_pretrained(bert_name, num_labels=10)

    [transformers/modeling_gpt2.py at master · huggingface/transformers](https://github.com/huggingface/transformers/blob/master/src/transformers/models/gpt2/modeling_gpt2.py#L412)

<br>

## 4. 학습 회고

#### 오늘은 정신없이 시간이 지나간 것 같다. 
<br>

#### 오전부터 피어세션전까지는 강의정리하고 해당 내용 발표를 위해서 추가 정보를 찾는등 정신없이 시간이 지나갔고 저녁과 밤에는 알고리즘 문제 푸니라 금방 지나간것 같다. 
<br>

#### 드디어 내일부터는 삽질했던 것 정리할 수 있을 것 같다~~~ ㅎㅎㅎㅎㅎㅎㅎ
<br><br>