---
title: "Glossary"
description: "Comprehensive glossary of robotics and AI terms used throughout the Physical AI & Humanoid Robotics textbook"
estimated_time: 1
week: 14
module: "References"
prerequisites: []
learning_objectives:
  - "Understand key terminology used throughout the textbook"
  - "Reference technical definitions for robotics and AI concepts"
  - "Connect terms to relevant chapters and concepts"
sidebar_label: "Glossary"
difficulty: "Beginner"
tags:
  - "glossary"
  - "terminology"
  - "definitions"
  - "robotics"
  - "ai"
  - "humanoid"
glossary_terms:
  - "glossary"
  - "terminology"
  - "definitions"
  - "robotics"
  - "ai"
---

# Glossary: Physical AI & Humanoid Robotics

This comprehensive glossary defines key terms used throughout the Physical AI & Humanoid Robotics textbook. Terms are organized alphabetically with definitions, pronunciations, and cross-references to relevant chapters.

## A

### Actuator
**Pronunciation**: /ˈæktʃuˌeɪtər/
**Definition**: A mechanical device for moving or controlling a mechanism or system, such as a motor that drives a humanoid robot's joints. In humanoid robotics, actuators must provide precise control with appropriate torque and speed characteristics for anthropomorphic movement.
**Category**: hardware
**Related Terms**: joint, motor, servo, torque
**First Mentioned**: Module 1, Chapter 1
**Use Cases**: Controlling humanoid joint positions, providing necessary force for locomotion and manipulation

### Artificial Intelligence (AI)
**Pronunciation**: /ˌɑr tɪˈfɪʃ əl ɪn tel ɪ jəns/
**Definition**: The simulation of human intelligence processes by machines, especially computer systems, particularly relevant for robotics applications involving perception, decision-making, and action execution.
**Category**: ai
**Related Terms**: machine learning, deep learning, cognitive planning
**First Mentioned**: Introduction
**Use Cases**: Robot decision making, perception, planning, natural language processing

### Anthropomorphic
**Pronunciation**: /ˌænθrəˈpɒmɔːrfɪk/
**Definition**: Having human form or human characteristics, particularly referring to humanoid robots designed with human-like body structure and movement capabilities.
**Category**: robotics
**Related Terms**: humanoid, bipedal, dexterous manipulation
**First Mentioned**: Introduction
**Use Cases**: Designing robots compatible with human environments and interaction patterns

## B

### Bipedal Locomotion
**Pronunciation**: /ˈbaɪˌped əl loʊ kə ˈmeɪ ʃən/
**Definition**: The act of walking on two legs, a fundamental capability for humanoid robots that requires sophisticated balance control and gait generation algorithms.
**Category**: locomotion
**Related Terms**: gait, balance control, zero moment point, center of pressure
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Humanoid walking, stair climbing, balance recovery

### Balance Control
**Pronunciation**: /ˈbæl əns kən ˈtroʊl/
**Definition**: Control systems designed to maintain a robot's stability, particularly critical for bipedal humanoid robots that must maintain balance on two points of contact with the ground.
**Category**: control
**Related Terms**: zero moment point, capture point, center of mass, ZMP
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Maintaining humanoid stability during walking, standing, and manipulation tasks

### Bayesian Filtering
**Pronunciation**: /ˈbeɪ zi ən ˈfɪl tər ɪŋ/
**Definition**: A mathematical approach for estimating the state of a system using Bayes' theorem to update probabilities based on new evidence, commonly used in robot localization and tracking.
**Category**: estimation
**Related Terms**: kalman filter, particle filter, localization, state estimation
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robot localization, sensor fusion, state estimation for humanoid navigation

## C

### Center of Mass (CoM)
**Pronunciation**: /ˈsen tər əv mæs/
**Definition**: The point in a body where the total mass of the body is considered to be concentrated for dynamic analysis, critical for humanoid balance and control.
**Category**: dynamics
**Related Terms**: zero moment point, balance control, kinematics, centroid
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Balance control, stability analysis, gait planning for humanoid robots

### Capture Point
**Pronunciation**: /ˈkæp tʃər pɔɪnt/
**Definition**: A point on the ground where a biped can step to stop its motion, used in humanoid balance control algorithms to ensure stable locomotion.
**Category**: balance
**Related Terms**: zero moment point, balance control, bipedal locomotion
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Balance recovery for humanoid robots, gait stability analysis

