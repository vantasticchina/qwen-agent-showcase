from typing import Dict, Any


class Config:
    """
    配置管理类
    """
    
    def __init__(self, config_dict: Dict[str, Any] = None):
        """
        初始化配置
        
        Args:
            config_dict (Dict[str, Any]): 配置字典
        """
        self._config = config_dict or {}
        
    def get(self, key: str, default=None):
        """
        获取配置值
        
        Args:
            key (str): 配置键
            default: 默认值
            
        Returns:
            配置值或默认值
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        设置配置值
        
        Args:
            key (str): 配置键
            value (Any): 配置值
        """
        self._config[key] = value
        
    def update(self, config_dict: Dict[str, Any]):
        """
        更新配置
        
        Args:
            config_dict (Dict[str, Any]): 配置字典
        """
        self._config.update(config_dict)