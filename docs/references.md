# References

Sources that inform the AI Character Memory Benchmark's concepts and design. Entries are grouped by topic. The benchmark does not claim that these works endorse it; they are cited for the ideas, evidence or methods they contribute. arXiv identifiers are given where available so each entry can be found directly.

If you find an error or know an important missing source, please open an issue or pull request.

## Long-term conversational memory

* Xu, J., Szlam, A., & Weston, J. (2022). **Beyond Goldfish Memory: Long-Term Open-Domain Conversation.** *Proceedings of ACL 2022.* [ACL Anthology](https://aclanthology.org/2022.acl-long.356/) · arXiv:2107.07567. Introduces Multi-Session Chat (MSC), dialogue across multiple sessions with persona information carried between them.
* Xu, X., Gou, Z., Wu, W., Niu, Z.-Y., Wu, H., Wang, H., & Wang, S. (2022). **Long Time No See! Open-Domain Conversation with Long-Term Persona Memory.** *Findings of ACL 2022.* [ACL Anthology](https://aclanthology.org/2022.findings-acl.207/) · arXiv:2203.05797.
* Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). **Evaluating Very Long-Term Conversational Memory of LLM Agents.** *Proceedings of ACL 2024.* [ACL Anthology](https://aclanthology.org/2024.acl-long.747/) · arXiv:2402.17753 · [project page](https://snap-research.github.io/locomo/). The LoCoMo benchmark.
* Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2025). **LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.** *ICLR 2025.* arXiv:2410.10813 · [code](https://github.com/xiaowu0162/LongMemEval). Covers information extraction, multi-session reasoning, temporal reasoning, knowledge updates and abstention.

## Memory architectures for LLM agents

* Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). **MemGPT: Towards LLMs as Operating Systems.** arXiv:2310.08560.
* Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). **Generative Agents: Interactive Simulacra of Human Behavior.** *Proceedings of UIST 2023.* arXiv:2304.03442. Memory streams with retrieval by recency, importance and relevance, plus reflection.
* Zhong, W., Guo, L., Gao, Q., Ye, H., & Wang, Y. (2024). **MemoryBank: Enhancing Large Language Models with Long-Term Memory.** *Proceedings of AAAI 2024.* [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/29946) · arXiv:2305.10250. Includes forgetting and updating inspired by the Ebbinghaus curve, demonstrated on a companion use case.
* Chhikara, P., Khant, D., Aryan, S., Singh, T., & Yadav, D. (2025). **Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory.** arXiv:2504.19413.

## Long context and retrieval

* Lewis, P., Perez, E., Piktus, A., et al. (2020). **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.** *NeurIPS 2020.* arXiv:2005.11401.
* Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). **Lost in the Middle: How Language Models Use Long Contexts.** *Transactions of the ACL, 12.* arXiv:2307.03172. Shows that the position of information in a long input affects whether models use it, relevant to separating memory from context.

## Character consistency and roleplay

