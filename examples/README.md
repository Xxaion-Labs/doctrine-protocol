# Examples

These examples show how mounted Doctrine Protocol context can be used inside DoctrineOS-compatible AI workflows.

## Prompt context export

```bash
python examples/prompt_context_export.py
```

Writes mounted instruction context to `mounted_context.txt`.

## API payload adapter

```bash
python examples/api_payload_adapter.py
```

Builds a generic payload with:

- mounted doctrine context as `system`
- user message as `user`
- doctrine ID and context hash in `metadata`

## Local model prompt

```bash
python examples/local_model_prompt.py
```

Builds a plain-text prompt for local model workflows.

## Testing

The example scripts are covered by `tests/test_examples.py` so they do not silently drift.
