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

2. [진행중인 실험](#2-진행중인-실험)

3. [학습 회고](#3-학습-회고)

## 1. 공부한 내용 정리

없음

<br>

## 2. 진행중인 실험

DPR 구현하기 - [해당 github issue](https://github.com/boostcampaitech2/mrc-level2-nlp-04/issues/8)

<br>

## 3. 학습 회고

아침 회의에서 팀원 덕분에 어제 막혔던 문제가 손 쉽게 해결이 되었다. 문제는

```
    p_embedding_set = []
    with tqdm(wiki_dataloader, unit="batch") as tepoch:
        for batch in tepoch:
            p_inputs = {
                "input_ids": batch[0].view(batch_size, -1).to(device),
                "attention_mask": batch[1].view(batch_size, -1).to(device),
                "token_type_ids": batch[2].view(batch_size, -1).to(device)
            }
            p_outputs = p_encoder(**p_inputs)
            # print(f'1. p_outpus : {p_outputs}')
            p_outputs = p_outputs.view(batch_size, 1, -1)
            # print(f'2. p_outpus : {p_outputs}')
            p_embedding_set.append(p_outputs)
    return p_embedding_set
```
위의 부분에서 p _ embedding _ set이라는 list에 device가 gpu인 변수를 cpu로 바꾸지 않고 바로 append해주었기 때문에 문제가 되었습니다.

이것이 문제가 된 원인은 pytorch는 computation graph를 가지는데 이때 위에서 append한 부분은 gpu device를 갖는 변수를 append하는 것이고 이때 해당 변수가 직접적으로 사용되지 않음에도 불구하고 list의 주소를 넘겨준 상태이므로 해당 값이 버려지지 않고 계속 유지가 되게 됩니다. 그리고 이게 for문 루프가 돌수록 계속 쌓이다 보니 결과적으로 out of memory가 발생하게 된 것입니다.

이를 해결하기 위해서는 
```
p_embedding_set.append(p_outputs)
```
위의 line에 detach().cpu().numpy()를 추가해서
```
p_embedding_set.append(p_outputs.detach().cpu().numpy())
```

이후에 train학습이 잘 안되는 문제가 있었고 이것을 아직 해결하지 못하였습니다.
<br>