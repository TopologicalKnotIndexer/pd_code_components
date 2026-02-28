# pd_code_components
计算 pd_code 中的每一个连通分量对应的编号集合

## Install

```bash
pip install pd-code-components
```

## Usage

```bash
from pd_code_components import get_components_from_pd_code
print(get_components_from_pd_code([[6, 1, 7, 2], [10, 4, 11, 3], [12, 8, 13, 7], [18, 16, 19, 15], [16, 9, 17, 10], [8, 17, 9, 18], [20, 14, 5, 13], [14, 20, 15, 19], [2, 5, 3, 6], [4, 12, 1, 11]]))
```
