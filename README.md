# Disruption Swarm Playground 3

A safe sandbox for learning Claude Code and Claude Flow. Experiment freely — nothing here is precious.

## What's Inside

| File | Purpose |
|------|---------|
| `src/analyze_data.py` | Sample Python script with a deliberate bug to practice debugging |
| `src/utils.py` | Utility functions to explore and modify |
| `data/sensor_readings.csv` | Sample dataset for analysis tasks |
| `paper_draft.md` | Short paper draft to practice editing and review |
| `CLAUDE.md` | Starter project instructions for Claude Code |

## Exercises

1. **Explore**: Start `claude` and ask it to describe this project's structure.
2. **Debug**: Ask Claude to find and fix the bug in `src/analyze_data.py`.
3. **Edit**: Ask Claude to add a new column calculation to the analysis script.
4. **Review**: Ask Claude to review `paper_draft.md` and suggest improvements.
5. **Memory**: Store a finding with `claude-flow memory store --key "exercise-1" --value "your finding" --namespace practice`.
6. **Swarm**: Run `claude-flow swarm init --topology hierarchical --max-agents 3 --strategy specialized` and route a task.

## Setup

See the [Getting Started Guide](https://github.com/DocWach/Disruption-Swarm-Setup/blob/main/docs/claude-flow-getting-started.md).