### Computer Vision
**Pronunciation**: /kəm ˈpjuː tər ˈvɪʒ ən/
**Definition**: A field of artificial intelligence that trains computers to interpret and understand the visual world, particularly relevant for humanoid robot perception systems.
**Category**: ai
**Related Terms**: SLAM, perception, image processing, object detection
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Object recognition, environment mapping, obstacle detection for humanoid navigation

### Control Theory
**Pronunciation**: /kən ˈtroʊl ˈθɪr i/
**Definition**: An interdisciplinary branch of engineering and mathematics that deals with the behavior of dynamical systems with inputs, and how their behavior is modified by feedback, essential for humanoid robot control.
**Category**: mathematics
**Related Terms**: PID control, feedback control, stability, transfer function
**First Mentioned**: Module 1, Chapter 4
**Use Cases**: Joint control, trajectory following, balance control for humanoid robots

## D

### Data Distribution Service (DDS)
**Pronunciation**: /ˈdeɪ tə dɪ strɪ bjut ˈsɜrv ɪs/
**Definition**: A middleware protocol and API standard for real-time, scalable, and reliable data distribution, serving as the communication layer for ROS 2.
**Category**: middleware
**Related Terms**: ROS 2, middleware, QoS, publisher-subscriber
**First Mentioned**: Module 1, Chapter 1
**Use Cases**: Real-time communication in robotic systems, Quality of Service management

### Deep Learning
**Pronunciation**: /diːp ˈlɜr nɪŋ/
**Definition**: A subset of machine learning based on artificial neural networks with representation learning, used in advanced robotics applications for perception and control.
**Category**: ai
**Related Terms**: neural network, machine learning, convolutional neural network, reinforcement learning
**First Mentioned**: Module 4, Introduction
**Use Cases**: Perception, control, cognitive planning in humanoid robots

### Digital Twin
**Pronunciation**: /ˈdɪdʒ ɪ təl twɪn/
**Definition**: A virtual representation of a physical object or system across its lifecycle, used extensively in robotics development and testing to validate behaviors before deployment on physical hardware.
**Category**: simulation
**Related Terms**: simulation, Gazebo, Isaac Sim, virtual testing
**First Mentioned**: Module 2, Introduction
**Use Cases**: Robot testing, validation, optimization, safety verification

### Degrees of Freedom (DOF)
**Pronunciation**: /dɪˈɡriːz əv ˈfraʊ dəm/
**Definition**: The number of independent movements or parameters that define the configuration or state of a mechanical system, critical for understanding humanoid robot kinematics.
**Category**: kinematics
**Related Terms**: joint, mobility, kinematic chain, configuration space
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Characterizing robot mobility, calculating workspace, determining controllability

## E

### Embodied Intelligence
**Pronunciation**: /ɪm bod i d ɪn tel ɪ dʒəns/
**Definition**: Intelligence that emerges from the interaction between an agent's physical form, its sensors and actuators, and its environment, forming the foundation of Physical AI concepts.
**Category**: ai
**Related Terms**: physical ai, morphological computation, sensorimotor coordination
**First Mentioned**: Introduction
**Use Cases**: Developing robots that learn from physical interaction, creating adaptive behaviors

### End Effector
**Pronunciation**: /ɛnd ɪˈfɛktər/
**Definition**: The device at the end of a robotic arm designed to interact with the environment, such as a gripper or tool, critical for humanoid manipulation tasks.
**Category**: hardware
**Related Terms**: manipulator, gripper, tool center point, dexterity
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Object manipulation, tool use, human-robot interaction

### Estimation Theory
**Pronunciation**: /ˌɛstɪˈmeɪʃən ˈθɪri/
**Definition**: A branch of statistics that deals with estimating the values of parameters based on measured/empirical data that has a random component, used in robotics for state estimation.
**Category**: mathematics
**Related Terms**: Kalman filter, particle filter, maximum likelihood, Bayesian inference
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robot localization, sensor fusion, state estimation for control

## F

