### python json 库
- 存在 JSON 字符串,可以使用 `json.loads()` 方法解析,返回的是 Python 字典
- 存在 Python 字典,可以使用 `json.dumps()` 方法转换,返回的是 JSON 字符串
- dict list tuple string int float True False None 均可以使用 `dumps` 方法转换
- 当 Python 转换为 JSON 时，Python 对象会被转换为 JSON（JavaScript）Python-JSON等效项： dict-Object list-Array tuple-Array str-String int-Number float-Number True-true False-false None-null
- JSON 输出格式化缩进 `json.dumps(x, indent=4)`
- JSON 输出格式化分隔符 `json.dumps(x, indent=4, separators=(", ", " = "))`
- JSON 输出格式化结果排序 `json.dumps(x, indent=4, sort_keys=True)`
- JSON 输出格式化不需要 ascii 输出 `json.dumps(x, ensure_ascii=False)`
  - 应对原内容里有非英文字母的场景
- JSON type always be str `type(json.dumps(x))`