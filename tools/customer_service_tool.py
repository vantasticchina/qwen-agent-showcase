from tools.base_tool import BaseTool
from typing import Dict, Any


class CustomerInfoTool(BaseTool):
    """
    客户信息工具，用于查询用户个人信息和订单信息
    """
    
    def __init__(self):
        """
        初始化客户信息工具
        """
        super().__init__("customer_info", "Query customer information and order details")

        # 模拟客户数据库
        self.customer_db = {
            "user123": {
                "name": "张三",
                "email": "zhangsan@example.com",
                "phone": "138****8888",
                "level": "VIP",
                "orders": {
                    "ORD001": {
                        "product": "无线耳机",
                        "status": "已发货",
                        "tracking_number": "SF1234567890",
                        "delivery_date": "2023-10-15"
                    },
                    "ORD002": {
                        "product": "智能手表",
                        "status": "已签收",
                        "tracking_number": "YT0987654321",
                        "delivery_date": "2023-09-20"
                    }
                }
            },
            "user456": {
                "name": "李四",
                "email": "lisi@example.com",
                "phone": "139****9999",
                "level": "普通会员",
                "orders": {
                    "ORD003": {
                        "product": "蓝牙音箱",
                        "status": "处理中",
                        "tracking_number": "ZTO111222333",
                        "delivery_date": "预计2023-10-25"
                    }
                }
            }
        }

    def execute(self, params: Dict[str, Any]) -> str:
        """
        执行客户信息查询
        
        Args:
            params (Dict[str, Any]): 包含查询参数的字典
            
        Returns:
            str: 查询结果
        """
        query_type = params.get("query_type")
        user_id = params.get("user_id", "guest")
        
        if user_id not in self.customer_db:
            return f"未找到用户 {user_id} 的信息，请确认用户身份或联系客服。"
        
        customer = self.customer_db[user_id]
        
        if query_type == "profile":
            # 查询用户个人信息
            result = f"用户信息：\n"
            result += f"姓名：{customer['name']}\n"
            result += f"邮箱：{customer['email']}\n"
            result += f"手机号：{customer['phone']}\n"
            result += f"会员等级：{customer['level']}\n"
            result += f"订单数量：{len(customer['orders'])}个\n"
            
            return result
            
        elif query_type == "order":
            # 查询订单信息
            order_id = params.get("order_id")
            if not order_id:
                return "请提供订单号。"
            
            if order_id in customer['orders']:
                order = customer['orders'][order_id]
                result = f"订单 {order_id} 信息：\n"
                result += f"商品：{order['product']}\n"
                result += f"状态：{order['status']}\n"
                result += f"快递单号：{order['tracking_number']}\n"
                result += f"预计/实际送达日期：{order['delivery_date']}\n"
                
                return result
            else:
                return f"未找到订单号 {order_id} 的信息，请确认订单号是否正确。"
        
        else:
            return f"不支持的查询类型: {query_type}"