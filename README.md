1. huggingface上的微调大模型

- https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

- https://huggingface.co/kshitizgajurel/Romanized-Nepali-Gemma2b-finetuned-for-ecommerce-application

- https://huggingface.co/clouditera/secgpt（云起无垠公司-13B）

- https://huggingface.co/lilBuffaloEric/autoaudit_20230703_attempt1（7B-有些模型即便能够接受带有上下文的 prompt，但在生成回应时可能无法充分利用这些上下文；有些模型是为特定任务设计的，比如问答、翻译、或文本生成，这些模型可能并没有针对对话场景进行优化，所以它们在处理上下文关联时表现不佳）

2. 检测 or 整合

3. 评论信息summarize + 人工决策树 + LLM整合

4. 决策树需要考虑预测的时候有数据缺失的情况（CART算法，多路径）

5. 决策树 分类树？ 规则？

6. 数据库里查拉起与被拉起的应用的信息（存的时候就是LLM总结的，例如已下架，下架原因，未下架，相关功能等）

7. 一旦告诉了LLM这款应用存在什么风险（决策树的输出结果），什么样的数据都会被解释成证据（检测结果先做分类）

8. 把一些额外信息的查询作为Agent配备的tool，让Agent自己判断是否需要
考虑到效率，应该是一些指标触发的，比如检测结果（有多少有值的），评论应该有多条呀？

challenge：技术上 系统实现上（从业务challenge提取学术）
用LLM 解决 的papers
workflow
前面模块的评估方案


-----------------

2024.9.20

1. 业务场景（是不是说业务人员只需要看这些数据就可以判断风险？具体是怎么做的？示例数据）
1.1 业务人员目前的风险类别？
2. 验收的时候是否会给出风险类型？
3. retest里的看起来像一个检测项的命中而不是风险结果？

目前的进展：
如果假设已经通过决策树选定了哪些特征作为依据，可以生成证据链

step1: 数据维度初筛
step2: 根据风险设计检测项（自己设计的 + 华为excel里分好的）
step3: 根据检测项的命中情况输入模块

只需要分大类，组装证据（进阶是一些关联数据的分析）
（一些需要的数据可以向华为申请）