### Forward Kinematics
**Pronunciation**: /ˈfɔrwərd kɪˈnɛmətɪks/
**Definition**: The use of kinematic equations to compute the position of the end-effector from the joint parameters of a robotic system, fundamental to robot control.
**Category**: kinematics
**Related Terms**: inverse kinematics, Jacobian, transformation matrix
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Robot pose calculation, trajectory planning, visualization

### Forward Dynamics
**Pronunciation**: /ˈfɔrwərd daɪˈnæmɪks/
**Definition**: The process of computing the motion of a mechanical system given the forces and torques applied to it, used in humanoid robot simulation and control.
**Category**: dynamics
**Related Terms**: inverse dynamics, Newton-Euler, Lagrangian mechanics
**First Mentioned**: Appendix D
**Use Cases**: Robot simulation, motion prediction, control system design

## G

### Gazebo
**Pronunciation**: /ɡəˈziːboʊ/
**Definition**: An open-source 3D robotics simulator that provides high-fidelity physics simulation and rendering for robot development, widely used for humanoid robot testing.
**Category**: simulation
**Related Terms**: simulation, digital twin, physics engine, ROS integration
**First Mentioned**: Module 2, Chapter 1
**Use Cases**: Robot testing, algorithm validation, sensor simulation, safety verification

### General-Purpose Robot (GPR)
**Pronunciation**: /ˈdʒɛnərəl ˈpɜrpəs roʊ bɑt/
**Definition**: A robot designed to perform a wide variety of tasks rather than being specialized for a single function, representing the goal for advanced humanoid robots.
**Category**: robotics
**Related Terms**: humanoid robot, multi-purpose, cognitive planning
**First Mentioned**: Introduction
**Use Cases**: Service robotics, assistance, human-robot interaction

### Geometric Jacobian
**Pronunciation**: /dʒɪˈɒmɪtrɪk dʒəˈkoʊbiən/
**Definition**: A matrix that relates the joint velocities of a robot to the end-effector twist (linear and angular velocities), essential for motion control and force analysis.
**Category**: kinematics
**Related Terms**: Jacobian, velocity kinematics, singularity, differential kinematics
**First Mentioned**: Appendix D
**Use Cases**: Motion control, singularity analysis, force control, trajectory planning

## H

### Hardware-in-the-Loop (HIL)
**Pronunciation**: /ˈhɑrdwer ɪn ðə ˈlup/
**Definition**: A testing technique that involves physical hardware components in a simulated environment for validation, particularly useful for humanoid robot control systems.
**Category**: testing
**Related Terms**: simulation, validation, real-time, rapid prototyping
**First Mentioned**: Module 2, Chapter 1
**Use Cases**: Controller validation, safety testing, performance evaluation

### Humanoid Robot
**Pronunciation**: /ˈhjuːmənɔɪd ˈroʊbɑt/
**Definition**: A robot with human-like characteristics, typically having a torso, head, two arms, and two legs, designed for operation in human environments and interaction.
**Category**: robotics
**Related Terms**: bipedal locomotion, anthropomorphic, dexterous manipulation
**First Mentioned**: Introduction
**Use Cases**: Service robotics, assistance, human-robot interaction, research platforms

## I

### Inverse Kinematics (IK)
**Pronunciation**: /ɪnˈvɜrs kɪˈnɛmətɪks/
**Definition**: The mathematical process of determining the joint parameters needed to place the end-effector at a desired position and orientation, critical for humanoid manipulation.
**Category**: kinematics
**Related Terms**: forward kinematics, Jacobian, trajectory planning, singularity
**First Mentioned**: Appendix D
**Use Cases**: Manipulation planning, reaching tasks, gait generation for humanoid robots

### Inverse Dynamics
**Pronunciation**: /ɪnˈvɜrs daɪˈnæmɪks/
**Definition**: The computation of forces and torques required to generate a specified motion, used in humanoid robot control to determine actuator commands.
**Category**: dynamics
**Related Terms**: forward dynamics, Newton-Euler, Lagrangian mechanics
**First Mentioned**: Appendix D
**Use Cases**: Robot control, trajectory optimization, force control

### Isaac Sim
**Pronunciation**: /ˈaɪzək sɪm/
**Definition**: NVIDIA's next-generation robotics simulation application based on NVIDIA Omniverse, designed for developing and testing AI-based robots with photorealistic rendering.
**Category**: simulation
**Related Terms**: digital twin, Gazebo, physics simulation, GPU acceleration
**First Mentioned**: Module 3, Chapter 1
**Use Cases**: High-fidelity simulation, AI training, perception testing, photorealistic rendering

