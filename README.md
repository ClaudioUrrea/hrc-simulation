# HRC Simulation Backup

Este repositorio contiene los scripts y datos generados para las simulaciones del paper "Advancing Human-Robot Collaboration in Industrial Automation: A Hybrid Deep Learning and Reinforcement Learning Framework for Adaptive Task Allocation".

## Estructura del Repositorio
- `human_state_publisher.py`: Script ROS para simular el trabajador humano virtual.
- `generate_synthetic_data.py`: Script Python para generar el conjunto de datos sintéticos.
- `synthetic_hrc_data.csv`: Conjunto de datos sintéticos con 10,000 episodios.
- `plot_throughput.m`: Script MATLAB para generar el gráfico de barras (Figure 1).

## Configuraciones del UR5e
- **Paquete ROS**: `universal_robot` (incluye `ur_gazebo` y `ur_description`).
- **Parámetros del `shoulder_pan_joint`**:
  - `effort: 120.0`
  - `damping: 5.8`
  - `friction: 5.8`
- **Parámetros PID del controlador**:
  - `p: 0.000001`
  - `i: 0.0`
  - `d: 8000.0`
- **Configuración de Gazebo**:
  - `--step-size=0.0001`
  - `--max-update-rate=1000`
  - `-e ode`

## Instrucciones para Rehacer las Simulaciones
1. Configurar el entorno:
   - Ubuntu 20.04, ROS Noetic, Gazebo 11.
   - Instalar dependencias: `sudo apt install ros-noetic-universal-robot ros-noetic-gazebo-ros`.
   - Crear espacio de trabajo: `mkdir -p ~/gazebo_ws/src && cd ~/gazebo_ws && catkin_make`.
   - Copiar el paquete `universal_robot` a `~/gazebo_ws/src`.
2. Configurar el paquete `my_package`:
   - `cd ~/gazebo_ws/src && catkin_create_pkg my_package std_msgs rospy`.
   - Copiar los scripts `human_state_publisher.py` y `generate_synthetic_data.py` a `~/gazebo_ws/src/my_package/scripts`.
   - Compilar: `cd ~/gazebo_ws && catkin_make && source devel/setup.bash`.
3. Lanzar la simulación del UR5e:
   - `roslaunch ur_gazebo ur5e.launch` (o el archivo de lanzamiento correspondiente).
   - Ajustar parámetros del UR5e según las configuraciones arriba.
4. Ejecutar el trabajador humano virtual:
   - `rosrun my_package human_state_publisher.py`.
5. Leer datos desde MATLAB:
   - Configurar MATLAB: `setenv('ROS_MASTER_URI', 'http://192.168.198.134:11311'); setenv('ROS_IP', '192.168.248.1'); rosinit('http://192.168.198.134:11311')`.
   - Leer datos: `sub = rossubscriber('/human_state', 'std_msgs/Float32MultiArray'); msg = receive(sub, 10); human_state = msg.Data; disp(human_state)`.
6. Generar datos sintéticos:
   - `python3 ~/gazebo_ws/src/my_package/scripts/generate_synthetic_data.py`.
7. Visualizar resultados:
   - Usar el script `plot_throughput.m` en MATLAB.

## Notas
- Gazebo Classic 11 está obsoleto desde enero de 2025. Considerar migrar a Gazebo Sim para futuras simulaciones.
