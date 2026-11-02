

# --- 工具描述（OpenAI Function Calling 格式）---
TOOLS: list = []
TOOL_FUNCTIONS: dict = {}


def func_to_tool(func):
    """将普通函数转换成 OpenAI Function Calling 的工具定义格式"""
    maps: dict = {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean",
    }
    
    doc = func.__doc__
    arg = doc.find('Args:')
    ret = doc.find('Returns:')
    exam = doc.find('Example:')

    func_desc = doc[:arg] + doc[exam:]
    arg_desc = doc[arg:ret]

    properties: dict = {}
    required: list = []
    for line in arg_desc.split('\n'):
        if line.strip() and not line.strip().startswith('Args:'):
            param_name_type, param_desc = line.strip().split('; ')
            name, type_ = param_name_type.split(': ')
            if '=' in type_:
                # 有默认值的参数
                type_, default = type_.split(' = ')
            else:
                # 没有默认值的参数
                default = None
                required.append(name)

            properties[name] = {
                "type": maps.get(type_, type_),
                "default": default,
                "description": param_desc,
            }
            
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": func_desc or "",
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            }
        }
    }


def tool(func):
    """装饰器，将普通函数转换成工具定义，并注册到 TOOL_FUNCTIONS 中"""
    tool_def = func_to_tool(func)
    TOOLS.append(tool_def)
    TOOL_FUNCTIONS[func.__name__] = func

    return func


# --- 具体工具函数实现 ---
@tool
def get_current_time(format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """获取当前时间。
    返回当前系统时间，用户可以指定时间格式。
    Args:
        format_str: str = "%Y-%m-%d %H:%M:%S"; 时间格式字符串，例如 "%Y-%m-%d" 或 "%H:%M:%S"。
    Returns:
        str; 格式化后的当前时间字符串。
    Example:
        get_current_time("%Y-%m-%d") -> "2026-06-01"
    """

    try:
        from datetime import datetime
        return datetime.now().strftime(format_str)
    
    except Exception as e:
        return f"获取当前时间出错: {str(e)}"
