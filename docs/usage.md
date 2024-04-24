### Evaluation

#### Run evaluation
- We have separate evaluation files per experiment for each of the model. So they can directly be run once all the requirements are setup.
  - You will have to change the file name and the split name depending on the experiment.
  - The experiments can be run using following:
```
python -m llama.eval +variant="ft_1.3b" eval.split=valid
```

#### Run evaluations metrics
To run the evaluation metrics, you can use the following command (from this directory):

```bash
python -m weblinx.eval -d results -b ./wl_data/demonstrations
```

In this case, `-b` is the base directory for the demonstrations, and `-d` is the directory containing the results (generated above by the `llama.eval` script). This will automatically run the evaluation metrics and save the results in the `results/aggregated_scores.json` directory. If you are only interested in the overall score for a split (e.g. `valid`), you can find look for the following entry in the aggregated score file (as an example):

```json
// ...
  {
    "split": "valid",
    "intent": "overall",
    "metric": "overall",
    "model_name": "princeton-nlp/Sheared-LLaMA-1.3B",
    "project_name": "llama_ft",
    "score": 0.21667765869744438,
    "unconditional_score": 0.15307513104251605
  },
// ...
```

Behind the scene, this will use the `weblinx.eval.auto_eval_and_save` function to run the evaluation metrics. If you want more control, you can also use that `weblinx.eval.auto_eval_and_save` function directly if you prefer; for an example, check out `weblinx/eval/__main__.py`.

Note that it might be slow the first time you run, because it reads a lot of demonstrations and load millions of files. However, a demo-level cache is automatically created (see `./.cache/demonstrations`), so the next time you run it, it should be much faster.