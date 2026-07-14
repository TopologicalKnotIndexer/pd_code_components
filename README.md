# pd-code-components

Find the components represented by a planar-diagram code.

## Installation

```bash
pip install pd-code-components
```

## Usage example

```python
from pd_code_components import get_components_from_pd_code

hopf = [[2, 3, 1, 4], [4, 1, 3, 2]]
print(get_components_from_pd_code(hopf))
# [[1, 2], [3, 4]]
```

## Algorithm

At each crossing, slots `0` and `2` belong to one strand and slots `1` and `3` to the other. These opposite-slot pairs form an undirected graph on arc labels. Before traversal, the implementation verifies a consistent label type and exactly two occurrences of every label. Iterative depth-first traversal then finds connected components in `O(V + E)` time. Sets are used for adjacency and visitation, avoiding the quadratic membership checks in the original list-based implementation.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Python 3.10 or newer is required. Run the regression tests with:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_pd_code_components,
  author = {{TopologicalKnotIndexer contributors}},
  title = {{pd\_code\_components}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/pd_code_components}
}
```
