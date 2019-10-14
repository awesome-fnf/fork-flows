## 简介

通过在主流程启动子流程打破单流程 Events 个数限制，子流程会在执行结束后将结果汇报给主流程。

**使用步骤**

1. 使用[Funcraft](https://help.aliyun.com/document_detail/64204.html)部署函数

    ```fun deploy -t template.yml```

2. 使用[阿里云 CLI](https://help.aliyun.com/document_detail/122611.html) 创建流程。使用控制台请参见[文档](https://help.aliyun.com/document_detail/124155.html)。

    ```aliyun fnf CreateFlow --Description "main flow" --Type FDL --Name fnf-mainflow --Definition "$(<./flows/main.yaml)" --RoleArn acs:ram::account-id:role/fnf```

    ```aliyun fnf CreateFlow --Description "sub flow" --Type FDL --Name fnf-subflow --Definition "$(<./flows/subflow.yaml)" --RoleArn acs:ram::account-id:role/fnf```

3. Start mainflow。

    ```aliyun fnf StartExecution --FlowName fnf-mainflow --Input '{"executionName": "run1", "subflowName": "fnf-subflow", "keys": ["a", "b", "c"]}' --ExecutionName run1```