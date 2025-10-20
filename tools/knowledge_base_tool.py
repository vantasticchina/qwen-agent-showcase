from tools.base_tool import BaseTool
from typing import Dict, Any
import re


class KnowledgeBaseTool(BaseTool):
    """
    知识库工具，用于回答常见问题和提供帮助信息
    """
    
    def __init__(self):
        """
        初始化知识库工具
        """
        super().__init__("knowledge_base", "Answer common questions and provide help information")

        # 模拟知识库
        self.knowledge_base = {
            "退货政策": {
                "title": "退货政策",
                "content": "我们提供7天无理由退货服务。商品需保持原包装且未经使用。请联系客服获取退货标签。"
            },
            "配送时间": {
                "title": "配送时间",
                "content": "一般订单在1-3个工作日内发货，配送时间根据地区不同为2-7个工作日。"
            },
            "支付方式": {
                "title": "支付方式", 
                "content": "我们支持微信支付、支付宝、银联卡、信用卡等多种支付方式。"
            },
            "会员权益": {
                "title": "会员权益",
                "content": "VIP会员享受9折优惠、专属客服、生日礼物等特权。"
            },
            "产品保修": {
                "title": "产品保修",
                "content": "所有产品享受1年免费保修服务，保修期内非人为损坏可免费维修或更换。"
            }
        }

    def execute(self, params: Dict[str, Any]) -> str:
        """
        执行知识库查询
        
        Args:
            params (Dict[str, Any]): 包含查询参数的字典
            
        Returns:
            str: 查询结果
        """
        query = params.get("query", "").lower()
        
        # 通过关键词匹配查找相关条目
        matched_entries = []
        for keyword, entry in self.knowledge_base.items():
            # 检查关键词、标题或内容中是否包含查询词
            if (keyword.lower() in query or 
                entry['title'].lower() in query or 
                any(kw in query for kw in [keyword.lower(), entry['title'].lower()]) or
                query in entry['content'].lower()):
                matched_entries.append(entry)
        
        # 如果没有精确匹配，尝试模糊匹配
        if not matched_entries:
            for keyword, entry in self.knowledge_base.items():
                # 检查是否包含相关词汇
                if any(token in query for token in ['配送', 'delivery', '时间', '多久', '天']) and '配送时间' in entry['title']:
                    matched_entries.append(entry)
                elif any(token in query for token in ['退货', 'return', '政策', '退款']) and '退货政策' in entry['title']:
                    matched_entries.append(entry)
                elif any(token in query for token in ['支付', '付款', '方式', 'pay']) and '支付方式' in entry['title']:
                    matched_entries.append(entry)
                elif any(token in query for token in ['会员', '权益', '特权', 'VIP']) and '会员权益' in entry['title']:
                    matched_entries.append(entry)
                elif any(token in query for token in ['保修', '维修', '售后']) and '产品保修' in entry['title']:
                    matched_entries.append(entry)
        
        if matched_entries:
            # 如果找到匹配项，返回相关内容
            result = "根据您的问题，找到以下相关信息：\n\n"
            for i, entry in enumerate(matched_entries, 1):
                result += f"{i}. {entry['title']}\n"
                result += f"   {entry['content']}\n\n"
            return result
        else:
            # 如果没找到匹配项，提供通用帮助信息
            all_topics = "、".join(self.knowledge_base.keys())
            return f"抱歉，我没有找到与您问题直接相关的信息。我们的知识库包含以下主题：{all_topics}。\n您可以重新表述问题，或联系人工客服获取更详细的帮助。"