## J

### Jacobian Matrix
**Pronunciation**: /dʒəˈkoʊbiən ˈmeɪtrɪks/
**Definition**: A matrix of partial derivatives that describes the local linear relationship between joint space and Cartesian space velocities in robotics, fundamental to motion control.
**Category**: mathematics
**Related Terms**: kinematics, differential kinematics, singularity, geometric Jacobian
**First Mentioned**: Appendix D
**Use Cases**: Motion control, singularity analysis, force control, differential kinematics

### Joint Space
**Pronunciation**: /dʒɔɪnt speɪs/
**Definition**: The space defined by the joint angles of a robot, where each dimension corresponds to a joint variable, used for robot control and planning.
**Category**: kinematics
**Related Terms**: Cartesian space, configuration space, workspace, joint limits
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Robot control, trajectory planning, inverse kinematics

## K

### Kinematics
**Pronunciation**: /kɪˈnɛmətɪks/
**Definition**: The study of motion without considering the forces that cause it, fundamental to robot modeling and control in humanoid robotics.
**Category**: mathematics
**Related Terms**: forward kinematics, inverse kinematics, dynamics, trajectory planning
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Robot modeling, trajectory planning, motion control, visualization

### Kalman Filter
**Pronunciation**: /ˈkælmən ˈfɪltər/
**Definition**: An algorithm that uses a series of measurements observed over time to estimate unknown variables, widely used in robotics for state estimation and sensor fusion.
**Category**: estimation
**Related Terms**: Bayesian filtering, sensor fusion, state estimation, extended Kalman filter
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robot localization, sensor fusion, state estimation, tracking

## L

### Locomotion
**Pronunciation**: /ˌloʊkəˈmoʊʃən/
**Definition**: The ability to move from one place to another, a critical capability for mobile robots including humanoid systems with bipedal walking.
**Category**: locomotion
**Related Terms**: gait, bipedal, navigation, walking patterns
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Navigation, walking, terrain adaptation, path following

### Machine Learning (ML)
**Pronunciation**: /məˈʃin ˈlɜrnɪŋ/
**Definition**: A method of data analysis that automates analytical model building using algorithms that iteratively learn from data, increasingly important in robotics applications.
**Category**: ai
**Related Terms**: artificial intelligence, deep learning, neural networks, reinforcement learning
**First Mentioned**: Module 4, Introduction
**Use Cases**: Perception, control, adaptation, planning in humanoid robots

### Manipulation
**Pronunciation**: /məˌnɪpjəˈleɪʃən/
**Definition**: The capability of a robot to physically interact with objects, typically using end-effectors to grasp, move, or modify objects, essential for humanoid dexterity.
**Category**: robotics
**Related Terms**: end-effector, gripper, dexterity, grasping
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Object handling, assembly, interaction, tool use

## N

### Neural Network
**Pronunciation**: /ˈnʊrəl ˈnɛtwɜrk/
**Definition**: A series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates, used in robotics AI.
**Category**: ai
**Related Terms**: deep learning, machine learning, perceptron, backpropagation
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Perception, control, decision making, learning in humanoid robots

### Node (ROS 2)
**Pronunciation**: /noʊd/
**Definition**: A process that performs computation in the ROS 2 computation graph, the fundamental unit of executable code in ROS 2 that enables modular robot software development.
**Category**: ros2
**Related Terms**: topic, service, publisher, subscriber, communication
**First Mentioned**: Module 1, Chapter 1
**Use Cases**: Robot control, sensor processing, communication, modular software design

### Numerical Integration
**Pronunciation**: /nuˈmɛrɪkəl ˌɪn tɪˈgreɪʃən/
**Definition**: A method for approximating the value of definite integrals using numerical techniques, essential for solving differential equations in robot dynamics simulation.
**Category**: mathematics
**Related Terms**: Runge-Kutta, Euler method, dynamics simulation, ODE solving
**First Mentioned**: Appendix D
**Use Cases**: Robot dynamics simulation, trajectory integration, state prediction

## P

