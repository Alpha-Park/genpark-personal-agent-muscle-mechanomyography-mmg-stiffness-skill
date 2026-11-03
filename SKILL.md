---
name: genpark-personal-agent-muscle-mechanomyography-mmg-stiffness-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating muscle mechanomyography (MMG), electromechanical delay (EMD), and peripheral muscular fatigue.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Muscle Mechanomyography (MMG) & Contractile Stiffness Skill

A sovereign personal agent capability for assessing skeletal muscle mechanical dynamics, motor unit firing frequency, and electromechanical coupling latency via acoustic myography.

## Core Capabilities
- **Acoustic Myography Analysis**: Extracts RMS amplitude of intramuscular mechanical oscillations.
- **Mean Power Frequency (MPF)**: Determines motor unit discharge rate dynamics (15-35 Hz).
- **Electromechanical Delay (EMD)**: Measures the delay between electrical excitation (EMG) and force production (MMG).
- **Muscular Contractile Score**: 0-100 rating of muscular power output and fatigue resistance.

## Fast Invocation
```python
from client import MuscleMechanomyographyClient

client = MuscleMechanomyographyClient()
res = client.evaluate_mechanomyography(
    mmg_rms_amplitude_mv=1.92,
    mmg_mean_power_frequency_hz=27.4,
    electromechanical_delay_ms=33.5
)
print("EMD:", res["electromechanical_delay_ms"], "ms")
print("Mechanical Index:", res["neuromuscular_mechanical_coupling_index"])
print("Contractile Score:", res["muscular_contractile_score"])
```
