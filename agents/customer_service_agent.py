from agents.base_agent import BaseAgent
from tools.customer_service_tool import CustomerInfoTool
from tools.knowledge_base_tool import KnowledgeBaseTool
from core.config import Config


class CustomerServiceAgent(BaseAgent):
    """
    智能客服机器人 Agent，处理客户咨询、查询用户信息和知识库
    """
    
    def __init__(self, config: Config):
        """
        初始化客服 Agent
        
        Args:
            config (Config): 配置对象
        """
        super().__init__(config)
        self.add_tool(CustomerInfoTool())
        self.add_tool(KnowledgeBaseTool())

    def process_request(self, user_input: str) -> str:
        """
        处理客户服务请求
        
        Args:
            user_input (str): 用户输入的客服请求
            
        Returns:
            str: 客服机器人的响应
        """
        import re
        
        # 检测用户ID（模拟从认证系统获取）
        user_id = getattr(self, 'current_user_id', 'guest')
        
        # 识别请求类型
        if any(keyword in user_input.lower() for keyword in ["订单", "购买", "订单号", "order", "购买记录"]):
            # 处理订单查询请求
            # 改进的正则表达式以匹配更广泛的订单号格式
            possible_matches = [
                re.search(r'订单号[:：\s]*(\w+)', user_input),
                re.search(r'order[ \w]*[:：\s]*(\w+)', user_input, re.IGNORECASE),
                re.search(r'订单[:：\s]*(\w+)', user_input)
            ]
            
            order_match = None
            order_id = None
            
            # 查找第一个有效的匹配
            for match in possible_matches:
                if match:
                    order_match = match
                    order_id = match.group(1)
                    break
            
            # 如果没有通过上述方式匹配到，尝试从整个输入中提取可能的订单号
            if not order_id:
                # 查找形如 ORD001 的模式
                alt_match = re.search(r'([A-Z]{2,}[0-9]{2,})', user_input.upper())
                if alt_match:
                    order_id = alt_match.group(1)
            
            if order_id:
                info_tool = self.tools[0]  # CustomerInfoTool
                result = info_tool.execute({"query_type": "order", "order_id": order_id, "user_id": user_id})
                return result
            else:
                return "请提供订单号以便查询订单信息。"
        
        elif any(keyword in user_input for keyword in ["个人信息", "账户", "资料", "profile", "信息"]):
            # 处理个人信息查询请求
            info_tool = self.tools[0]  # CustomerInfoTool
            result = info_tool.execute({"query_type": "profile", "user_id": user_id})
            return result
        
        elif any(keyword in user_input.lower() for keyword in ["怎么办", "怎么解决", "如何", "help", "帮助", "怎么办", "问题"]):
            # 处理知识库查询请求
            kb_tool = self.tools[1]  # KnowledgeBaseTool
            result = kb_tool.execute({"query": user_input})
            return result
        else:
            # 默认查询知识库
            kb_tool = self.tools[1]  # KnowledgeBaseTool
            result = kb_tool.execute({"query": user_input})
            return result