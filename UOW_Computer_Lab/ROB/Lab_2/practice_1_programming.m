function practice_1_programming
global robot TD_gripper RT_initial RT_approach RT_grip RT_approach2 RT_release

% Load the robot
robot = load_robot('ABB','IRB140');
robot.equipment(1) = load_robot('equipment', 'tables/table_two_areas');
robot.tool = load_robot('equipment','end_tools/parallel_gripper_0');
robot.piece(1) = load_robot('equipment','cylinders/cylinder_tiny');
robot.graphical.draw_axes = 0;

% Initialize the position of the piece at the beginning of the simulation
robot.piece(1).T0(1:3,4) = [-0.1,-0.5,0.2];

% robot.tool.piece_gripped = 0;
drawrobot3d(robot,robot.q)

% Define the tool
% In RAPID this is don by means of the tooldata structure
TD_gripper = []

% Define target point for SIMULATION
RT_intial = []
RT_approach = []
RT_grip = []
RT_grip = []
RT_approach2 = []
RT_release = []
main
end

function main()
global robot TD_gripper RT_initial RT_approach RT_grip RT_approach2 RT_release

% Close the tool
simulation_close_tool; % Set do1

% Move the inital point
MoveJ(RT_inital, 'vmax','fine', TD_gripper,'wobj0');

% Now open the tool
simulation_open_tool; % Reset do1

% Move to the approaching point
MoveJ(RT_approach1,'vmax','fine',TD_gripper,'wobj0');

% Now, go down to the grabbing target point and
MoveL(RT_grip,'vmax','fine',TD_gripper,'wobj0');

% and close the tool and grip the piece. These two functions
% must be called to simulate that the gripper has the piece grabbed and the
% tool is closed
simulation_close_tool; % Set do1
simulation_grip_piece; 

% Now go to the same approach point so that the collision with the table is
% avoided
MoveL(RT_approach1,'vmax','fine'





end
