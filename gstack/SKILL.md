---
name: gstack
description: "Garry Tan's AI engineering workflow - 23 specialist skills for CEO review, design, QA, release, and more"
tags:
  - ai-agent
  - workflow
  - code-review
  - qa
  - release
  - ceo
---

# GStack - AI Engineering Workflow

Skills from https://github.com/garrytan/gstack - structured roles for AI agents in software development.

## Available Skills

### Planning Reviews
- **office-hours** - Start here. Reframes your product idea before you write code.
- **plan-ceo-review** - CEO-level review: find the 10-star product in the request.
- **plan-eng-review** - Lock architecture, data flow, edge cases, and tests.
- **plan-design-review** - Rate each design dimension 0-10, explain what a 10 looks like.

### Implementation + Review
- **review** - Pre-landing PR review. Finds bugs that pass CI but break in prod.
- **investigate** - Systematic root-cause debugging. No fixes without investigation.
- **design-review** - Live-site visual audit + fix loop with atomic commits.
- **qa** - Open a real browser, find bugs, fix them, re-verify.

### Release + Deploy
- **ship** - Run tests, review, push, open PR. Workspace-aware version queue.

## Usage

These skills are automatically loaded. Key triggers:

1. **New product idea** → use `gstack:office-hours`
2. **Before merging PR** → use `gstack:review`
3. **Found a bug** → use `gstack:investigate`
4. **Ready to ship** → use `gstack:ship`
5. **Need QA** → use `gstack:qa`

## Key Principles

1. **Review before shipping** - Never ship without review
2. **Investigate before fixing** - Understand root cause first
3. **QA with real browsers** - Test actual user experience
4. **Ship systematically** - Tests, review, push in sequence

## Sub-skills

- `gstack:office-hours` - Product brainstorming
- `gstack:review` - Code review
- `gstack:ship` - Release workflow
- `gstack:qa` - Quality assurance
- `gstack:design-review` - Visual audit
- `gstack:investigate` - Debugging
