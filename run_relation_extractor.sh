allennlp predict dygiepp/ace05-relation.tar.gz \
    adventure-ace05.json \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader \
    --output-file adventure-relation.jsonl \
    --cuda-device -1