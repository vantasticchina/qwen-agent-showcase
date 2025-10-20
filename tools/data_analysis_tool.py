import pandas as pd
import matplotlib.pyplot as plt
from tools.base_tool import BaseTool
from typing import Dict, Any
import os


class DataAnalysisTool(BaseTool):
    """
    数据分析工具，用于读取、分析和可视化数据
    """
    
    def __init__(self):
        """
        初始化数据分析工具
        """
        super().__init__("data_analysis", "Analyze data and generate insights")

    def execute(self, params: Dict[str, Any]) -> str:
        """
        执行数据分析
        
        Args:
            params (Dict[str, Any]): 包含数据路径和查询的参数字典
            
        Returns:
            str: 数据分析结果
        """
        try:
            data_path = params.get("data_path")
            query = params.get("query", "")
            
            if not data_path:
                return "错误：未提供数据路径"
            
            # 检查文件是否存在
            if not os.path.exists(data_path):
                return f"错误：文件 {data_path} 不存在"
            
            # 读取数据
            if data_path.endswith('.csv'):
                df = pd.read_csv(data_path)
            elif data_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(data_path)
            elif data_path.endswith('.json'):
                df = pd.read_json(data_path)
            else:
                return f"错误：不支持的文件格式: {data_path}"
            
            # 基本数据分析
            result = f"数据文件 {data_path} 分析结果：\n"
            result += f"数据形状: {df.shape}\n"
            result += f"列名: {list(df.columns)}\n"
            
            # 数值列统计
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if numeric_cols:
                result += f"\n数值列统计:\n{df[numeric_cols].describe()}\n"
                
                # 如果有多个数值列，生成相关性矩阵
                if len(numeric_cols) > 1:
                    correlation = df[numeric_cols].corr()
                    result += f"\n数值列相关性:\n{correlation}\n"
            
            # 如果查询包含可视化请求，生成图表
            if any(visual_keyword in query.lower() for visual_keyword in ['plot', 'chart', 'graph', 'visual', '图', '可视化']):
                # 生成简单的柱状图
                plt.figure(figsize=(10, 6))
                
                # 如果有数值列，绘制第一列的直方图
                if numeric_cols:
                    plt.hist(df[numeric_cols[0]].dropna(), bins=20)
                    plt.title(f'{numeric_cols[0]} 分布直方图')
                    plt.xlabel(numeric_cols[0])
                    plt.ylabel('频次')
                    
                    # 保存图表
                    chart_path = data_path.rsplit('.', 1)[0] + '_chart.png'
                    plt.savefig(chart_path)
                    plt.close()
                    
                    result += f"\n已生成图表并保存至: {chart_path}"
            
            return result
        except FileNotFoundError:
            return f"错误：找不到文件 {data_path}"
        except pd.errors.EmptyDataError:
            return "错误：数据文件为空"
        except pd.errors.ParserError:
            return "错误：数据文件解析失败"
        except Exception as e:
            return f"数据分析时出错：{type(e).__name__}: {str(e)}"