* Zhang, S., Dinan, E., Urbanek, J., Szlam, A., Kiela, D., & Weston, J. (2018). **Personalizing Dialogue Agents: I have a dog, do you have pets too?** *Proceedings of ACL 2018.* arXiv:1801.07243. The PersonaChat dataset.
* Welleck, S., Weston, J., Szlam, A., & Cho, K. (2019). **Dialogue Natural Language Inference.** *Proceedings of ACL 2019.* arXiv:1811.00671. Frames persona consistency as natural language inference.
* Li, K., Liu, T., Bashkansky, N., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2024). **Measuring and Controlling Instruction (In)Stability in Language Model Dialogs.** *COLM 2024.* arXiv:2402.10962. Documents persona/instruction drift over long dialogues.
* Shao, Y., Li, L., Dai, J., & Qiu, X. (2023). **Character-LLM: A Trainable Agent for Role-Playing.** *Proceedings of EMNLP 2023.* arXiv:2310.10158.
* Wang, Z. M., Peng, Z., Que, H., et al. (2023). **RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models.** arXiv:2310.00746.
* Tu, Q., Fan, S., Tian, Z., & Yan, R. (2024). **CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation.** *Proceedings of ACL 2024.* [ACL Anthology](https://aclanthology.org/2024.acl-long.638/) · arXiv:2401.01275.
* Wang, X., Xiao, Y., Huang, J., et al. (2024). **InCharacter: Evaluating Personality Fidelity in Role-Playing Agents through Psychological Interviews.** *Proceedings of ACL 2024.* arXiv:2310.17976.
* **RMTBench: Benchmarking LLMs Through Multi-Turn User-Centric Role-Playing** (2025). arXiv:2507.20352.
* **RP-Bench**, a roleplay quality benchmark covering character consistency, user agency, lorebook integration, long-range temporal memory and prose across many dimensions. [GitHub: LeviTheWeasel/rp-benchmark](https://github.com/LeviTheWeasel/rp-benchmark) · [arena](https://arena.l3vi4th4n.ai/).

## Behavior under user pressure

* Sharma, M., Tong, M., Korbak, T., et al. (2023). **Towards Understanding Sycophancy in Language Models.** arXiv:2310.13548. Relevant to false-memory confirmation and identity collapse under pressure.

## Human-computer interaction and AI companions

* Reeves, B., & Nass, C. (1996). ***The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places.*** Cambridge University Press / CSLI.
* Bickmore, T. W., & Picard, R. W. (2005). **Establishing and Maintaining Long-Term Human-Computer Relationships.** *ACM Transactions on Computer-Human Interaction, 12*(2), 293–327. [doi:10.1145/1067860.1067867](https://dl.acm.org/doi/10.1145/1067860.1067867).
* Skjuve, M., Følstad, A., Fostervold, K. I., & Brandtzaeg, P. B. (2021). **My Chatbot Companion: A Study of Human-Chatbot Relationships.** *International Journal of Human-Computer Studies, 149*, 102601. [doi:10.1016/j.ijhcs.2021.102601](https://doi.org/10.1016/j.ijhcs.2021.102601).

## Cognitive science of memory

* Tulving, E. (1972). **Episodic and Semantic Memory.** In E. Tulving & W. Donaldson (Eds.), *Organization of Memory* (pp. 381–403). Academic Press. Origin of the episodic/semantic distinction. The benchmark uses "episodic" descriptively and makes no claim that AI memory mirrors human memory.

## Evaluation methodology

* Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.** *NeurIPS 2023 Datasets and Benchmarks.* arXiv:2306.05685. Background for using, and validating, LLM judges ([scoring/judge-prompt.md](../scoring/judge-prompt.md)).

## Background essays

These are informal writings by the maintainer that motivated parts of the framework. They are not peer-reviewed and are listed for transparency about where the ideas came from.

* [AI Character Long-Term Memory](https://github.com/garretewilliams/ai-character-long-term-memory): notes on memory, context and contextual inference in AI roleplay, including the distinction between fact memory and experience memory.
* [AI Chat That Remembers: Persistent Memory, Not a Reset](https://chatbrat.ai/ai-chat-that-remembers) (ChatBrat): on persistent memory and relationship continuity.
* [Why Does Character.AI Keep Forgetting Everything After 20 Messages?](https://chatbrat.ai/bratlog/why-character-ai-forgets-everything) (ChatBrat Bratlog): a general explainer on why AI characters forget (context limits, summarization and retrieval).
* [The Ultimate AI Roleplay Setup Guide: Memory, Lorebooks, and Multi-Character Scenes](https://medium.com/@chatbrat.ai/the-ultimate-ai-roleplay-setup-guide-memory-lorebooks-and-multi-character-scenes-2626e78b8c24) (ChatBrat on Medium): on memory and lore in long-term roleplay.
