# Welcome to TasTrack
Tastrack is a cli-based app, that allow you manage you tasks using a few commands.
# TasTrack CLI - Quick Guide

## Commands

### Basic Operations
```bash
# Add new task
task-cli add "Task description"

# Update task
task-cli update  "New description"

# Delete task
task-cli delete 
```

### Status Management
```bash
# Mark progress
task-cli mark-in-progress 
task-cli mark-done 
```

### View Tasks
```bash
# List all tasks
task-cli list

# Filter by status
task-cli list todo
task-cli list in-progress
task-cli list done
```

## Task Structure
- `id`: Unique identifier
- `description`: Task details
- `status`: todo/in-progress/done
- `createdAt`: Creation timestamp
- `updatedAt`: Last modified timestamp

## Notes
- Tasks stored in local `tasks.json`
- Use quotes for descriptions with spaces