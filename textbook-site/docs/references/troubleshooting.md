---
title: "Troubleshooting Guide"
description: "Common issues and solutions for Physical AI & Humanoid Robotics development with ROS 2, Gazebo, Isaac Sim, and VLA models"
estimated_time: 2
week: 14
module: "References"
prerequisites: []
learning_objectives:
  - "Identify and resolve common robotics development issues in humanoid systems"
  - "Apply debugging techniques for ROS 2 systems in humanoid applications"
  - "Troubleshoot simulation and hardware integration problems for humanoid robots"
  - "Validate and diagnose AI model integration issues in humanoid robotics"
  - "Implement systematic debugging approaches for complex humanoid systems"
sidebar_label: "Troubleshooting"
difficulty: "Intermediate"
tags:
  - "troubleshooting"
  - "debugging"
  - "issues"
  - "solutions"
  - "humanoid-robotics"
  - "ros2"
  - "simulation"
  - "ai"
glossary_terms:
  - "troubleshooting"
  - "debugging"
  - "diagnostics"
  - "issue-resolution"
  - "robotics-debugging"
---

# Troubleshooting Guide: Physical AI & Humanoid Robotics

## Introduction

This troubleshooting guide provides solutions to common issues encountered when developing with ROS 2, simulation environments, AI models, and hardware integration in humanoid robotics applications. The guide is organized by system component and includes diagnostic procedures, solutions, and preventive measures specific to humanoid robotics development.

According to research by Fedder et al. (2019), effective troubleshooting and debugging capabilities are essential for robotics development, with 60% of development time often spent on diagnosing and resolving issues. For humanoid robotics, where systems are particularly complex and safety considerations are paramount, systematic troubleshooting approaches are critical for efficient development.

## ROS 2 Troubleshooting

### Common Node Issues

#### Node Not Connecting to ROS 2 Network
**Symptoms**: Nodes cannot communicate, `ros2 topic list` shows no topics, publisher/subscriber connections fail

**Diagnosis**:
```bash
# Check if ROS daemon is running
ros2 daemon status

# Check ROS domain ID
echo $ROS_DOMAIN_ID

# Verify network configuration
ip addr show | grep -E "(inet|ether)"

# Check for multiple ROS distributions sourced
echo $ROS_DISTRO
```

**Solutions**:
1. Restart the ROS 2 daemon:
   ```bash
   ros2 daemon stop && ros2 daemon start
   ```

2. Verify same domain ID across all terminals:
   ```bash
   export ROS_DOMAIN_ID=0  # Use same value for all terminals
   ```

3. Check firewall settings that may block DDS communication:
   ```bash
   # Temporarily disable firewall for testing
   sudo ufw disable  # For Ubuntu systems
   ```

4. Verify network interface settings for multi-machine setups:
   ```bash
   export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
   export CYCLONEDDS_URI='<CycloneDDS><Domain><General create_default_participant_factory="true"/></Domain></CycloneDDS>'
   ```

#### Topic/Service Not Found
**Symptoms**: Publishers/subscribers cannot connect, services unavailable, action servers not responding

**Diagnosis**:
```bash
# Verify node is running
ros2 node list

# Check topic/service names
ros2 topic list
ros2 service list

# Check for typos in topic/service names
ros2 topic info /topic_name
```

**Solutions**:
1. Verify topic/service names match exactly (case-sensitive)
2. Check that nodes are running and properly initialized
3. Confirm QoS settings are compatible between publishers and subscribers
4. Check for namespace issues if using prefixed topics

### Performance Issues

#### High CPU Usage
**Symptoms**: Nodes consuming excessive CPU resources, slow response times, dropped messages

**Diagnosis**:
```bash
# Monitor CPU usage
htop
# Look for ROS 2 processes consuming high CPU

# Check node update rates
ros2 run topic_tools relay --help  # Check for frequent publications
```

**Solutions**:
1. Reduce loop rates in nodes:
   ```python
   # Instead of tight loops, use appropriate sleep times
   rate = node.create_rate(100)  # 100 Hz instead of max speed
   rate.sleep()
   ```

2. Optimize QoS settings:
   ```python
   # Use appropriate history depth
   qos_profile = QoSProfile(
       depth=1,  # Only keep most recent message for control commands
       reliability=ReliabilityPolicy.RELIABLE
   )
   ```

