# PrompGent
This repository is the implementation for the project submitted as part of course COMP545 at McGill University, Winter 2024. Built on top of [Weblinx](https://mcgill-nlp.github.io/weblinx/). Enhanced prompting for the agent to navigate web tasks.


### Description
Conversational web navigation poses a formidable challenge as digital agents navigate web browsers, responding to user instructions across multi-turn dialogues to accomplish real-world tasks. The introduction of WEBLINX, a robust benchmark derived from 2300 expert demonstrations, has provided an invaluable platform for training and evaluating agents across diverse scenarios.

Recent advancements in prompting have highlighted LLMs' prowess as adept few-shot and zero-shot reasoners. Furthermore, guiding LLMs with longer-term historical context has shown promise in enhancing performance.

Our study delves into how advanced prompting methods impact text-only decoder capabilities in conversational web navigation. By evaluating on the WEBLINX benchmark, we demonstrate that integrating the main conversation topic into the prompt offers enhanced contextual guidance, leading to more accurate actions. Furthermore, we observe that smaller LLMs struggle as zero-shot and few-shot reasoners in conversational web navigation. Our findings highlight the need for a nuanced approach to prompt designs, considering both the capabilities and limitations of different model sizes.

More details available: View the full report [here](./docs/report/report.pdf).

### Requirements
We implemented three experiments each with a different approach to enhance the prompt. This was done on top of the base code supplied by webLinx paper. To run our experiments, all the requirements needed for webLinx need to be installed.

Our experiments were run on the compute Canada cluster so the package names in the [requirements](./requirements.txt) file depict the same.

More details on setting up the environment can be found here: [setup docs](./docs/setup.md)

### Usage
- Setup the webLinx package as described [here](https://github.com/McGill-NLP/WebLINX).
  - or clone our repository and install all the dependencies for webLinx manually.
- Download the complete dataset for webLinx. (get data [here](https://huggingface.co/datasets/McGill-NLP/WebLINX))
  - To speed up the data download process, you can skip screenshot and video files per demonstration since we only considered text only models for our experiments.
- We have separate evaluation files per experiment for each of the model. So they can directly be run once all the requirements are setup.

- Detailed instructions can be found here: [usage docs](./docs/usage.md)


### Results
- These were our experiments:
  - Incorporating evolving main context of conversation to prompt
  - Zero-shot CoT
  - Few-shot CoT
- We aggregate the results for the two models, Sheared-LlaMa-1.3B and Flan-T5-780M here: [results](results\tables.md)


### Contribution
It was a collaboration between the following group members:
Aayush Kapur: @kpraays
Vishvak Raghavan: @vishvak11
More details under contribution section: [contribution](./docs/contribution.md)



