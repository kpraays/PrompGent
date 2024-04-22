from pathlib import Path
from functools import partial
import weblinx as wl

import weblinx.utils.format as wlf
from weblinx.processing.dom import clean_and_prune_tree
from weblinx.processing import load_candidate_elements
from weblinx.processing.prompt import build_input_records_from_selected_turns, select_turns_and_candidates_for_prompts

from processing import (
    build_prompt_records_for_llama_truncated,
    build_formatter_for_multichoice,
    insert_formatted_chat_into_records
)

from transformers import (
    AutoTokenizer
)

from transformers.pipelines.pt_utils import KeyDataset

from weblinx.processing.prompt import (
    find_turns_with_instructor_chat,
    format_candidates,
    format_utterances,
    format_utterances_truncated,
    get_speaker,
    multi_attempt_format_prev_turns_truncated,
)
from weblinx.processing.truncation import (
    multi_attempt_truncate_cands_turn,
    multi_attempt_truncate_dom_tree,
)

print("all imports are okay")

def build_formatter_for_multichoice():
    format_click = partial(wlf.format_click, formatters=(wlf.format_uid,))
    format_text_input = partial(
        wlf.format_text_input,
        formatters=(
            partial(wlf.format_arg_item, name="text", max_length=200),
            wlf.format_uid,
        ),
    )
    format_change = partial(
        wlf.format_change,
        formatters=(
            partial(wlf.format_arg_item, name="value", max_length=200),
            wlf.format_uid,
        ),
    )
    format_submit = partial(wlf.format_submit, formatters=(wlf.format_uid,))
    format_load = partial(
        wlf.format_load,
        include_transition=False,
        include_timestamp=False,
        max_length=200,
    )
    format_scroll = partial(wlf.format_scroll, include_timestamp=False)
    format_say = partial(wlf.format_say, include_timestamp=False)
    format_intent_auto = partial(
        wlf.format_intent_automatically,
        format_change=format_change,
        format_click=format_click,
        format_load=format_load,
        format_say=format_say,
        format_scroll=format_scroll,
        format_submit=format_submit,
        format_text_input=format_text_input,
    )
    
    return format_intent_auto

wl_dir = Path("./wl_data")
base_dir = "/home/kapmcgil/scratch/weblinx/modeling/wl_data/demonstrations"
split_path = "/home/kapmcgil/scratch/weblinx/modeling/wl_data/splits-prompt.json"

# Load the name of the demonstrations in the training split
demo_names = wl.utils.load_demo_names_in_split(split_path, split='train')
# You can use: train, valid, test_iid, test_vis, test_cat, test_geo, test_web
# Or you can specify the demo_names yourself, such as the ones we just fetched
# demo_names = ['saabwsg', 'ygprzve', 'iqaazif']  # 3 random demo from valid

print(f"demo from the training split is:{demo_names}")

tokenizer = AutoTokenizer.from_pretrained("McGill-NLP/Sheared-LLaMA-1.3B-weblinx", padding_side="left")
tokenizer.pad_token = tokenizer.eos_token
print("We have the tokeniser.")

format_intent = build_formatter_for_multichoice()

build_prompt_records_fn = partial(
    build_prompt_records_for_llama_truncated,
    format_intent=format_intent,
    tokenizer=tokenizer,)

# Load the demonstrations
demos = [wl.Demonstration(name, base_dir=base_dir) for name in demo_names]

candidates = load_candidate_elements(path="/home/kapmcgil/scratch/weblinx/modeling/wl_data/candidates/train-small.jsonl")


selected_turns = select_turns_and_candidates_for_prompts(
    demos=demos,
    candidates=candidates,
    num_candidates=1,
)


input_records = build_input_records_from_selected_turns(
    selected_turns=selected_turns,
    format_intent=format_intent,
    build_prompt_records_fn=build_prompt_records_fn,
    format_prompt_records_fn=None,
)

print("Input records are:")
print(input_records)
input_records_preformatted = input_records
template_tokenizer = AutoTokenizer.from_pretrained("McGill-NLP/Sheared-LLaMA-1.3B-weblinx")
insert_formatted_chat_into_records(
    records=input_records,
    tokenizer=template_tokenizer,
    include_output_target=False,
)

print()
print("####################################################")
print("Formatted Input records are:")
print(input_records)

dset = KeyDataset(input_records, key="text")
# What is the input being given to the model?
# dset[0], dset[1], ...


# Select a demo to work with
# demo = demos[0]

# # Load the Replay object, which contains the turns of the demonstration
# replay = wl.Replay.from_demonstration(demo)

# print(f"this is what the replay object looks like:{replay}")

# # pick all the turns
# start_index = 0
# prev_turns = replay[start_index : turn.index]
# prev_turns_formatted = [format_intent(turn, return_as=str) for turn in prev_turns]
# # # Filter the turns to keep only the ones that are relevant for the task
# # turns = replay.filter_by_intents(
# #     "click", "textInput", "load", "say", "submit"
# # )

# # # Only keep the turns that have a good screenshot (i.e., the screenshot is not empty)
# # turns = wl.filter_turns(
# #     turns, lambda t: t.has_screenshot() and t.get_screenshot_status() == "good"
# # )

# # # Remove chat turns where the speaker is not the navigator (e.g. if you want to train a model to predict the next action)
# # turns = wl.filter_turns(
# #     turns,
# #     lambda turn: not (
# #         turn.type == "chat" and turn.get("speaker") != "navigator"
# #     ),
# # )

# num_utterances=5,
# max_utterance_tokens=40 * 5
# num_prev_turns=5

# instructor_chat_turns = find_turns_with_instructor_chat(
#     replay, turn, num_prev_turns=num_prev_turns
# )

# utterance_context = format_utterances_truncated(
#         instructor_chat_turns,
#         tokenizer=tokenizer,
#         max_tokens=max_utterance_tokens,
#         num_utterances=num_utterances,
#         format_utterances_fn=format_utterances,
#         allow_iterative_reduction=allow_iterative_reduction,
#     )


