# Superpowers & GStack 技能包

本仓库已集成两个热门 AI 编程技能框架：

## Superpowers (obra)

来自 https://github.com/obra/superpowers

核心方法论框架，包含：
- **brainstorming** - 创意前的设计探索（必须先使用）
- **writing-plans** - 多步骤任务的实施计划
- **writing-skills** - 创建和维护技能文件
- **systematic-debugging** - 系统化调试（先调查再修复）
- **test-driven-development** - TDD 工作流
- **verification-before-completion** - 完成前的验证检查

## GStack (Garry Tan)

来自 https://github.com/garrytan/gstack

23个专业角色技能，包含：
- **office-hours** - 产品头脑风暴起点
- **review** - PR 代码审查
- **ship** - 发布工作流
- **qa** - 质量保证测试
- **design-review** - 视觉审计
- **investigate** - 系统化调试

## 自动触发

这些技能会根据任务类型自动加载：
- 开始新功能前 → brainstorming
- 修复 bug 前 → systematic-debugging
- 完成工作前 → verification-before-completion
- 准备发布时 → ship

## 手动调用

```
superpowers:brainstorming
superpowers:writing-plans
gstack:review
gstack:ship
```
