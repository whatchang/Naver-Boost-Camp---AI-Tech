<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day28 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [과제 정리](#2-과제-정리)

3. [피어세션 정리](#3-피어세션-정리)

4. [학습 회고](#4-학습-회고)

## 1. 공부한 내용 정리

* LSTM이 완벽히 gradient vanishing/exploding을 해결했는지에 대해서 구글링하면서 삽질을 했다 ㅠㅠ
* 이 부분에 대해서 내용 정리를 하고 올릴 생각이다.

<br>

## 2. 과제 정리

#### 필수과제 4를 잠깐만 도전해보았다. 그리고 대부분의 시간을 LSTM에 대한 삽질을 하면서 시간을 보냈다 ㅠㅠㅠㅠㅠ


<br>

## 3. 피어세션 정리

발표자:  전진 

- 발표 내용

    [Beam Search and BLEU Score](https://www.notion.so/Beam-Search-and-BLEU-Score-9372e1e56ae1471d8c46d756f8dcc66a)

- Discussions

    Beam search Error analysis (참조 : Deeplearning.ai)

    [C5W3L05 Error Analysis of Beam Search](https://www.youtube.com/watch?v=ZGUZwk7xIwk)

    질문 : beam search에서 결과가 k개? 한번에 보는 것이 k개?

    답변 : 한번에 보는 것이 k개로 가져가는 것이 정설입니다. 보고 있던 hypothesis가 end가 되면 그 hypothesis를 제외하고 다른 것들을 포함하여 4개를 보게 됩니다.

    해당 답변

    [[Sooftware 머신러닝] Beam Search (빔서치)](https://blog.naver.com/PostView.nhn?blogId=sooftware&logNo=221809101199&from=search&redirect=Log&widgetTypeCall=true&directAccess=false)

    - Beam search 코드 구현

    [Search](https://kh-kim.gitbooks.io/pytorch-natural-language-understanding/content/neural-machine-translation/beam-search.html)

    질문 : recall, precision에 대한 설명을 부탁드립니다.

    답변 

    [BLEU Score](https://donghwa-kim.github.io/BLEU.html)

    [예시를 통한 ROUGE 성능 지표의 이해 - Programador | Huffon Blog](https://huffon.github.io/2019/12/07/rouge/)

    - 분자는 같지만, 분모에서 차이가 난다.
    - 중복된 것을 더 잘 찾아내는 것은 precision이다.

### Further Question

---

Q )  BLEU score가 번역 문장 평가에 있어서 갖는 단점은 무엇이 있을까요?

A )  Variety of Reference sentence? 

human evaluation과 다르다. 

- 사람은 n-gram을 카운트해서 번역이 잘 되었음을 평가하지 않는다.
- 다른 의미적인 표현이 있을 수 있다.(의미론적 문장 유사관계)
- 낮은 BLEU로 나타난 문장들이 더 인간적인 경우가 많았다.
- Blender bot ?
- HyperCLOVA 발표 & BLEURT예측 문장의 벡터와 타겟 문장의 벡터의 유사도를 이용해 생성된 문장의 품질을 평가하는 방법

    [Python, Machine & Deep Learning](https://greeksharifa.github.io/machine_learning/2021/01/13/BLEURT-Learning-Robust-Metrics-for-Text-Generation/)

- BARTScore: 위와 유사한 LM을 이용한 평가방법

    [BARTScore: Evaluating Generated Text as Text Generation](https://arxiv.org/abs/2106.11520)

- BEAM Search Hugging Face 구현체 작동 과정 확인하기
    - HF Lib - GenerationMixin
        - `modeling_utils.py` 의 PreTrainModel 클래스에서 GenerationMixin 클래스를 상속 받음
        - `generation_utils.py 에 위치 -> PLM의 genration mixin을 수행. generate() 메서드 사용가능 -> if 문으로 greedy search, sampling, beam search, beam sampling, grouping 등 옵션 존재,`
    - vscode에서 중단 지점 genration_utils.py의 generate 메서드에 중단 지점 걸어두고 실행시켜서 각 과정 확인하기

        ```python
        from transformers import BertForConditionalGeneration
        bart = BertForConditionalGeneration.from_pretrained('jinmang2/kobart')
        import torch
        input_ids = torch.LongTensor(1, 10).reandom_(0, 25000)

        generated = bart.generate(input_ids)
        generated
        # default beam size = 4? 6?
        sequence_output = beam_scorer.finalize() # 결과값을 정리, beam_score도 입력으로 받는데 가장 높은 것을 선택하기 위해.
        ```

### 회의록

---

-  내일 모더레이터: 우창님 

-  특이사항: 맡은 논문 차근차근 읽고 있기

<br>

## 4. 학습 회고

* 피어세션에서 어제 들었던 seq2seq with attention과 bleu에 대한 내용에 대해서 설명을 해주셨는데 그때 놓쳤던 부분이나 좀 더 깊은 부분에 대해서 알 수 있어서 매우 좋았다. 특히 bleu에 대한 발표 이후 precision, recall에 대한 차이 + 만약 predict sequence에서 중복 단어가 있을 경우 어떤 것이 더 정확하게 평가를 해주는지에 대해서도 토론을 해보았다. 항상 그렇지만 오늘도 2시간정도 피어세션 시간을 가진 것 같아서 매우 좋았고 항상 팀원들이 열정적이고 배울점이 많아서 동기부여와 자극을 많이 받는다.
* 어제 이번 주 강의에 대해서 대부분 들어서 오늘은 이전 LSTM 강의의 further question 부분에 있었던 내용에서 질문에 의문이 든 점이 있었는데 질문은 다음과 같다. __'BPTT 이외에 RNN/LSTM/GRU의 구조를 유지하면서 gradient vanishing/exploding 문제를 완화할 수 있는 방법이 있을까요?'__ 이 부분에서 의문이 든 점은 LSTM과 GRU는 gradient vanishing/exploding 문제를 해결한 줄 알았는데 질문을 보니까 마치 완벽히 해결하지는 못했다- 라는 느낌을 받게 되어서 6~7시간 정도 삽질을 했던 것 같다.
* 내 실력과 배경지식이 부족하여 답을 찾는 과정에서 여러 의문점이 생기고 해결도 많이 못하였지만 포기하지 않고 내일 좀 더 찾아보고 정리할 생각이다.
* 다음 level3부터는 팀을 랜덤으로 구성하는 방식이 아닌 직접 구해야 되는데 음.... 처음에는 '분명 잘 되겠지~'라는 마음이었지만 slack에서 하나, 둘 팀 모집을 끝내고 구하는 모습을 보면서 뭔가 불안한 느낌을 많이 받았다. 또 이러한 불안함 때문인지 평소에는 피어세션에서 동기부여와 자극이 되는 것들도 오늘은 뭔가 팀원들과 나 자신과의 격차를 느끼는 감정으로 변했던 것 같다.... 그래도 저녁 먹고 침대에 누워서 여러 생각하고 잠자고 나니 괜찮아졌던 것 같다. 그리고 팀원에 대해서도 원하는 방향의 팀 모집글이 있으면 DM걸고 내 자신에 대해서 적극적으로 어필을 해볼 생각이다.
* 오늘도 고생많았고 화이팅하구~ 
(๑و•̀Δ•́)و 
<br>