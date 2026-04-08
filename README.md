# Delivery Optimization Environment

## Description
Simulates a delivery agent completing package deliveries under time constraints.

## Actions
- DELIVER

## State
- packages_left
- time_left

## Reward
- +10 for delivery
- -1 for invalid action

## Tasks
- Easy: 1 package
- Medium: 3 packages
- Hard: 5 packages

## Run
python inference.py