3. Check for infinite loops or inefficient algorithms
4. Profile code to identify bottlenecks using tools like `cProfile`

#### Memory Leaks
**Symptoms**: Gradually increasing memory usage over time, eventual system slowdown or crashes

**Diagnosis**:
```bash
# Monitor memory usage over time
watch -n 1 'ps aux | grep -i ros | sort -k4 -nr | head -10'

# Use memory profiling tools
pip install memory-profiler
python -m memory_profiler your_script.py
```

**Solutions**:
1. Properly manage message callbacks and avoid retaining unnecessary references
2. Use weak references when appropriate to prevent circular references
3. Monitor memory usage with `htop` or similar tools
4. Check for circular references in Python nodes

### Humanoid-Specific ROS 2 Issues

#### Joint State Synchronization Issues
**Symptoms**: Joint positions not updating in simulation, desynchronized joint states, timing issues

**Diagnosis**:
```bash
# Check joint state publication rate
ros2 topic hz /joint_states

# Verify joint names match between different nodes
ros2 topic echo /joint_states --field name

# Check for message drops
ros2 topic info /joint_states
```

**Solutions**:
1. Increase QoS history depth for joint states:
   ```python
   joint_state_qos = QoSProfile(
       depth=10,  # More history for joint states
       reliability=ReliabilityPolicy.RELIABLE
   )
   ```

2. Ensure proper timing synchronization between controllers and state publishers
3. Check for hardware interface issues in real robots

## Simulation Troubleshooting

### Gazebo Issues

#### Gazebo Fails to Start
**Symptoms**: Gazebo crashes immediately, segmentation fault, unable to initialize graphics

**Diagnosis**:
```bash
# Check graphics drivers
nvidia-smi
glxinfo | grep "OpenGL renderer"

# Check for missing dependencies
ldd $(which gz)  # or gazebo depending on version

# Check for GPU memory issues
nvidia-smi
```

**Solutions**:
1. Verify graphics drivers and OpenGL support:
   ```bash
   # Install graphics dependencies
   sudo apt update
   sudo apt install nvidia-driver-XXX  # Replace XXX with appropriate version
   sudo apt install mesa-utils
   ```

2. Try software rendering:
   ```bash
   export LIBGL_ALWAYS_SOFTWARE=1
   gz sim -s  # or gazebo -s for older versions
   ```

3. Check for GPU memory issues and close other GPU-intensive applications

#### Physics Simulation Problems
**Symptoms**: Robots falling through floors, unrealistic movements, joint limit violations, unstable simulation

**Diagnosis**:
```bash
# Check physics engine status
gz service -s /world/default/physics/info

# Verify URDF/SDF model correctness
check_urdf your_robot.urdf

# Check for mass/inertia issues
gz topic -e -t /world/default/dynamic_pose/info
```

**Solutions**:
1. Verify collision and visual model definitions in URDF/SDF
2. Adjust physics parameters (step size, solver settings):
   ```xml
   <!-- In SDF physics configuration -->
   <physics type="ode">
     <max_step_size>0.001</max_step_size>  <!-- Smaller step size for stability -->
     <real_time_factor>1.0</real_time_factor>
     <real_time_update_rate>1000</real_time_update_rate>
   </physics>
   ```

3. Check mass and inertia properties of links:
   ```xml
   <!-- Ensure realistic mass and proper inertia tensors -->
   <inertial>
     <mass>0.1</mass>
     <inertia>
       <ixx>0.001</ixx>
       <ixy>0</ixy>
       <ixz>0</ixz>
       <iyy>0.001</iyy>
       <iyz>0</iyz>
       <izz>0.001</izz>
     </inertia>
   </inertial>
   ```

#### Sensor Data Issues
**Symptoms**: No sensor data, unrealistic values, high noise, or inconsistent readings

**Diagnosis**:
```bash
# Check if sensor topics are being published
ros2 topic list | grep -i sensor

# Monitor sensor data
ros2 topic echo /sensor_topic_name

# Check sensor plugin configuration
gz model -m robot_name --info  # Check model details
```

**Solutions**:
1. Verify sensor plugin configurations in URDF/SDF:
   ```xml
   <sensor name="camera" type="camera">
     <camera>
       <horizontal_fov>1.047</horizontal_fov>
       <image>
         <width>640</width>
         <height>480</height>
       </image>
       <clip>
         <near>0.1</near>
         <far>10.0</far>
       </clip>
     </camera>
     <always_on>true</always_on>
     <update_rate>30</update_rate>
     <topic>camera/image_raw</topic>
   </sensor>
   ```

