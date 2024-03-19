该项目对纽约市出租车委员会（NYC TLC）的数据集进行预处理和分析，为出租车管理公司提供咨询服务。
该研究主要分为两个部分：
-  对重大节假日，我们使用了geopandas包绘制heatmap，结合统计数据，分析当天出租车运营推荐区域，提高精确度
-  对大部分数据，使用天气和日期数据，训练决策树回归模型，用于对未来某年给定日期、星期、天气的条件下，出租车的需求情况进行预测。

文件说明：
1. **data**：存储了从官方网站上存储的源数据和处理后的csv文件
2. **New York City Taxi Data Exploration.ipynb**：该项目的主要文件，穿插代码和文字说明，详细地介绍了该项目的研究过程和结果。
3. **environment.yml**：记录了本项目所需要配置的python环境
4. **event-exploration.ipynb**：是在探索纽约具体到某日的出租车运营情况时使用的代码，便于发现异常数据点
5. **weather-investigation.ipynb**、**investigation.ipynb**：分析过程中探索数据规律的代码
6. **utils.py**：研究过程中使用的自定义函数，用于数据预处理

The project preprocesses and analyzes data sets from the New York City Taxi Commission (NYC TLC) to provide consulting services to taxi management companies.
The study is divided into two main parts:
- For holidays or special events' date, we use geopandas package to draw heatmap and analyze the recommended areas for taxi operation on the day with statistical data to improve the accuracy
- weather and date data are used for other regular date, and the decision tree regression model is trained to predict the demand for taxis under the conditions of a given date, week and weather in a future year.

Document description:
1. **data** folder: stores the source data stored from the official website and the processed csv file
2. **New York City Taxi Data Exploration.ipynb**: The main document of the project, interspersed with codes and text descriptions, introduced the research process and results of the project in detail.
3. **Environment. yml**: Records the python environment that needs to be configured for this project
4. **event-exploration.ipynb**: This is the code used to explore the operation of taxis in New York City on a specific day to facilitate the detection of abnormal data points
5. **weather-investigation.ipynb**, investigation.ipynb: code to explore data rules in the analysis process
6. **utils.py**: Custom function used in the research process for data preprocessing
