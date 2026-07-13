# pd-code-components

Find link components in a planar-diagram code.

## Installation

```bash
pip install pd-code-components
```

## Quick start

`from pd_code_components import get_components_from_pd_code`.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
