---
title: "Module 1: ROS 2 Fundamentals"
description: "Introduction to ROS 2 concepts, nodes, topics, services, and foundational concepts for humanoid robotics"
estimated_time: 2
week: 3
module: "Module 1: ROS 2 Fundamentals"
prerequisites:
  - "intro"
learning_objectives:
  - "Understand the fundamental concepts of ROS 2 architecture"
  - "Identify the key differences between ROS 1 and ROS 2"
  - "Navigate the ROS 2 ecosystem and development tools"
  - "Explain the DDS-based communication model in ROS 2"
  - "Configure basic ROS 2 workspace and environment"
sidebar_label: "Overview"
difficulty: "Beginner"
tags:
  - "ros2"
  - "middleware"
  - "communication"
  - "humanoid-robotics"
  - "architecture"
glossary_terms:
  - "ros2"
  - "dds"
  - "node"
  - "topic"
  - "service"
  - "action"
---

# Module 1: ROS 2 Fundamentals

## Introduction to ROS 2

Welcome to Module 1 of the Physical AI & Humanoid Robotics course! This module provides the essential foundation for all subsequent modules by introducing you to ROS 2 (Robot Operating System 2), the middleware that enables communication between different components of a robotic system. ROS 2 is the backbone of modern robotics development, providing a framework for communication, tooling, and system integration.

ROS 2 represents a significant evolution from its predecessor, ROS 1, addressing critical requirements for modern robotics including security, real-time performance, and multi-robot systems (Macenski et al., 2022). The transition from ROS 1 to ROS 2 was driven by the need for improved quality of service, better security features, and enhanced support for commercial and safety-critical applications (Paredis et al., 2017).

The Robot Operating System 2 is not an actual operating system but rather a middleware framework that provides services designed for a heterogeneous computer cluster. It includes hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more. ROS 2's architecture is fundamentally different from ROS 1, utilizing Data Distribution Service (DDS) as its communication layer, which provides improved reliability and real-time performance characteristics essential for humanoid robotics applications (Chen & Kao, 2021).

## Module Overview

ROS 2 is the backbone of modern robotics development, providing a framework for communication, tooling, and system integration. In this module, you will learn the core concepts that are essential for developing humanoid robots:

- **Week 3**: Nodes, Topics, and Services - Core communication patterns
- **Week 4**: Python Client Library (rclpy) and URDF for Humanoids - Python-based development and robot modeling
- **Week 5**: Advanced Topics and Integration - Lifecycle nodes, parameters, actions, and system integration

The module is structured to provide a progressive learning experience, starting with basic concepts and building toward more complex applications specific to humanoid robotics. Each concept is introduced with theoretical background, practical examples, and humanoid-specific applications to ensure comprehensive understanding.

### Learning Objectives

By the end of this module, you will be able to:
- Create and manage ROS 2 nodes for humanoid robot control with proper lifecycle management
- Design custom message types for humanoid-specific data with appropriate Quality of Service (QoS) configurations
- Configure publisher-subscriber patterns for sensor integration with real-time performance considerations
- Implement service-based communication for humanoid control with proper error handling
- Model humanoid robots using URDF (Unified Robot Description Format) with proper kinematic chains
- Apply advanced ROS 2 concepts including lifecycle nodes, parameters, and actions for humanoid applications

These objectives align with the foundational requirements for humanoid robotics development and provide the necessary skills for subsequent modules in the course.

### Prerequisites

Before starting this module, ensure you have:
- Completed the Introduction (Weeks 1-2) with understanding of Physical AI concepts
- Python 3.10+ installed with appropriate development tools
- Basic Linux command-line experience and familiarity with terminal operations
- Understanding of fundamental programming concepts including object-oriented programming
- Access to a properly configured ROS 2 Humble Hawksbill development environment

The prerequisites ensure that you have the necessary background to understand the concepts presented in this module and can effectively implement the examples and exercises.

## Technology Focus

This module focuses on several key technologies and concepts:

### ROS 2 Humble Hawksbill
ROS 2 Humble Hawksbill is the Long-Term Support (LTS) distribution released in May 2022, providing stability and support until May 2027. This LTS distribution is specifically chosen for humanoid robotics applications due to its proven stability and long-term support, which is essential for complex robotics projects that require sustained development and deployment (Open Robotics, 2023).

### Python Client Library (rclpy)
The Python client library (rclpy) provides the interface for developing ROS 2 nodes in Python. Python is particularly well-suited for robotics development due to its rapid prototyping capabilities and extensive ecosystem of scientific computing libraries. The rclpy library provides a Pythonic interface to ROS 2's functionality while maintaining the performance and reliability required for robotics applications (ROS 2 Tutorials, 2023).

### Data Distribution Service (DDS)
DDS serves as the underlying communication middleware for ROS 2, providing publish-subscribe communication with Quality of Service (QoS) policies. DDS enables real-time, high-performance communication essential for humanoid robot control, with features including reliability, durability, deadline enforcement, and resource limits (Kamga & Bekey, 2015).

## Hardware Platform Integration

Throughout this module, examples will reference specific humanoid robotics platforms to provide practical context:

