from agents.base_agent import BaseAgent
from tools.weather_tool import WeatherTool
from core.config import Config


class WeatherAgent(BaseAgent):
    """
    天气查询 Agent，专门处理天气相关的查询请求
    """
    
    def __init__(self, config: Config):
        """
        初始化天气 Agent
        
        Args:
            config (Config): 配置对象
        """
        super().__init__(config)
        self.add_tool(WeatherTool())

    def process_request(self, user_input: str) -> str:
        """
        处理天气查询请求
        
        Args:
            user_input (str): 用户输入的天气查询请求
            
        Returns:
            str: 天气查询结果
        """
        # 检查输入是否包含城市信息
        if "天气" in user_input or "weather" in user_input.lower():
            # 提取城市名称（这里简化处理，实际可能需要NLP技术）
            import re
            city_match = re.search(r'([A-Za-z\u4e00-\u9fa5]+)的天气|weather in ([A-Za-z\u4e00-\u9fa5]+)', user_input)
            city = None
            if city_match:
                city = city_match.group(1) or city_match.group(2)
            else:
                # 如果没有明确城市，尝试从记忆中获取
                for item in reversed(self.memory):
                    if "city" in item.get("content", ""):
                        import json
                        try:
                            content = json.loads(item["content"])
                            city = content.get("city")
                        except:
                            pass
                        break
            
            if city:
                # 使用天气工具查询
                weather_tool = self.tools[0]  # 假设天气工具是第一个
                result = weather_tool.execute({"city": city})
                return result
            else:
                return "请提供您想查询天气的城市名称。"
        else:
            return "我是天气查询助手，可以帮您查询指定城市的天气信息。"