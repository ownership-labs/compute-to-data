# Compute-to-Data

## 概览

该项目基于分布式数据管理中间件DataToken和Rosetta隐私AI框架来实现可追溯且隐私保护的机器学习，由此构建了允许第三方执行远程计算的私域数据资产服务网格。rtt_tracer为基于flask架构的资产部署工具，帮助资产方快速定义本地计算服务并自动校验外部计算请求。client为面向第三方科学家的服务请求工具，以完成数据可用不可见情况下的机器学习。

## MVP体验

### 交互过程

考虑简单的联合风控场景，第三方金融科技公司C为两家银行A、B提供模型服务。银行A和银行B的客户数据位于私域数据库中，在保证数据隐私安全且操作可审计的情况下，允许接收第三方的联合风控模型，确认服务条款后授权以执行本地计算，最终对外提供结果。通过使用DataToken SDK，资产方可在区块链数据市场上对数据的计算权进行交易，完成数据资产货币化。

### 运行demo

我们在[samples](./samples)中提供了用于快速测试的配置文件、数据集、资产元信息、联合风控模型等。本地计算所需的资源、运行日志等被存储在[tests](./tests)中，每一次计算将自动创建对应job_id的文件夹，自动获取所需的数据、模型和参数等。这相当于简单模拟一个私域计算沙箱。查看完整的demo[操作流程](./demo.md)。