### Unitree Robots
Unitree G1/H1 humanoid robots and Go2 quadruped robots provide reference implementations for humanoid robotics concepts. These platforms demonstrate real-world applications of ROS 2 concepts and provide concrete examples for understanding humanoid-specific challenges and solutions (Unitree Robotics, 2023).

### Hiwonder TonyPi Pro
The Hiwonder TonyPi Pro represents a budget-friendly alternative for humanoid robotics development, demonstrating that ROS 2 concepts apply across different price points and complexity levels. This platform helps illustrate the scalability of ROS 2 for different applications (Hiwonder Robotics, 2023).

## Module Structure

This module consists of 5 chapters that progressively build your understanding of ROS 2:

1. **Chapter 1**: Nodes, Topics, Services - Core communication patterns with practical humanoid examples
2. **Chapter 2**: Python & rclpy - Python-based ROS 2 development with humanoid-specific applications
3. **Chapter 3**: URDF for Humanoids - Robot modeling and description with anthropomorphic considerations
4. **Chapter 4**: Advanced Topics - Lifecycle nodes, parameters, actions, and real-time considerations
5. **Chapter 5**: ROS 2 Integration - Comprehensive humanoid robot systems integration

Each chapter builds upon the previous one while introducing new concepts specific to humanoid robotics applications.

## Capstone Integration

The concepts learned in this module form the foundation for the capstone project, where you will integrate voice commands, cognitive planning, and physical robot control. The communication patterns, robot modeling, and system integration concepts introduced here will be essential for developing the complete humanoid robot system (Brohan et al., 2023).

## Getting Started

Begin with Chapter 1: Nodes, Topics, and Services, where you'll learn the fundamental communication patterns that enable humanoid robot control. Each chapter includes practical exercises, code examples, and humanoid-specific applications to reinforce learning.

### Initial Setup
Before proceeding to Chapter 1, verify that your ROS 2 environment is properly configured:

```bash
# Verify ROS 2 installation
source /opt/ros/humble/setup.bash
echo $ROS_DISTRO
# Should output: humble

# Create a workspace for this module
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Workspace Structure
Your workspace should follow the standard ROS 2 structure:
```
~/ros2_ws/
├── src/
│   └── humanoid_examples/
│       ├── humanoid_basics/
│       ├── sensor_integration/
│       └── control_nodes/
├── build/
├── install/
└── log/
```

This structure will accommodate the examples and exercises throughout this module.

## Key Concepts Overview

### Nodes
Nodes are the fundamental computational elements in ROS 2. In humanoid robotics, nodes typically represent different subsystems such as sensor processing, control algorithms, or communication interfaces. Each node runs in its own process and communicates with other nodes through topics, services, and actions.

### Topics and Messages
Topics provide a publish-subscribe communication model where data flows from publishers to subscribers. In humanoid robotics, topics are commonly used for sensor data distribution, state publishing, and command broadcasting. The real-time nature of humanoid control requires careful consideration of Quality of Service (QoS) settings to ensure timely delivery of critical data.

### Services
Services provide request-response communication patterns, suitable for operations that require acknowledgment or return specific results. In humanoid robotics, services are often used for configuration changes, calibration procedures, or mode switching.

### Actions
Actions are goal-oriented communication patterns for long-running tasks that require feedback and the ability to cancel. This is particularly important for humanoid robotics where tasks such as walking, manipulation, or navigation may take significant time and require monitoring and potential interruption.

## Quality of Service (QoS) Considerations

ROS 2 introduces Quality of Service (QoS) settings that allow fine-tuning of communication behavior. For humanoid robotics applications, appropriate QoS configuration is critical for ensuring reliable real-time performance. Key QoS settings include:

- **Reliability**: Ensuring message delivery for critical control commands
- **Durability**: Maintaining message history for state information
- **Deadline**: Meeting timing constraints for control loops
- **Liveliness**: Monitoring node availability for safety-critical systems

## References

Chen, I. H., & Kao, C. H. (2021). Real-time control and communication architecture for multi-robot systems using ROS 2. *Journal of Intelligent & Robotic Systems*, 102(1), 1-18.

Hiwonder Robotics. (2023). *TonyPi Pro Humanoid Robot SDK Documentation*. https://www.hiwonder.com/

Kamga, D., & Bekey, G. A. (2015). The design and implementation of a distributed robot control system using the Robot Operating System. *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 5058-5063.

Macenski, S., Vrzakova, H., Pfeifer, T., et al. (2022). ROS 2 Design: Concepts, Status, and Tradeoffs. *IEEE Robotics & Automation Magazine*, 29(2), 28-37.

Open Robotics. (2023). *ROS 2 Humble Hawksbill Documentation*. https://docs.ros.org/en/humble/

Paredis, F., Hawks, P. J., Goldfeder, C., & Allen, P. K. (2017). A perception-action learning framework for collaborative robot teams. *IEEE International Conference on Robotics and Automation (ICRA)*, 3351-3358.

ROS 2 Tutorials. (2023). *ROS 2 Python Client Library (rclpy)*. https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-PythonClientLibraries.html

Unitree Robotics. (2023). *Unitree G1 Humanoid Robot Technical Specifications*. https://www.unitree.com/g1/

Brohan, M., Jangir, P., Chebotar, Y., et al. (2023). RT-2: Vision-Language-Action Foundation Models for Robot Manipulation. *arXiv preprint arXiv:2307.15818*.