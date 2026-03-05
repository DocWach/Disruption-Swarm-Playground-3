# Disruption Swarm Playground 3

A personal development playground built on **Ruflo** (formerly Claude Flow) — an enterprise AI agent orchestration framework for Claude Code.

## What's Inside

| Directory | Description |
|-----------|-------------|
| `ruflo/` | Ruflo package source — CLI, MCP bridge, chat UI, NGINX, config |
| `v3/` | V3 architecture — DDD domains, security, memory, CLI, shared packages |
| `v2/` | Legacy V2 implementation |
| `agents/` | Agent definitions and configurations |
| `plugin/` | Plugin system |
| `scripts/` | Utility and build scripts |
| `tests/` | Test suites |
| `bin/` | CLI entry points |

## About Ruflo

Ruflo is a multi-agent AI orchestration platform that turns Claude Code into a coordinated swarm of 60+ specialized agents.

```
User → Ruflo (CLI/MCP) → Router → Swarm → Agents → Memory → LLM Providers
                       ↑                          ↓
                       └──── Learning Loop ←──────┘
```

### Quick Start

```bash
# Initialize a project
npx ruflo@latest init --wizard

# Spawn an agent
ruflo agent spawn -t coder

# Start a swarm
ruflo swarm init --topology hierarchical --max-agents 8

# Search vector memory
ruflo memory search --query "authentication patterns"

# System diagnostics
ruflo doctor
```

### Key Features

- **60+ Agent Types** — coder, reviewer, tester, architect, security, researcher, and more
- **Swarm Topologies** — hierarchical, mesh, ring, star
- **Vector Memory** — AgentDB with HNSW indexing (150x–12,500x faster search)
- **Self-Learning** — RuVector intelligence pipeline (RETRIEVE → JUDGE → DISTILL → CONSOLIDATE)
- **MCP Integration** — Works as a Model Context Protocol server for Claude Code
- **Fault-Tolerant Consensus** — Raft, BFT, Gossip, CRDT

### Add as MCP Server

```bash
claude mcp add ruflo -- npx -y ruflo@latest mcp start
```

## Development

```bash
npm install
npm run build
npm test
```

**Requirements:** Node 20+

## Upstream

- npm: [npmjs.com/package/ruflo](https://www.npmjs.com/package/ruflo) / [npmjs.com/package/claude-flow](https://www.npmjs.com/package/claude-flow)
- Source: [github.com/ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

## License

MIT