2. Check sensor frame transforms:
   ```bash
   ros2 run tf2_tools view_frames
   ros2 run rqt_tf_tree rqt_tf_tree
   ```

3. Adjust sensor noise parameters for more realistic simulation

### Isaac Sim Issues

#### Isaac Sim Not Launching
**Symptoms**: Isaac Sim fails to start, crashes during initialization, or doesn't open the application window

**Diagnosis**:
```bash
# Check NVIDIA GPU and CUDA
nvidia-smi
nvcc --version

# Check Isaac Sim installation
ls -la ~/.local/share/ov/pkg/
ls -la /opt/nvidia/isaac_sim/

# Check for permission issues
ls -la ~/isaac_sim_workspace/
```

**Solutions**:
1. Verify NVIDIA GPU with CUDA support:
   ```bash
   # Check GPU compute capability
   nvidia-smi -q -d COMPUTE
   ```

2. Check Isaac Sim installation and dependencies:
   ```bash
   # Install Isaac Sim prerequisites
   sudo apt install cuda-toolkit-12-1  # Match your Isaac Sim version
   ```

3. Verify Omniverse connection and authentication if using cloud services

#### Performance Problems in Isaac Sim
**Symptoms**: Low frame rates, simulation instability, long loading times, GPU memory exhaustion

**Diagnosis**:
```bash
# Monitor GPU usage
nvidia-smi -l 1

# Check scene complexity
# Look for high-polygon models, complex lighting, large scenes

# Monitor memory usage
htop
```

**Solutions**:
1. Adjust rendering quality settings in Isaac Sim preferences
2. Simplify scene complexity by reducing polygon counts
3. Monitor GPU memory usage and close unnecessary applications
4. Consider using lower-resolution textures for development

## AI/ML Troubleshooting

### API Connection Issues

#### OpenAI API Connection Failures
**Symptoms**: Whisper or GPT API calls failing, timeout errors, authentication failures

**Diagnosis**:
```bash
# Check API key is set
echo $OPENAI_API_KEY

# Test API connectivity
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Check network connectivity
ping api.openai.com
```

**Solutions**:
1. Verify API key is properly set in environment variables:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

2. Check internet connection and firewall settings:
   ```bash
   # Check proxy settings if behind corporate firewall
   env | grep -i proxy
   ```

3. Verify API usage limits and billing status in OpenAI dashboard

#### Rate Limiting Issues
**Symptoms**: API calls being rejected due to rate limits, intermittent failures, quota exceeded errors

**Solutions**:
1. Implement exponential backoff in API calls:
   ```python
   import time
   import random

   def make_api_call_with_backoff(api_function, max_retries=5):
       for attempt in range(max_retries):
           try:
               return api_function()
           except RateLimitError as e:
               if attempt == max_retries - 1:
                   raise e
               sleep_time = (2 ** attempt) + random.uniform(0, 1)
               time.sleep(sleep_time)
   ```

2. Add delays between consecutive API requests
3. Consider using local models for high-frequency operations

## Hardware Integration Issues

### Jetson Orin Nano Problems

#### Performance Limitations
**Symptoms**: AI models running slowly, thermal throttling, system instability, high CPU/GPU usage

**Diagnosis**:
```bash
# Check thermal status
sudo tegrastats  # Shows real-time thermal and power stats

# Monitor performance
jetson_stats

# Check memory usage
free -h
```

**Solutions**:
1. Improve thermal management:
   ```bash
   # Install heatsink/fan if not already installed
   # Monitor temperature and implement thermal throttling in software
   ```

2. Optimize models for edge deployment:
   ```bash
   # Use model quantization
   python -c "import torch; print(torch.__version__)"
   # Apply INT8 quantization for faster inference
   ```

3. Reduce model complexity or resolution for real-time performance

#### Memory Constraints
**Symptoms**: Out of memory errors, model loading failures, system crashes during inference

**Solutions**:
1. Reduce batch sizes in inference:
   ```python
   # Use batch_size=1 for edge deployment
   batch_size = 1
   ```

2. Optimize models for memory usage through quantization
3. Monitor memory usage and implement proper resource management

## Network and Communication Issues

### ROS 2 Network Problems

