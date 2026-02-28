
# 向一个指定的图中新增节点
def add_edge(nxt:dict, node_a:str|int, node_b:str|int):

    # 确保节点存在
    if nxt.get(node_a) is None:
        nxt[node_a] = []
    if nxt.get(node_b) is None:
        nxt[node_b] = []

    # 将节点加入到列表中
    if node_b not in nxt[node_a]:
        nxt[node_a].append(node_b)
    if node_a not in nxt[node_b]:
        nxt[node_b].append(node_a)

# 使用深度优先搜索确定所有连通分量
def dfs(nxt:dict, vis:list, arr:list, node_name:str|int):
    if node_name in vis:
        return
    vis.append(node_name)
    arr.append(node_name)
    for nxt_node in nxt[node_name]:
        dfs(nxt, vis, arr, nxt_node)

# 从 pd_code 中计算每一个连通分支对应的数值集合
def get_components_from_pd_code(pd_code:list[list[int|str]]) -> list[list[int|str]]:
    if not isinstance(pd_code, list):
        raise TypeError()
    for item in pd_code:
        if len(item) != 4:
            raise AssertionError()
        for sub_item in item:
            if (not isinstance(sub_item, str)) and (not isinstance(sub_item, int)):
                raise TypeError()
    
    # nxt 记录每个节点的后继节点（一般来说有两个）
    nxt = {}
    
    # 建图   
    for crossing in pd_code:
        add_edge(nxt, crossing[0], crossing[2])
        add_edge(nxt, crossing[1], crossing[3])

    vis = []
    components = []
    for node_name in nxt:
        if node_name not in vis:
            arr = []
            dfs(nxt, vis, arr, node_name)
            components.append(sorted(arr))
    
    return sorted(components)
