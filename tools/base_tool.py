from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """
    工具基类，定义了工具的基本接口
    """
    
    def __init__(self, name: str, description: str):
        """
        初始化工具
        
        Args:
            name (str): 工具名称
            description (str): 工具描述
        """
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, params: Dict[str, Any]) -> str:
        """
        执行工具的抽象方法，子类必须实现
        
        Args:
            params (Dict[str, Any]): 工具执行参数
            
        Returns:
            str: 工具执行结果
        """
        pass