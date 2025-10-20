import json
import os
from typing import Any, Dict


def save_to_file(data: Any, file_path: str, format: str = 'json'):
    """
    将数据保存到文件
    
    Args:
        data (Any): 要保存的数据
        file_path (str): 文件路径
        format (str): 文件格式 ('json', 'txt')
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        if format == 'json':
            json.dump(data, f, ensure_ascii=False, indent=2)
        elif format == 'txt':
            f.write(str(data))


def load_from_file(file_path: str, format: str = 'json'):
    """
    从文件加载数据
    
    Args:
        file_path (str): 文件路径
        format (str): 文件格式 ('json', 'txt')
        
    Returns:
        从文件加载的数据
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        if format == 'json':
            return json.load(f)
        elif format == 'txt':
            return f.read()


def format_response(response: str, max_length: int = 1000) -> str:
    """
    格式化响应，限制长度
    
    Args:
        response (str): 原始响应
        max_length (int): 最大长度
        
    Returns:
        格式化后的响应
    """
    if len(response) > max_length:
        return response[:max_length] + "\n[内容已截断]"
    return response