### Perception
**Pronunciation**: /pərˈsɛpʃən/
**Definition**: The ability of a robot to interpret sensory information from its environment, essential for autonomous operation and interaction in humanoid robotics.
**Category**: ai
**Related Terms**: computer vision, sensor fusion, SLAM, object recognition
**First Mentioned**: Module 2, Chapter 3
**Use Cases**: Object recognition, environment mapping, obstacle detection, scene understanding

### Physics Engine
**Pronunciation**: /ˈfɪzɪks ˈɛndʒɪn/
**Definition**: Software that simulates the physical properties and interactions of objects in a virtual environment, critical for realistic humanoid robot simulation.
**Category**: simulation
**Related Terms**: simulation, Gazebo, Isaac Sim, collision detection, dynamics
**First Mentioned**: Module 2, Chapter 1
**Use Cases**: Robot simulation, testing, validation, safety verification

### Proportional-Integral-Derivative (PID) Control
**Pronunciation**: /ˈproʊpɔrʃənl ˈɪntɪɡrəl ˈdɛrɪvətɪv kənˈtroʊl/
**Definition**: A control loop mechanism employing feedback that is widely used in robotics for precise control of joint positions, velocities, and forces.
**Category**: control
**Related Terms**: feedback control, control theory, joint control, stability
**First Mentioned**: Module 1, Chapter 4
**Use Cases**: Joint position control, trajectory following, force control

## Q

### Quality of Service (QoS)
**Pronunciation**: /ˈkwɑləti əv ˈsɜrvɪs/
**Definition**: A set of policies that define how messages are delivered between publishers and subscribers in ROS 2, critical for real-time humanoid robot communication.
**Category**: communication
**Related Terms**: ROS 2, DDS, reliability, durability, deadline
**First Mentioned**: Module 1, Chapter 1
**Use Cases**: Real-time communication, safety-critical systems, performance optimization

## R

### Robot Operating System 2 (ROS 2)
**Pronunciation**: /ˈroʊbɑt ˈɑpəreɪtɪŋ ˈsɪstəm tu/
**Definition**: Flexible framework for writing robot software, providing services designed for a heterogeneous computer cluster, the middleware for modern robotics development.
**Category**: middleware
**Related Terms**: node, topic, service, action, communication
**First Mentioned**: Module 1, Introduction
**Use Cases**: Robot development, communication, integration, tooling

### ROS 2 Humble Hawksbill
**Pronunciation**: /roʊs tu ˈhʌmbəl ˈhɔksbɪl/
**Definition**: The Long-Term Support (LTS) distribution of ROS 2, released in May 2022 and supported until May 2027, the recommended version for humanoid robotics projects.
**Category**: ros2
**Related Terms**: ROS 2, distribution, LTS, middleware
**First Mentioned**: Module 1, Introduction
**Use Cases**: Stable robot development, long-term projects, industrial applications

### Reinforcement Learning
**Pronunciation**: /ˌriɪnfɔrsˈmɛnt ˈlɜrnɪŋ/
**Definition**: A type of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties, applicable to humanoid robot control.
**Category**: ai
**Related Terms**: machine learning, artificial intelligence, Q-learning, policy gradient
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Motor skill learning, adaptive control, behavior optimization

## S

### Simultaneous Localization and Mapping (SLAM)
**Pronunciation**: /sɪməlˈteɪniəs ˌloʊkəlaɪˈzeɪʃən ənd ˈmæpɪŋ/
**Definition**: The computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.
**Category**: perception
**Related Terms**: perception, localization, mapping, computer vision, EKF
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robot navigation, environment mapping, autonomous operation

### Simulation
**Pronunciation**: /ˌsɪmjəˈleɪʃən/
**Definition**: The imitation of the operation of a real-world process or system over time, crucial for robot development and testing especially for humanoid robots.
**Category**: simulation
**Related Terms**: Gazebo, Isaac Sim, digital twin, physics engine, testing
**First Mentioned**: Module 2, Introduction
**Use Cases**: Robot testing, algorithm validation, safety verification, training

### State Estimation
**Pronunciation**: /steɪt ˌɛstɪˈmeɪʃən/
**Definition**: The process of estimating the internal state of a dynamic system from noisy measurements, critical for humanoid robot control and navigation.
**Category**: estimation
**Related Terms**: Kalman filter, particle filter, sensor fusion, Bayesian inference
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robot localization, sensor fusion, control system feedback