#### Multi-Robot Communication
**Symptoms**: Robots cannot communicate across network, cross-robot topics unavailable, discovery issues

**Diagnosis**:
```bash
# Check ROS domain IDs
echo $ROS_DOMAIN_ID  # Should be same on all robots

# Check network connectivity
ping other_robot_ip

# Check firewall settings
sudo ufw status
```

**Solutions**:
1. Ensure consistent `ROS_DOMAIN_ID` across robots:
   ```bash
   export ROS_DOMAIN_ID=1  # Same on all robots in the system
   ```

2. Configure firewall to allow DDS communication:
   ```bash
   # Open necessary ports for DDS (varies by DDS implementation)
   sudo ufw allow from robot_subnet  # Allow traffic from robot subnet
   ```

3. Verify IP address configuration and network topology

#### Latency Issues
**Symptoms**: High latency in command execution, delayed sensor feedback, poor real-time performance

**Solutions**:
1. Optimize QoS settings for real-time requirements:
   ```python
   # Use reliable communication for critical data
   critical_qos = QoSProfile(
       depth=1,
       reliability=ReliabilityPolicy.RELIABLE,
       durability=DurabilityPolicy.VOLATILE,
       deadline=Duration(seconds=0.01)  # 10ms deadline for critical data
   )
   ```

2. Use appropriate transport protocols (UDP for non-critical, TCP for critical)
3. Monitor network bandwidth and congestion

## Development Environment Issues

### Build and Dependency Problems

#### Package Build Failures
**Symptoms**: `colcon build` fails, missing dependencies, compilation errors

**Diagnosis**:
```bash
# Check for missing dependencies
rosdep check --from-paths src --ignore-src

# Verify ROS 2 installation
source /opt/ros/humble/setup.bash
echo $ROS_DISTRO

# Check for compilation errors
colcon build --event-handlers console_direct+
```

**Solutions**:
1. Update package lists and install missing dependencies:
   ```bash
   sudo apt update
   rosdep install --from-paths src --ignore-src -r -y
   ```

2. Check compiler compatibility and ROS 2 distribution alignment
3. Verify workspace structure and package.xml files

#### Python Environment Problems
**Symptoms**: Import errors, missing packages, version conflicts, virtual environment issues

**Solutions**:
1. Use virtual environments for project isolation:
   ```bash
   python3 -m venv humanoid_env
   source humanoid_env/bin/activate
   pip install -r requirements.txt
   ```

2. Verify Python version compatibility (3.10+ for ROS 2 Humble):
   ```bash
   python3 --version
   which python3
   ```

3. Check for conflicting package installations and use proper dependency management

## Debugging Techniques

### ROS 2 Debugging Tools

#### Using rqt Tools
- `rqt_graph`: Visualize the ROS 2 computation graph to see node connections
- `rqt_plot`: Plot numerical values from topics to analyze signal behavior
- `rqt_console`: Monitor log messages from all nodes
- `rqt_bag`: Record and replay data for debugging sessions

#### Command Line Debugging
```bash
# Monitor topics and their rates
ros2 topic echo /topic_name
ros2 topic hz /topic_name

# Check node status and connections
ros2 node info node_name
ros2 run topic_tools echo_delay /topic_name

# Debug launch files
ros2 launch --dry-run package_name launch_file.py
```

### Simulation Debugging

#### Gazebo Debugging
- Enable verbose logging: `gz sim -v 4` for maximum verbosity
- Check physics parameters in SDF files for realistic values
- Validate transforms using `ros2 run tf2_tools view_frames`

#### Isaac Sim Debugging
- Monitor Isaac Sim logs in `~/.nvidia-omniverse/logs/`
- Use Isaac Sim's built-in debugging tools and visualizers
- Validate USD stage files for proper scene structure

## Common Error Messages and Solutions

### "Address already in use" Error
**Cause**: Port conflict when starting multiple instances or processes
**Solution**: Change `ROS_DOMAIN_ID` or ensure proper cleanup of previous processes

### "Failed to load URDF" Error
**Cause**: Invalid URDF syntax, missing mesh files, or incorrect file paths
**Solution**: Validate URDF with `check_urdf` tool and verify all file paths exist

### "CUDA error: out of memory"
**Cause**: Insufficient GPU memory for model inference or simulation
**Solution**: Reduce batch size, use model quantization, or close other GPU applications

