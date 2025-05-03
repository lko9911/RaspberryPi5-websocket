# 라즈베리파이랑 연동한는 임시 웹소켓 코드 - websocket_pkg 랑 연동함

### 목적 : py를 실행하면 ros 터미널에 정보를 넘김 (vs code랑 ros 플랫폼 분리)

### 실행 방법
<pre><code> run ros2 websocket_pkg ws_to_ros_publisher </pre></code> <br>
실행 후 "ws_client.py" 파일 실행 하면 ws_client 정보를 넘김 (여기서는 라즈베리파이의 로컬 IP 주소를 사용했기에 다른 환경에서 정보를 줄거면 그 장치의 로컬 IP로 바꿔야 함)

<pre><code> run ros2 websocket_pkg ik_to_ws_publisher </pre></code> <br>
실행 후 "ws_server.py" 파일 실행 하면 ROS2 터미널로부터 정보를 받음 (단, k_to_ws_publisher.py에서 uri에 기입한 ip와 포트정보가 일치해야 함)
