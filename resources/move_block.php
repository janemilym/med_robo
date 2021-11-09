<?php
echo '<html>';
echo '<head>';
echo '</head>';
echo '<body>';
exec('/home/mariellacox/web/robot_parm.py 4D-300',$output);
exec('/home/mariellacox/web/robot_parm.py 0D445',$output);
exec('/home/mariellacox/web/robot_parm.py 1D30',$output);
exec('/home/mariellacox/web/robot_parm.py 2D406',$output);
exec('/home/mariellacox/web/robot_parm.py 3D403',$output);
sleep(2);

//wait_motor(0, 450, 440);
//wait_motor(1, 35, 25);
//wait_motor(2, 416, 400);
//wait_motor(3, 413, 400);
//wait_motor(4, -290, -300);

exec('/home/mariellacox/web/robot_parm.py 4D-178',$output);
//wait_motor(4, -172, -183);
sleep(3);

exec('/home/mariellacox/web/robot_parm.py 1D-450',$output);
exec('/home/mariellacox/web/robot_parm.py 2D0',$output);
sleep(3);
exec('/home/mariellacox/web/robot_parm.py 0D-445',$output);
sleep(3);
exec('/home/mariellacox/web/robot_parm.py 1D30',$output);
exec('/home/mariellacox/web/robot_parm.py 2D406',$output);
exec('/home/mariellacox/web/robot_parm.py 3D403',$output);
sleep(1);
exec('/home/mariellacox/web/robot_parm.py 4D-300',$output);
print_r($output);
echo '<form action="top.php" methode="post">';
echo '<input type="submit" value="Back">';
echo '</form>';
echo '</body>';
echo '</html>';

function wait_motor(int $m, int $lower, int $upper) {
  $cmd = '/home/mariellacox/web/robot_parm_w_read.py ' . $m . 'QD'; 
  $pos = 'junk';
  do {
    unset($pos);
    exec($cmd, $pos);
    $pos = $pos[3]; // set m0 to third element of m0, hopefully thr responce string
    $pos = substr($pos, 4);
  }  
  while($pos > $upper && $pos < $lower);
}
?>