### "Unable to register type" in DDS
**Cause**: Type definition conflicts between different nodes
**Solution**: Ensure all nodes use the same message definitions and rebuild workspace

## Prevention Strategies

### Development Best Practices
1. **Version Control**: Use Git for all code and configurations with proper branching strategies
2. **Environment Isolation**: Use virtual environments and containerization for dependency management
3. **Incremental Testing**: Test components individually before integration
4. **Documentation**: Maintain clear documentation of configurations and dependencies
5. **Backup Plans**: Keep backup configurations and development environments

### Systematic Debugging Approach
1. **Reproduce**: Confirm you can consistently reproduce the issue
2. **Isolate**: Narrow down which component or configuration causes the issue
3. **Hypothesize**: Formulate theories about the root cause
4. **Test**: Test your theories with minimal changes
5. **Verify**: Confirm the fix resolves the issue without creating new problems

## Hardware-Specific Troubleshooting

### Unitree Robots
- **Connection Issues**: Verify USB/Ethernet connection and check for driver updates
- **Joint Calibration**: Follow manufacturer's calibration procedures if joints behave unexpectedly
- **Firmware Updates**: Keep robot firmware updated to latest stable version

### Hiwonder TonyPi Pro
- **Servo Issues**: Check servo connections and power supply stability
- **SDK Compatibility**: Ensure SDK version matches robot firmware version
- **Motion Planning**: Verify motion planning parameters are appropriate for the robot's physical limits

## Simulation-Specific Issues

### Physics Engine Tuning
For humanoid robots, physics parameters need special attention:

```yaml
# Example physics configuration for humanoid simulation
physics:
  step_size: 0.001  # Smaller for humanoid stability
  solver_iterations: 50  # Higher for stability
  contact_surface_layer: 0.001  # Prevent sinking
  friction_pyramid_scheme: true  # Better for humanoid contact
```

### Real-time Performance
Humanoid robots require real-time performance:

- Monitor real-time factor (should be close to 1.0)
- Use appropriate solver settings for stability
- Limit scene complexity during development
- Consider using simpler collision geometries for controllers

## Validation and Testing

### System Validation Checklist
- [ ] All nodes start without errors
- [ ] Topics are publishing/subscribing correctly
- [ ] Joint states update at appropriate rates
- [ ] Control commands are received and executed
- [ ] Sensors provide realistic data
- [ ] Safety systems are operational
- [ ] Communication latencies are acceptable

### Performance Benchmarks
- **Joint State Rate**: 100-200 Hz for humanoid control
- **Control Loop Rate**: 100-500 Hz for stable humanoid control
- **Real-time Factor**: ≥0.9 for real-time simulation
- **CPU Usage**: `<80%` sustained for stability
- **Memory Usage**: Stable without leaks over time

## Getting Help

### Useful Commands for Diagnosis
```bash
# Comprehensive system check
source /opt/ros/humble/setup.bash
ros2 doctor

# Check all active topics and services
ros2 topic list && ros2 service list

# Monitor system resources
ros2 run top top

# Check for node connectivity issues
ros2 run topic_tools relay_test
```

### Resources
- ROS 2 Documentation: https://docs.ros.org/en/humble/
- Gazebo Documentation: https://gazebosim.org/docs/
- NVIDIA Isaac Documentation: https://docs.omniverse.nvidia.com/isaacsim/
- GitHub Issues for specific packages and repositories
- Robotics Stack Exchange for community support
- Manufacturer documentation for specific hardware platforms

## Emergency Procedures

### Safety Shutdown Procedures
For humanoid robots, have emergency procedures ready:

1. **Immediate Stop**: Implement emergency stop services that can be called from any node
2. **Safe Position**: Have a service to move the robot to a safe position (e.g., sitting or crouching)
3. **Power Off**: Know how to safely cut power to actuators if needed
4. **Communication Loss**: Have timeout procedures for lost communication

### Recovery Steps
After an issue occurs:
1. **Assess**: Check for any damage to hardware or environment
2. **Diagnose**: Use logs and diagnostic tools to understand the cause
3. **Fix**: Apply appropriate solution based on diagnosis
4. **Test**: Verify the fix works and doesn't introduce new issues
5. **Document**: Record the issue and solution for future reference

This troubleshooting guide will continue to expand as new issues are encountered during the course. Always verify basic system requirements and configurations before diving into complex debugging procedures.