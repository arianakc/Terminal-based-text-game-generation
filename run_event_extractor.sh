allennlp predict dygiepp/ace05-event.tar.gz \
    adventure.json \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader \
    --output-file adventure-event.jsonl \
    --cuda-device -1