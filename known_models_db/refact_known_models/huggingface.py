huggingface_mini_db = {
    "starcoder/15b/base": {
        "backend": "autogptq",
        "model_path": "TheBloke/starcoder-GPTQ",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 18000,
        "T": 4096,
        "filter_caps": ["completion"],
    },
    "starcoder/15b/plus": {
        "backend": "autogptq",
        "model_path": "TheBloke/starcoderplus-GPTQ",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 18000,
        "T": 4096,
        "filter_caps": ["completion"],
    },
    "starchat/15b/beta": {
        "backend": "autogptq",
        "model_path": "TheBloke/starchat-beta-GPTQ",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceStarChat",
        "model_class_kwargs": {},
        "required_memory_mb": 18000,
        "T": 4096,
        "filter_caps": ["starchat"],
    },
    "starcoder/1b/base": {
        "backend": "transformers",
        "model_path": "smallcloudai/starcoderbase-1b",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 8000,
        "T": 8192,
        "filter_caps": ["completion", "finetune"],
    },
    "starcoder/3b/base": {
        "backend": "transformers",
        "model_path": "smallcloudai/starcoderbase-3b",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 12000,
        "T": 4096,
        "filter_caps": ["completion", "finetune"],
    },
    "starcoder/7b/base": {
        "backend": "transformers",
        "model_path": "smallcloudai/starcoderbase-7b",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 20000,
        "T": 4096,
        "filter_caps": ["completion", "finetune"],
    },
    "wizardcoder/15b": {
        "backend": "autogptq",
        "model_path": "TheBloke/WizardCoder-15B-1.0-GPTQ",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadPSM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 18000,
        "T": 4096,
        "filter_caps": ["completion"],
    },
    "wizardlm/7b": {
        "backend": "autogptq",
        "model_path": "TheBloke/WizardLM-7B-V1.0-Uncensored-GPTQ",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceWizard",
        "model_class_kwargs": {},
        "required_memory_mb": 8000,
        "T": 2048,
        "filter_caps": ["wizardlm"],
    },
    "wizardlm/13b": {
        "backend": "autogptq",
        "model_path": "TheBloke/WizardLM-13B-V1.1-GPTQ",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceWizard",
        "model_class_kwargs": {},
        "required_memory_mb": 14000,
        "T": 2048,
        "filter_caps": ["wizardlm"],
    },
    "llama2/7b": {
        "backend": "autogptq",
        "model_path": "TheBloke/Llama-2-7b-Chat-GPTQ",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceLlama2",
        "model_class_kwargs": {},
        "required_memory_mb": 8000,
        "T": 2048,
        "filter_caps": ["llama2"],
    },
    "llama2/13b": {
        "backend": "autogptq",
        "model_path": "TheBloke/Llama-2-13B-chat-GPTQ",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceLlama2",
        "model_class_kwargs": {},
        "required_memory_mb": 14000,
        "T": 2048,
        "filter_caps": ["llama2"],
    },
    "codellama/7b": {
        "backend": "transformers",
        "model_path": "TheBloke/CodeLlama-7B-fp16",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadCodeLlamaSPM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 14000,
        "T": 2048,
        "filter_caps": ["completion", "finetune"],
    },
    "codellama/34b": {
        "backend": "transformers",
        "model_path": "TheBloke/CodeLlama-34B-fp16",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadCodeLlamaSPM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "required_memory_mb": 70000,
        "T": 2048,
        "filter_caps": ["completion", "finetune"],
    },
    "wizardlm/30b": {
        "backend": "transformers",
        "model_path": "TheBloke/WizardLM-30B-fp16",
        "diff_scratchpad_class": None,
        "chat_scratchpad_class": "refact_scratchpads:ScratchpadHuggingfaceWizard",
        "model_class_kwargs": {
            "load_in_4bit": True,
        },
        "T": 2048,
        "filter_caps": ["wizardlm"],
     },
    "deepseek-coder/1.3b/base": {
        "backend": "transformers",
        "model_path": "deepseek-ai/deepseek-coder-1.3b-base",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadDeepSeekCoderFIM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "T": 4096,
        "filter_caps": ["completion", "finetune"],
     },
    "deepseek-coder/5.7b/mqa-base": {
        "backend": "transformers",
        "model_path": "deepseek-ai/deepseek-coder-5.7bmqa-base",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadDeepSeekCoderFIM",
        "chat_scratchpad_class": None,
        "model_class_kwargs": {},
        "T": 4096,
        "filter_caps": ["completion", "finetune"],
     },
    "deepseek-coder/6.7b/base": {
        "backend": "transformers",
        "model_path": "deepseek-ai/deepseek-coder-6.7b-base",
        "diff_scratchpad_class": "refact_scratchpads:ScratchpadDeepSeekCoderFIM",
        "chat_scratchpad_class": None,
        "hidden": True,  # we see some kind of problem with this model (nan's while loss calculation)
        "model_class_kwargs": {},
        "T": 4096,
        "filter_caps": ["completion", "finetune"],
     },
}
