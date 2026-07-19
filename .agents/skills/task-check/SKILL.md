---
name: task-check
description: Validates the user's latest code edits (SQL DDL/DML, Python) for correctness. Use when the user requests a code check, completes a task, or when validating syntax before moving to the next roadmap phase.
---

# Task Check Skill

## Purpose
This skill establishes a strict validation loop for the user's coding tasks. It ensures that no code with syntax errors, incorrect datatypes, or missing constraints is permitted to pass without correction, maintaining high project standards.

## Workflow

1. **Locate & Read the Code:**
   * Find the file related to the user's most recent task (e.g., `sql/create_tables.sql`, `data/db_setup.py`, etc.).
   * Read the file contents using filesystem viewing tools.

2. **Verify Correctness:**
   * Analyze the code for syntax errors (e.g., trailing commas, spelling mistakes in keywords, misplaced syntax).
   * Check for logical requirements (e.g., proper foreign key relationships, correct decimal precision for money, appropriate date/time types, specific check constraints).
   * Validate against the current roadmap goals.

3. **Respond & Guide:**
   * **If the code is 100% correct:**
     * State clearly that the code is correct.
     * Update/check the task off in `project/roadmap.md` if necessary.
     * Transition the user directly to the next task in the roadmap.
   * **If the code has errors or needs improvement:**
     * **Do NOT** proceed to the next task.
     * Clearly explain the error or logical issue.
     * Provide the correct code block in the chat interface.
     * **Do NOT** edit the file directly; let the user make the correction.
     * Guide them step-by-step until the code passes validation.