## T

### Topic (ROS 2)
**Pronunciation**: /ˈtoʊpɪk/
**Definition**: A named bus over which nodes exchange messages in a publish-subscribe communication pattern in ROS 2, the primary communication mechanism for data streams.
**Category**: ros2
**Related Terms**: node, publisher, subscriber, message, communication
**First Mentioned**: Module 1, Chapter 1
**Use Cases**: Sensor data streaming, state broadcasting, communication

### Trajectory Planning
**Pronunciation**: /trəˈdʒɛktəri ˈpleɪnɪŋ/
**Definition**: The process of creating a path that a robot should follow through space and time, particularly complex for humanoid robots with many degrees of freedom.
**Category**: planning
**Related Terms**: path planning, motion planning, waypoints, optimization
**First Mentioned**: Module 3, Chapter 3
**Use Cases**: Movement generation, obstacle avoidance, task execution

## U

### Unified Robot Description Format (URDF)
**Pronunciation**: /juˈnaɪf aɪd roʊˈbɑt dɪˈskrɪpʃən ˈfɔrmæt/
**Definition**: An XML format for representing a robot model, including kinematic and dynamic properties, visual appearance, and collision geometry, essential for humanoid robots.
**Category**: modeling
**Related Terms**: robot model, XML, kinematics, dynamics, collision
**First Mentioned**: Module 1, Chapter 3
**Use Cases**: Robot modeling, simulation, visualization, kinematic analysis

### Uncertainty Quantification
**Pronunciation**: /ʌnˈsɜrtənti ˌkwɑntəfɪˈkeɪʃən/
**Definition**: The science of quantifying and managing uncertainties in computational and real-world applications, critical for robust humanoid robot operation.
**Category**: mathematics
**Related Terms**: probability, statistics, sensor noise, robust control
**First Mentioned**: Module 4, Chapter 2
**Use Cases**: Robust control, sensor fusion, path planning, decision making

## V

### Vision-Language-Action (VLA) Model
**Pronunciation**: /ˈvɪʒən ˈleɪɡwɪdʒ ˈækʃən ˈmɑdəl/
**Definition**: A type of AI model that can process visual input, understand natural language commands, and generate appropriate robotic actions, representing the state of the art in cognitive robotics.
**Category**: ai
**Related Terms**: artificial intelligence, cognitive planning, perception, RT-2, OpenVLA
**First Mentioned**: Module 4, Introduction
**Use Cases**: Voice-controlled robots, cognitive planning, human-robot interaction

### VSLAM (Visual SLAM)
**Pronunciation**: /ˈviː ˈes ˈel ˈeɪ ˈem/
**Definition**: A technique for SLAM that uses visual sensors such as cameras to construct maps and localize robots, particularly relevant for humanoid robots in human environments.
**Category**: perception
**Related Terms**: SLAM, computer vision, perception, ORB-SLAM, RTAB-MAP
**First Mentioned**: Module 3, Chapter 2
**Use Cases**: Visual navigation, environment mapping, localization

### Velocity Kinematics
**Pronunciation**: /vəˈlɑsəti kɪˈnɛmətɪks/
**Definition**: The study of the relationship between joint velocities and end-effector velocities in robotic systems, essential for real-time motion control.
**Category**: kinematics
**Related Terms**: Jacobian, forward kinematics, differential kinematics, motion control
**First Mentioned**: Appendix D
**Use Cases**: Motion control, trajectory planning, real-time control

## Z

### Zero Moment Point (ZMP)
**Pronunciation**: /ˈzɪroʊ ˈmoʊmənt pɔɪnt/
**Definition**: A criterion for static and dynamic stability of legged robots, representing the point where the sum of all moments of the active forces equals zero, fundamental to humanoid balance.
**Category**: dynamics
**Related Terms**: balance control, bipedal locomotion, stability, capture point
**First Mentioned**: Appendix D
**Use Cases**: Gait generation, balance control, stability analysis for humanoid robots

---

This glossary contains definitions for key terms used throughout the Physical AI & Humanoid Robotics textbook. Each term includes pronunciation, definition, category, related terms, and the first chapter where it was mentioned. The glossary will continue to expand as new terms are introduced throughout the course.