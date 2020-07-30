#!/bin/bash

CWD=`dirname -- "$0"`
BAGFILE="../../assignments/assets/husky_navigation.bag"
RED='\033[0;31m'
NC='\033[0m'

cd $CWD
if [ ! -f "$BAGFILE" ]; then
  echo -e "${RED}>>> FILE NOT FOUND <<<${NC}"
  echo "Please follow instructions in module4.md to download the husky_navigation.bag file."
  exit -1
fi

CMD1="source ../devel/setup.bash; cd ../launch; roslaunch exercise4.launch"
CMD2="rviz -d ../config/exercise4.rviz"
CMD3="rosbag play --clock $BAGFILE"

xterm -hold -geometry 80x24+1000+000 -e "cd $CWD; $CMD1" &
sleep 5
xterm -hold -geometry 80x24+1490+000 -e "cd $CWD; $CMD2" &

echo "Be sure to click the [play] button on rqt_multiplot."
echo "Starting ROS bag replay in"
let count=5
while [[ $count -gt 0 ]]; do
  echo -e "\t$count"
  let count-=1
  sleep 1
done

xterm -hold -geometry 80x24+1000+380 -e "cd $CWD; $CMD3" &