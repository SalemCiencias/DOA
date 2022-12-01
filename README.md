# DOA
**DOA Action Service**

## Para instalar

(Desde el workspace)
Primero hacer source de ros2 
```bash
source /opt/ros/foxy/setup.bash 
 ``` 
Generar archivo de permisos para el microfono
```bash
sudo cp -f config/60-respeaker.rules /etc/udev/rules.d/60-respeaker.rules
sudo systemctl restart udev
```
Compilar 
```bash
 colcon build
 ``` 
 Source del install
 ```bash
 . install/setup.bash
 ``` 
Correr el server
```bash
 ros2 run doa server
 ``` 
Pedir una meta al server desde consola
```bash
 ros2 action send_goal /doaaction action_doa/action/DOAaction "{orden: 0}" --feedback
 ``` 
Correr el cliente
```bash
 ros2 run doa client
 ``` 
No olvides sourcear los drivers la [kobuki](https://sites.google.com/ciencias.unam.mx/robotica-movil/kobuki-ros2)

---

[.](https://open.spotify.com/track/4jmLj7bALZTQoe93dT623W)

