---
name: superpowers
description: "Core agentic skills framework for AI-assisted software development - brainstorming, planning, debugging, TDD, and verification"
tags:
  - ai-agent
  - development
  - workflow
  - brainstorming
  - debugging
  - tdd
---

# Superpowers - Agentic Skills Framework

Core skills from https://github.com/obra/superpowers - a methodology for AI-assisted software development.

## Included Skills

### Planning Phase
- **brainstorming** - MUST use before any creative work. Explores user intent, requirements, and design before implementation.
- **writing-plans** - Use when you have a spec or requirements for a multi-step task, before touching code.
- **writing-skills** - Create and maintain reusable skill files.

### Implementation Phase
- **test-driven-development** - Write tests first, then implement.
- **systematic-debugging** - Root cause analysis before fixes.

### Verification Phase
- **verification-before-completion** - Comprehensive checks before marking work done.

## Usage

These skills are automatically loaded. Key triggers:

1. **Before building anything new** → use `superpowers:brainstorming`
2. **Before implementing a plan** → use `superpowers:writing-plans`
3. **Before fixing bugs** → use `superpowers:systematic-debugging`
4. **Before completing work** → use `superpowers:verification-before-completion`

## Key Principles

1. **Never skip brainstorming** - Even "simple" projects need design review
2. **TDD by default** - Write tests first, then implement
3. **Debug systematically** - Investigate root cause before fixing
4. **Verify before completing** - Run tests, check docs, verify behavior

## Sub-skills

- `superpowers:brainstorming` - Design exploration
- `superpowers:writing-plans` - Implementation planning
- `superpowers:writing-skills` - Skill creation
- `superpowers:systematic-debugging` - Bug investigation
- `superpowers:test-driven-development` - TDD workflow
- `superpowers:verification-before-completion` - Final checks
