from abc import ABC, abstractmethod
from typing import Any, Dict, List
from tools.base_tool import BaseTool
from core.config import Config


class BaseAgent(ABC):
    """
    Agent 基类，定义了 Agent 的基本接口和通用功能
    """
    
    def __init__(self, config: Config):
        """
        初始化 Agent
        
        Args:
            config (Config): 配置对象
        """
        self.config = config
        self.tools: List[BaseTool] = []
        self.memory = []

    def add_tool(self, tool: BaseTool) -> None:
        """
        添加工具到 Agent
        
        Args:
            tool (BaseTool): 工具实例
        """
        self.tools.append(tool)

    @abstractmethod
    def process_request(self, user_input: str) -> str:
        """
        处理用户请求的抽象方法，子类必须实现
        
        Args:
            user_input (str): 用户输入
            
        Returns:
            str: 处理结果
        """
        pass

    def get_response(self, user_input: str) -> str:
        """
        获取 Agent 的响应
        
        Args:
            user_input (str): 用户输入
            
        Returns:
            str: Agent 响应
        """
        self.memory.append({"role": "user", "content": user_input})
        response = self.process_request(user_input)
        self.memory.append({"role": "assistant", "content": response})
        return response